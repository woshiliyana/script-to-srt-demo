"""Compare where each paragraph starts in voiceover.mp3 with the first subtitle line
of that paragraph in output.srt. Standard library only: python3 check_timing.py"""
import json, re

def parse_srt(path):
    cues = []
    for block in open(path, encoding="utf-8").read().strip().split("\n\n"):
        lines = block.splitlines()
        h, m, s, ms = map(int, re.match(r"(\d+):(\d+):(\d+),(\d+)", lines[1]).groups())
        cues.append((h * 3600 + m * 60 + s + ms / 1000, " ".join(lines[2:])))
    return cues

cues = parse_srt("output.srt")
worst = 0.0
for p in json.load(open("paragraph-starts.json")):
    start, text = next((c for c in cues if c[1].startswith(p["first_words"][:20])), (None, None))
    diff = start - p["starts_at_seconds"]
    worst = max(worst, abs(diff))
    print(f"paragraph {p['paragraph']}: audio {p['starts_at_seconds']:6.2f}s  subtitle {start:6.2f}s  diff {diff:+.2f}s")
print(f"largest difference: {worst:.2f}s")
