#!/usr/bin/env python3
"""Extract a Bilibili multi-part video's spoken content into reference Markdown files.

Adapts the evidence contract of the `douyin-reference-transcript` skill to Bilibili:
local whisper.cpp ASR, timestamp coverage validation, internal-gap detection,
verified/partial/unknown labeling, and temporary-media cleanup.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.parse
from typing import Any


UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
REFERER = "https://www.bilibili.com/"
NAV_URL = "https://api.bilibili.com/x/web-interface/nav"
VIEW_URL = "https://api.bilibili.com/x/web-interface/view"
PAGELIST_URL = "https://api.bilibili.com/x/player/pagelist"
PLAYURL_URL = "https://api.bilibili.com/x/player/wbi/playurl"
MIXIN_KEY_ENC_TAB = [
    46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49,
    33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40, 61,
    26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11, 36,
    20, 34, 44, 52,
]

# High-confidence ASR corrections for this domain. Only unambiguous technical
# terminology and page-metadata-confirmed proper nouns. Rules are applied
# longest-first so that specific phrases win over their shorter substrings.
TERM_FIXES: list[tuple[str, str]] = [
    # --- proper nouns confirmed by page metadata (owner) and video description ---
    ("穆宇", "木羽"), ("沐宇", "木羽"), ("穆羽", "木羽"), ("沐云", "木羽"), ("穆云", "木羽"),
    ("Semantic", "Semantica"), ("Semantik", "Semantica"),
    ("Gatehub", "GitHub"), ("get hub", "GitHub"),
    ("Pentel", "Palantir"),
    # --- job role ---
    ("FBE", "FDE"), ("fde", "FDE"),
    # --- core technical terms ---
    ("Antology", "Ontology"), ("antology", "ontology"),
    ("Adenture", "Agent"), ("Advent", "Agent"),
    ("Right", "RAG"), ("Rag", "RAG"),
    # --- product / table names misheard as near-homophones ---
    ("Booking War", "Booking表"),
    ("斯达克", "Star"), ("斯达", "Star"),
    ("拍摄框架", "Python框架"),
    # --- phrases with unambiguous same-sound evidence ---
    # Keep this list conservative: only cases where the correct form is certain.
    # Do NOT add "sounds like it should be X" guesses here — the skill contract
    # forbids turning the extractor's assumptions into source facts.
    ("肥腹", "回复"), ("教验", "校验"), ("去虫", "去重"),
    ("圆码", "源码"), ("制定评论", "置顶评论"),
    ("予以检索", "语义检索"), ("图便利", "图遍历"), ("高型项目", "高星项目"),
    ("商手", "上手"), ("编做编学", "边做边学"), ("优会", "优惠"),
    ("全链录", "全链路"), ("旅游规范", "履约规范"), ("散散的", "散乱的"),
    ("新分口", "新兴风口"), ("刷评", "刷屏"), ("点餐", "电商"),
    ("协统", "协同"),
    # --- BV1wVb76bE8e（AI Coding / Ontology / 规格驱动流程）---
    # Each entry was verified against every occurrence in that video's ASR body:
    # same-sound mishearing, or a term the author spells correctly elsewhere.
    ("you the story", "User Story"), ("you的story", "User Story"),
    ("优则story", "User Story"), ("优则4.2", "User Story 4.2"), ("优则", "User Story"),
    ("User Solary", "User Story"),
    ("air coding", "AI coding"), ("air agent", "AI agent"),
    ("workflop", "workflow"),
    ("Spacify", "Specify"), ("spack", "Spec"), ("Spac", "Spec"),
    ("Tasq", "Task"), ("Mapnaum", "Markdown"), ("Skeema", "Schema"),
    ("Given Winston", "Given When Then"),
    ("Jekens", "Jenkins"),
    ("微仓tology", "Ontology"),
    ("大码", "代码"), ("托普", "拓扑"), ("工理", "公理"),
    ("教研", "校验"), ("国际教研", "规则校验"),
    ("测试用力", "测试用例"), ("色彩用力", "测试用例"),
    ("关系技术", "关系基数"), ("供应性需求", "功能性需求"),
    ("移制性", "一致性"), ("自断制", "字段值"), ("自断", "字段"), ("避田", "必填"),
    ("表男", "表单"), ("政客表达", "正则表达"), ("1级几开轴", "以几开头"),
    ("提要不了", "提交不了"), ("门镜", "门禁"), ("拽套", "摘要"),
    ("透布关系", "拓扑关系"), ("详细的秒数", "详细的描述"),
    ("写作", "协作"), ("共同制造", "共同知道"),
    ("呈倾", "澄清"), ("诚庆", "澄清"), ("语异", "语义"), ("语意推你", "语义推理"),
    ("规方", "规范"), ("裸裂", "罗列"), ("接铺", "接口"), ("硬设", "映射"),
    ("闪出量", "产出量"), ("身上环境", "生产环境"), ("归党", "归档"),
    ("撒水池", "洒水车"),
]


def fail(message: str) -> None:
    raise RuntimeError(message)


def run(command: list[str], *, cwd: Path | None = None, timeout: int = 1800) -> str:
    result = subprocess.run(
        command, cwd=cwd, text=True,
        # Children (notably ffmpeg, which polls stdin for interactive keys) must
        # not inherit the caller's stdin: when this script is driven from a
        # shell `while read` loop they would consume the loop's input file.
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        timeout=timeout, check=False,
    )
    if result.returncode:
        fail(f"Command failed ({result.returncode}): {' '.join(command[:4])}\n{result.stdout[-3000:]}")
    return result.stdout


def require_command(name: str) -> str:
    path = shutil.which(name)
    if not path:
        fail(f"Missing dependency: {name}")
    return path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def locate_model(explicit: str | None, curl: str) -> Path:
    candidates = [
        explicit,
        os.environ.get("WHISPER_MODEL"),
        str(Path.home() / ".cache/hyperframes/whisper/models/ggml-small.bin"),
        str(Path.home() / ".cache/douyin-reference-transcript/models/ggml-small.bin"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file() and Path(candidate).stat().st_size > 1_000_000:
            return Path(candidate).resolve()
    fail("No local ggml-small.bin found; pass --model explicitly")


# ---------------------------------------------------------------- Bilibili API

class BiliClient:
    def __init__(self, curl: str, cookie: str | None = None):
        self.curl = curl
        self.cookie = cookie
        self.mixin_key: str | None = None

    def _get(self, url: str, *, timeout: int = 60) -> str:
        cmd = [self.curl, "-s", "-L", "-A", UA, "-e", REFERER]
        if self.cookie:
            cmd += ["-b", self.cookie]
        cmd.append(url)
        out = run(cmd, timeout=timeout)
        return out

    @staticmethod
    def harvest_cookie(curl: str, jar: Path) -> str:
        run([curl, "-s", "-c", str(jar), "-A", UA, "-o", "/dev/null", REFERER], timeout=60)
        pairs = []
        for line in jar.read_text(errors="ignore").splitlines():
            if line.startswith("#") or not line.strip():
                continue
            fields = line.split("\t")
            if len(fields) > 6:
                pairs.append(f"{fields[5].strip()}={fields[6].strip()}")
        # A stable device fingerprint reduces WAF friction on later calls.
        spi = run([curl, "-s", "-A", UA, "-e", REFERER,
                   "https://api.bilibili.com/x/frontend/finger/spi"], timeout=60)
        try:
            data = (json.loads(spi).get("data") or {})
            for key, field in (("buvid3", "b_3"), ("buvid4", "b_4")):
                if data.get(field):
                    pairs.append(f"{key}={data[field]}")
        except json.JSONDecodeError:
            pass
        return "; ".join(pairs)

    def json_get(self, url: str, *, timeout: int = 60) -> dict[str, Any]:
        raw = self._get(url, timeout=timeout)
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            fail(f"Non-JSON API response from {url.split('?')[0]}: {raw[:400]}")
            raise exc

    def wbi_sign(self, params: dict[str, str]) -> str:
        if self.mixin_key is None:
            # NOTE: for anonymous visitors nav returns code -101 ("not logged in")
            # while still serving data.wbi_img. Do not gate on code here.
            nav = self.json_get(NAV_URL)
            wbi = (nav.get("data") or {}).get("wbi_img") or {}
            if not wbi.get("img_url") or not wbi.get("sub_url"):
                fail(f"nav API served no wbi_img: {nav.get('code')} {nav.get('message')}")
            img = wbi["img_url"].rsplit("/", 1)[-1].split(".")[0]
            sub = wbi["sub_url"].rsplit("/", 1)[-1].split(".")[0]
            raw = img + sub
            self.mixin_key = "".join(raw[i] for i in MIXIN_KEY_ENC_TAB)[:32]
        payload = dict(params)
        payload["wts"] = str(int(time.time()))
        query = urllib.parse.urlencode(sorted(payload.items()))
        payload["w_rid"] = hashlib.md5((query + self.mixin_key).encode()).hexdigest()
        return urllib.parse.urlencode(sorted(payload.items()))

    def video_info(self, bvid: str) -> dict[str, Any]:
        data = self.json_get(f"{VIEW_URL}?bvid={bvid}")
        if data.get("code") != 0:
            fail(f"view API failed: {data.get('code')} {data.get('message')}")
        return data["data"]

    def parts(self, bvid: str) -> list[dict[str, Any]]:
        data = self.json_get(f"{PAGELIST_URL}?bvid={bvid}")
        if data.get("code") != 0:
            fail(f"pagelist API failed: {data.get('code')} {data.get('message')}")
        return data["data"]

    def audio_url(self, bvid: str, cid: int) -> tuple[str, int]:
        query = self.wbi_sign(
            {"bvid": bvid, "cid": str(cid), "fnval": "16", "fnver": "0", "fourk": "1"}
        )
        data = self.json_get(f"{PLAYURL_URL}?{query}")
        if data.get("code") != 0:
            fail(f"playurl API failed: {data.get('code')} {data.get('message')}")
        dash = data["data"].get("dash")
        if not dash or not dash.get("audio"):
            fail("No DASH audio stream in playurl response")
        # Lowest bitrate is sufficient for speech ASR and downloads fastest.
        best = min(dash["audio"], key=lambda a: a.get("bandwidth") or 10**9)
        return best["baseUrl"], best.get("bandwidth") or 0


# ---------------------------------------------------------------- transcript

def sanitize_filename(value: str, *, limit: int = 100) -> str:
    value = value.strip()
    value = re.sub(r"_哔哩哔哩_bilibili$", "", value)
    value = re.sub(r"[\\/:：*?？\"<>|｜\x00-\x1f]", "_", value)
    value = re.sub(r"\s+", " ", value).strip(" ._")
    if len(value.encode("utf-8")) > limit * 3:
        value = value[:limit]
    return value or "未命名"


def apply_term_fixes(text: str, log: list[tuple[str, str, int]]) -> str:
    for wrong, right in sorted(TERM_FIXES, key=lambda p: -len(p[0])):
        if not wrong or wrong == right:
            continue
        # Skip no-op rewrites (e.g. a lowercase rule whose uppercase variant was
        # already applied) so the audit log only lists real changes.
        if wrong.lower() == right.lower():
            continue
        count = text.count(wrong)
        if count:
            text = text.replace(wrong, right)
            log.append((wrong, right, count))
    return text


def timestamp_value(value: Any) -> str:
    if isinstance(value, str):
        return value.replace(",", ".")
    return ""


def segment_fields(item: dict[str, Any]) -> tuple[str, str, str]:
    ts = item.get("timestamps") or {}
    start = timestamp_value(ts.get("from") or ts.get("start"))
    end = timestamp_value(ts.get("to") or ts.get("end"))
    return start, end, str(item.get("text") or "").strip()


def seconds(timestamp: str) -> float:
    match = re.search(r"(\d+):(\d+):(\d+)[.,](\d+)", timestamp or "")
    if not match:
        return 0.0
    hours, minutes, secs = (int(p) for p in match.groups()[:3])
    frac = match.group(4)
    return hours * 3600 + minutes * 60 + secs + int(frac) / (10 ** len(frac))


def join_segments(parts: list[str]) -> str:
    result = ""
    for part in parts:
        if result and result[-1].isascii() and result[-1].isalnum() \
                and part[0].isascii() and part[0].isalnum():
            result += " "
        result += part
    return result


def group_segments(items: list[dict[str, Any]]) -> list[tuple[str, str, str]]:
    groups: list[tuple[str, str, str]] = []
    current: list[str] = []
    group_start = group_end = ""
    start_seconds = 0.0
    for item in items:
        start, end, text = segment_fields(item)
        if not text:
            continue
        if not current:
            group_start, start_seconds = start, seconds(start)
        current.append(text)
        group_end = end
        if seconds(end) - start_seconds >= 30 or len(join_segments(current)) >= 420:
            groups.append((group_start, group_end, join_segments(current)))
            current = []
    if current:
        groups.append((group_start, group_end, join_segments(current)))
    return groups


def internal_gaps(items: list[dict[str, Any]], threshold: float = 2.0) -> list[tuple[str, str, float]]:
    gaps: list[tuple[str, str, float]] = []
    previous_end = ""
    for item in items:
        start, end, text = segment_fields(item)
        if not text:
            continue
        if previous_end:
            gap = seconds(start) - seconds(previous_end)
            if gap > threshold:
                gaps.append((previous_end, start, gap))
        previous_end = end
    return gaps


def build_markdown(
    *, title: str, series_title: str, author: str, source_url: str, page_url: str,
    bvid: str, cid: int, part_index: int, part_total: int, part_title: str,
    duration: float, model: Path, transcription: list[dict[str, Any]],
    end_timestamp: str, delta: float, gaps: list[tuple[str, str, float]],
    fixes: list[tuple[str, str, int]],
) -> str:
    groups = group_segments(transcription)
    fix_line = (
        "；".join(f"`{w}` → `{r}`（{c} 处）" for w, r, c in fixes) if fixes else "未做术语替换"
    )
    lines = [
        f"# {title}",
        "",
        "> 资料类型：公开视频口播参考资料。",
        "> 证据状态：页面、来源、bvid/cid、音频与时间覆盖为 `verified`；口播为本地 ASR，属于 `partial`；"
        "视频中的事实主张为 `unknown / 待外部核验`。",
        "",
        "## 使用边界",
        "",
        "本文用于给其他 Agent 或方案讨论提供可追溯信息源。引用时应写成"
        "“视频作者在该时间段主张……”，不得把作者的案例、数字或判断直接写成已证实事实。",
        "",
        "## 来源与提取记录",
        "",
        f"- 系列标题：{series_title}",
        (
            f"- 单P视频：{part_title}"
            if part_total == 1
            else f"- 分P：`P{part_index}/{part_total}` — {part_title}"
        ),        f"- 作者：{author or '页面未可靠提取，待补充'}",
        f"- 原链接：{source_url}",
        f"- 页面 URL：{page_url}",
        f"- bvid：`{bvid}`；cid：`{cid}`",
        f"- 音频时长：`{duration:.3f}` 秒",
        f"- ASR：本地 `whisper.cpp`，模型 `{model.name}`",
        f"- ASR 时间片：`{len(transcription)}`",
        f"- 末段时间：`{end_timestamp}`；与媒体时长差：`{delta:.3f}` 秒",
        "- ASR 内部时间空档（>2秒）：" + (
            "；".join(f"`{s}–{e}`（`{g:.3f}` 秒，可能为静音或漏识，待复核）" for s, e, g in gaps)
            if gaps else "未检出"
        ),
        f"- 术语纠正：{fix_line}",
        "- 整理方式：按原时间顺序机械合并段落，未做观点删减或摘要替换。",
        "",
        "## 完整口播（自动转写参考版）",
        "",
    ]
    for start, end, text in groups:
        lines.extend([f"**[{start}–{end}]** {text}", ""])
    lines.extend([
        "## 校订与核验说明",
        "",
        "- 本文仅对高置信技术术语做了机械替换，未改写句式或观点。",
        "- 英文缩写、人名、企业名、产品名和数字仍可能存在 ASR 误识别；不确定的专有名词应标记 `待外部核验`。",
        "- 正式方案使用前，应对视频中的关键事实主张进行独立外部核验。",
        "",
    ])
    return "\n".join(lines)


# ---------------------------------------------------------------- pipeline

def process_part(
    *, client: BiliClient, bvid: str, part: dict[str, Any], part_total: int,
    series_title: str, author: str, source_url: str, page_url: str,
    output_dir: Path, model: Path, tools: dict[str, str],
    options: argparse.Namespace,
) -> dict[str, Any]:
    page = part["page"]
    cid = part["cid"]
    part_title = str(part.get("part") or f"P{page}")
    # Single-part videos repeat the series title as the part title; do not
    # duplicate it in the document title.
    if part_total == 1 and part_title.strip() == series_title.strip():
        title = series_title
    else:
        title = f"{series_title} - P{page} {part_title}"
    output = output_dir / f"{sanitize_filename(title)}_参考资料.md"

    if output.is_file() and not options.force:
        return {"page": page, "part": part_title, "status": "skipped_existing",
                "output": str(output), "cid": cid}

    audio_url, bandwidth = client.audio_url(bvid, cid)

    with tempfile.TemporaryDirectory(prefix=f"bili-ref-P{page}-") as temp_value:
        temp = Path(temp_value)
        media = temp / "audio.m4s"
        run([
            tools["curl"], "-L", "--fail", "--retry", "3", "--connect-timeout", "20",
            "-A", UA, "-e", REFERER, "-o", str(media), audio_url,
        ], cwd=temp, timeout=600)
        if not media.is_file() or media.stat().st_size < 10_000:
            fail(f"P{page}: downloaded audio is missing or too small")

        duration = float(run([
            tools["ffprobe"], "-v", "error", "-show_entries", "format=duration",
            "-of", "default=nw=1:nk=1", str(media),
        ], cwd=temp).strip())

        wav = temp / "audio.wav"
        run([tools["ffmpeg"], "-y", "-v", "error", "-i", str(media),
             "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", str(wav)], cwd=temp)

        base = temp / "transcript"
        run([tools["whisper"], "-m", str(model), "-l", "zh", "-f", str(wav),
             "-otxt", "-osrt", "-oj", "-ojf", "-of", str(base), "-np",
             "-t", str(options.threads)], cwd=temp)

        data = json.loads(base.with_suffix(".json").read_text(encoding="utf-8"))
        transcription = data.get("transcription") or data.get("segments") or []
        if not transcription:
            fail(f"P{page}: whisper JSON contains no transcription segments")

        end_timestamp = segment_fields(transcription[-1])[1]
        delta = abs(duration - seconds(end_timestamp))
        gaps = internal_gaps(transcription)

        if delta > 2.0:
            fail(f"P{page}: timestamp coverage failed, duration delta is {delta:.3f}s")

        # Correct the transcript segments themselves. Replacing inside the
        # rendered document would also rewrite the correction log line.
        applied: dict[tuple[str, str], int] = {}
        for item in transcription:
            if "text" not in item:
                continue
            local: list[tuple[str, str, int]] = []
            item["text"] = apply_term_fixes(str(item["text"]), local)
            for wrong, right, count in local:
                applied[(wrong, right)] = applied.get((wrong, right), 0) + count
        # Log in the table's own (longest-first) order, with real counts.
        order = {
            pair: index
            for index, pair in enumerate(sorted(TERM_FIXES, key=lambda p: -len(p[0])))
        }
        fixes: list[tuple[str, str, int]] = [
            (wrong, right, applied[(wrong, right)])
            for wrong, right in sorted(applied, key=lambda p: order.get(p, len(order)))
        ]

        markdown = build_markdown(
            title=title, series_title=series_title, author=author,
            source_url=source_url, page_url=page_url, bvid=bvid, cid=cid,
            part_index=page, part_total=part_total, part_title=part_title,
            duration=duration, model=model, transcription=transcription,
            end_timestamp=end_timestamp, delta=delta, gaps=gaps, fixes=fixes,
        )

        output_dir.mkdir(parents=True, exist_ok=True)
        pending = output.with_suffix(output.suffix + ".pending")
        pending.write_text(markdown, encoding="utf-8")
        pending.replace(output)
        if not output.is_file() or output.stat().st_size < 1000:
            fail(f"P{page}: generated Markdown is missing or unexpectedly small")

        result = {
            "page": page, "part": part_title, "status": "verified_with_partial_asr",
            "output": str(output), "cid": cid,
            "api_duration": part.get("duration"),
            "audio_duration": round(duration, 3),
            "audio_bandwidth": bandwidth,
            "segments": len(transcription),
            "chars": len("".join(segment_fields(i)[2] for i in transcription)),
            "duration_delta_seconds": round(delta, 3),
            "internal_gaps_over_2s": [
                {"from": s, "to": e, "seconds": round(g, 3)} for s, e, g in gaps
            ],
            "term_fixes": [{"from": w, "to": r, "count": c} for w, r, c in fixes],
            "document_sha256": sha256_file(output),
            "temporary_media_retained": False,
        }
        return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Bilibili video URL or BV id")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--model", help="whisper.cpp ggml model path")
    parser.add_argument("--only", help="Comma-separated part numbers, e.g. 1,3,5")
    parser.add_argument("--threads", type=int, default=max(4, (os.cpu_count() or 8) - 2))
    parser.add_argument("--force", action="store_true", help="Re-extract existing outputs")
    parser.add_argument(
        "--no-term-fixes", action="store_true",
        help="Emit raw ASR. Use for a different creator: TERM_FIXES entries were "
             "verified only against the videos they were written for.",
    )
    args = parser.parse_args()

    if args.no_term_fixes:
        TERM_FIXES.clear()

    bv_match = re.search(r"(BV[0-9A-Za-z]{10})", args.url)
    if not bv_match:
        fail(f"No BV id found in: {args.url}")
    bvid = bv_match.group(1)

    tools = {
        name: require_command(name)
        for name in ("curl", "ffmpeg", "ffprobe", "whisper-cli")
    }
    tools["whisper"] = tools.pop("whisper-cli")
    model = locate_model(args.model, tools["curl"])

    with tempfile.TemporaryDirectory(prefix="bili-cookie-") as ck:
        cookie = BiliClient.harvest_cookie(tools["curl"], Path(ck) / "jar.txt")
    client = BiliClient(tools["curl"], cookie)

    info = client.video_info(bvid)
    series_title = str(info["title"])
    author = str(info.get("owner", {}).get("name") or "")
    page_url = f"https://www.bilibili.com/video/{bvid}"
    parts = client.parts(bvid)

    wanted = None
    if args.only:
        wanted = {int(x) for x in re.findall(r"\d+", args.only)}

    if not author:
        fail("owner name not found in view API")

    total = len(parts)
    print(f"SERIES={series_title}", flush=True)
    print(f"AUTHOR={author}", flush=True)
    print(f"PARTS={total}", flush=True)
    print(f"MODEL={model}", flush=True)
    print(f"OUTPUT_DIR={args.output_dir.resolve()}", flush=True)

    results: list[dict[str, Any]] = []
    for part in parts:
        if wanted and part["page"] not in wanted:
            continue
        page = part["page"]
        print(f"\n--- P{page}/{total} cid={part['cid']} {part.get('part')} ---", flush=True)
        started = time.time()
        try:
            result = process_part(
                client=client, bvid=bvid, part=part, part_total=total,
                series_title=series_title, author=author, source_url=args.url,
                page_url=page_url, output_dir=args.output_dir, model=model,
                tools=tools, options=args,
            )
        except (RuntimeError, subprocess.CalledProcessError,
                subprocess.TimeoutExpired) as exc:
            result = {"page": page, "part": part.get("part"), "status": "failed",
                      "error": str(exc)[:1500]}
        result["elapsed_seconds"] = round(time.time() - started, 1)
        results.append(result)
        print("RESULT=" + json.dumps(result, ensure_ascii=False), flush=True)

    summary = {
        "bvid": bvid, "series_title": series_title, "author": author,
        "parts_total": total, "output_dir": str(args.output_dir.resolve()),
        "ok": sum(1 for r in results if r["status"] == "verified_with_partial_asr"),
        "skipped": sum(1 for r in results if r["status"] == "skipped_existing"),
        "failed": sum(1 for r in results if r["status"] == "failed"),
        "results": results,
    }
    print("\nSUMMARY_JSON=" + json.dumps(summary, ensure_ascii=False), flush=True)

    summary_path = args.output_dir / "_提取汇总.json"
    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
