# Script + MP3 to SRT: a reproducible test

This repository holds everything from one real run of turning a finished script and its voiceover into a timed SRT file, so anyone can check the result instead of taking my word for it.

> Disclosure: I'm the founder of [TimedSubs](https://timedsubs.com), the tool used for this run. The run was done on the live product on November 8, 2026. The voiceover is AI text-to-speech.

## Files

| File | What it is |
| --- | --- |
| `script.txt` | The input script: 141 English words in seven paragraphs |
| `voiceover.mp3` | The input voiceover: 66 seconds, the same words read by a TTS voice |
| `output.srt` | The SRT that TimedSubs produced from those two files, unedited (12 lines) |
| `paragraph-starts.json` | Where each paragraph begins in `voiceover.mp3`, known exactly because the audio was generated one paragraph at a time and joined with 0.6-second gaps |
| `check_timing.py` | Compares each paragraph's start in the audio with the first subtitle line of that paragraph (Python standard library only) |

## Result

```
python3 check_timing.py
```

prints one line per paragraph. In this run every paragraph's first subtitle started between 0.00 and 0.29 seconds after the paragraph begins in the audio, which is about the silence a TTS clip has before its first word.

Other numbers from the run:

- Cost: 2 Timing Minutes (a 66-second file rounds up to two minutes).
- Time: about 46 seconds from confirming to finished subtitles.
- Wording: every subtitle line uses the script text exactly; nothing was re-transcribed.

## Limits

- This is one short, clean TTS recording. Real voices with breaths, overlaps, music, or ad-libs are harder, and this test does not prove anything about them.
- The method needs the final script. If the speaker improvised, transcription is the right tool, not alignment.
- Line length follows your sentences: line 2 stays on screen for about eight seconds because it is one long sentence.

## Reproduce it

1. Open [Script to Subtitles](https://timedsubs.com/en/tools/script-to-subtitles) and sign in (15 free minutes, no card).
2. Paste `script.txt`, upload `voiceover.mp3`, confirm, and download the SRT.
3. Replace `output.srt` with your download and run `python3 check_timing.py`.

A walkthrough with screenshots: [Script and MP3 to SRT: one real run, with the numbers](https://timedsubs.com/en/blog/script-and-mp3-to-srt-real-run).

## License

Script, voiceover, SRT and code in this repository: CC BY 4.0.
