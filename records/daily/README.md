# Daily Reports

Daily reports generated from Discord captures, Obsidian research indexes, and
repository changes should be stored here as `YYYY-MM-DD.md`.

The generator follows the user's Obsidian daily template. The stable contract is:

- top metadata lines for `日付`, `起床`, `就寝（予想）`, and `天気`
- `#天気の移り変わり` when weather capture is available
- `#活動まとめ` as Japanese prose, not bullets
- `#食事`
- `#Obsidianメモ変更履歴`
- `#やった`
- `#思った`
- `#視聴ログ抜粋` as Japanese prose
- `#読んだ/見た/知った`
- `#SNSでの活動`
- `#生成AIでの活動`
- `#精神状態` with `朝`, `昼`, and `夜`; missing mood logs are filled with
  clearly labelled automatic estimates
- `###### 今日の感想` as Japanese prose, not bullets
- `## Discord Digest`

The report should not copy a separate life-log `振り返り` channel into the body.
Reflection belongs in the daily report prose itself.

Raw source packets and health reports are generated separately under
`records/inbox/`, `records/health/`, and `records/logs/automation-runs/`.
