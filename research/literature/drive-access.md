# Google Drive Reference Access

## Canonical reference shelf

- Folder ID: `1R7j8xtt1nNXVxFrlutAn9eo5LCpUWn1l`
- URL: https://drive.google.com/drive/folders/1R7j8xtt1nNXVxFrlutAn9eo5LCpUWn1l
- Verified: 2026-07-18 through the connected Google Drive interface.
- Verification scope: direct child metadata listing succeeded. Sharing/permission policy was not audited.

The listing includes subject folders such as `Provability logic`, `Proof theory`, `Algebraic logic`, `Category theory`, `Categorical logic`, `Domain theory`, `Incompleteness Theorem`, `Set theory`, `Type theory`, `Universal Algebra`, and research-meeting folders, together with top-level PDFs.

## Record contract

When a Drive item becomes research-relevant, record:

- `drive_file_id` as the stable identity key;
- the observed title and MIME type;
- the direct Drive URL;
- `access_checked_at`;
- the linked Goal/problem;
- whether only metadata or the full text was actually read.

Do not infer that a PDF is citable merely because its metadata is visible. Do not duplicate the full reference shelf into Git. Store a research note and stable link; keep licensed or private originals in Drive.

## Agent access procedure

1. Start from the canonical folder above or a known `fileId`.
2. Narrow to a subject folder before broad search.
3. Read metadata before export/download so the MIME type and identity are known.
4. Update the local literature card with the observed ID/URL; never synthesize a Drive URL.

