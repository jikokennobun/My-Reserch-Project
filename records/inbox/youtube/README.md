# YouTube Inbox

YouTube watch activity and transcript captures are local source material for
daily reports. Raw JSONL, transcript text, and subtitle files are ignored by
Git because they can contain copyrighted or private working material.

Use `code/scripts/import-youtube-activity.ps1` to queue a video URL, optional
notes, and optional transcript metadata for the daily-report pass.

