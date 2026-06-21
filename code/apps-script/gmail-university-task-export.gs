/**
 * Gmail -> Drive task export for Codex/Obsidian.
 *
 * Setup:
 * 1. Create Gmail labels:
 *    - Codex/大学タスク
 *    - Codex/塾講師タスク
 *    - Codex/取込済み
 * 2. Paste this file into script.google.com.
 * 3. Run exportUniversityTasks once, approve Gmail/Drive permissions.
 * 4. Add a time trigger, e.g. every morning.
 *
 * The script exports messages carrying the task labels below, and can
 * optionally auto-label recent messages involving configured addresses.
 */
const SOURCE_LABEL_NAME = 'Codex/大学タスク';
const TUTORING_LABEL_NAME = 'Codex/塾講師タスク';
const PROCESSED_LABEL_NAME = 'Codex/取込済み';
const DRIVE_FOLDER_NAME = 'Codex Gmail Task Export';
const UNIVERSITY_ADDRESSES = [
  'shibuya.i.aa@m.titech.ac.jp',
  'shibuya.i.9f75@m.isct.ac.jp',
  'shibuyaiori2004+univ@gmail.com'
];
const TUTORING_ADDRESSES = [
  'shibuyaiori2004@gmail.com'
];
const AUTO_LABEL_UNIVERSITY_ADDRESS_MAIL = true;
const AUTO_LABEL_TUTORING_ADDRESS_MAIL = true;
const EXPORT_INBOX_MESSAGES_ONLY = true;
const DAYS_BACK = 45;
const MARK_PROCESSED = false;
const MAX_THREADS = 100;
const TEST_UNIVERSITY_RECIPIENTS = [
  'shibuya.i.aa@m.titech.ac.jp',
  'shibuya.i.9f75@m.isct.ac.jp'
];
const UNIVERSITY_FORWARDING_TEST_ADDRESSES = [
  'shibuyaiori2004+univ@gmail.com'
];
const UNIVERSITY_FORWARDING_TEST_DAYS_BACK = 7;
const UNIVERSITY_FORWARDING_TEST_MAX_THREADS = 20;
const IGNORE_FROM_PATTERNS = [
  /no-reply@accounts\.google\.com/i,
  /mail@tnews\.jp/i,
  /donotreply@indeed\.com/i,
  /noreply@.*indeed/i,
  /townwork|baitoru|mynavi|rikunabi/i
];
const IGNORE_TEXT_PATTERNS = [
  /セキュリティ通知|security alert|new sign-in|ログイン/i,
  /メールマガジン|本日のPick Up|おすすめ塾|求人|採用|応募|スカウト|新着|Indeed|勤務形態|福利厚生|公式オンラインストア|放課後学習サポート/i,
  /^\s*\[TEST\]/i,
  /Codex\/Obsidian automation test mail|実際の課題・締切・提出依頼ではありません/i
];

function exportUniversityTasks() {
  const sourceLabel = getOrCreateLabel_(SOURCE_LABEL_NAME);
  const tutoringLabel = getOrCreateLabel_(TUTORING_LABEL_NAME);
  const processedLabel = getOrCreateLabel_(PROCESSED_LABEL_NAME);
  const folder = getOrCreateFolder_(DRIVE_FOLDER_NAME);
  const today = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'yyyy-MM-dd');
  const query = buildQuerySummary_();
  const threads = collectTargetThreads_(sourceLabel, tutoringLabel, processedLabel);
  const records = [];

  threads.forEach(thread => {
    const threadKind = getThreadKind_(thread);
    thread.getMessages().forEach(message => {
      if (EXPORT_INBOX_MESSAGES_ONLY && !message.isInInbox()) {
        return;
      }

      const plainBody = normalizeText_(message.getPlainBody()).slice(0, 6000);
      const subject = normalizeText_(message.getSubject());
      const from = normalizeText_(message.getFrom());
      const to = normalizeText_(message.getTo());
      const cc = normalizeText_(message.getCc());
      const receivedAt = message.getDate();
      const taskHints = extractTaskHints_(subject + '\n' + plainBody);
      const matchedUniversityAddresses = findMatchedUniversityAddresses_([from, to, cc].join('\n'));
      const matchedTutoringAddresses = findMatchedTutoringAddresses_([from, to, cc].join('\n'));
      const kind = matchedTutoringAddresses.length > 0 ? 'tutoring' :
        (matchedUniversityAddresses.length > 0 ? 'university' : threadKind);
      const label = kind === 'tutoring' ? TUTORING_LABEL_NAME : SOURCE_LABEL_NAME;

      if (shouldIgnoreMessage_(from, subject + '\n' + plainBody)) {
        return;
      }

      if (taskHints.length === 0 && !looksActionable_(subject + '\n' + plainBody)) {
        return;
      }

      records.push({
        exported_at: new Date().toISOString(),
        received_at: receivedAt.toISOString(),
        date: Utilities.formatDate(receivedAt, Session.getScriptTimeZone(), 'yyyy-MM-dd'),
        source: 'gmail',
        kind,
        label,
        thread_id: thread.getId(),
        message_id: message.getId(),
        from,
        to,
        cc,
        matched_university_addresses: matchedUniversityAddresses,
        matched_tutoring_addresses: matchedTutoringAddresses,
        subject,
        task_hints: taskHints,
        snippet: plainBody.slice(0, 1000),
        body_excerpt: plainBody
      });
    });

    if (MARK_PROCESSED) {
      thread.addLabel(processedLabel);
      thread.removeLabel(sourceLabel);
      thread.removeLabel(tutoringLabel);
    }
  });

  const payload = JSON.stringify({
    exported_at: new Date().toISOString(),
    labels: [SOURCE_LABEL_NAME, TUTORING_LABEL_NAME],
    query,
    count: records.length,
    records
  }, null, 2);

  const fileName = `mail-tasks-${today}.json`;
  const existing = folder.getFilesByName(fileName);
  while (existing.hasNext()) {
    existing.next().setTrashed(true);
  }
  folder.createFile(fileName, payload, 'application/json');
  Logger.log(`Exported ${records.length} mail task record(s) to ${fileName}.`);
}

function collectTargetThreads_(sourceLabel, tutoringLabel, processedLabel) {
  const threads = [];
  const seen = {};

  const addThread = thread => {
    const id = thread.getId();
    if (seen[id]) return;
    seen[id] = true;
    threads.push(thread);
  };

  GmailApp
    .search(`label:"${SOURCE_LABEL_NAME}" newer_than:${DAYS_BACK}d -label:"${PROCESSED_LABEL_NAME}"`, 0, MAX_THREADS)
    .forEach(addThread);

  GmailApp
    .search(`label:"${TUTORING_LABEL_NAME}" newer_than:${DAYS_BACK}d -label:"${PROCESSED_LABEL_NAME}"`, 0, MAX_THREADS)
    .forEach(addThread);

  if (AUTO_LABEL_UNIVERSITY_ADDRESS_MAIL) {
    const addressQuery = buildUniversityAddressQuery_();
    if (addressQuery) {
      GmailApp
        .search(`in:inbox ${addressQuery} newer_than:${DAYS_BACK}d -label:"${PROCESSED_LABEL_NAME}"`, 0, MAX_THREADS)
        .forEach(thread => {
          thread.addLabel(sourceLabel);
          addThread(thread);
        });
    }
  }

  if (AUTO_LABEL_TUTORING_ADDRESS_MAIL) {
    const addressQuery = buildTutoringAddressQuery_();
    if (addressQuery) {
      GmailApp
        .search(`in:inbox ${addressQuery} newer_than:${DAYS_BACK}d -label:"${PROCESSED_LABEL_NAME}"`, 0, MAX_THREADS)
        .forEach(thread => {
          thread.addLabel(tutoringLabel);
          addThread(thread);
        });
    }
  }

  return threads;
}

function buildUniversityAddressQuery_() {
  const terms = [];
  UNIVERSITY_ADDRESSES.forEach(address => {
    terms.push(`from:${address}`);
    terms.push(`to:${address}`);
    terms.push(`cc:${address}`);
    terms.push(`deliveredto:${address}`);
  });
  if (terms.length === 0) return '';
  return `{${terms.join(' ')}}`;
}

function buildTutoringAddressQuery_() {
  const terms = [];
  TUTORING_ADDRESSES.forEach(address => {
    terms.push(`from:${address}`);
    terms.push(`to:${address}`);
    terms.push(`cc:${address}`);
    terms.push(`deliveredto:${address}`);
  });
  if (terms.length === 0) return '';
  return `{${terms.join(' ')}}`;
}

function buildAddressQuery_(addresses) {
  const terms = [];
  addresses.forEach(address => {
    terms.push(`to:${address}`);
    terms.push(`cc:${address}`);
    terms.push(`deliveredto:${address}`);
  });
  if (terms.length === 0) return '';
  return `{${terms.join(' ')}}`;
}

function buildQuerySummary_() {
  const parts = [`label:"${SOURCE_LABEL_NAME}"`, `label:"${TUTORING_LABEL_NAME}"`];
  const addressQuery = buildUniversityAddressQuery_();
  if (AUTO_LABEL_UNIVERSITY_ADDRESS_MAIL && addressQuery) {
    parts.push(addressQuery);
  }
  const tutoringQuery = buildTutoringAddressQuery_();
  if (AUTO_LABEL_TUTORING_ADDRESS_MAIL && tutoringQuery) {
    parts.push(tutoringQuery);
  }
  return `${parts.join(' OR ')} newer_than:${DAYS_BACK}d -label:"${PROCESSED_LABEL_NAME}"`;
}

function sendUniversityForwardingTestMail() {
  const now = new Date();
  const stamp = Utilities.formatDate(now, Session.getScriptTimeZone(), 'yyyy-MM-dd HH:mm:ss');
  const token = Utilities.getUuid().slice(0, 8);
  const subject = `[Codex Test] 大学メール転送確認 ${stamp}`;
  const body = [
    'Codex/Obsidian automation test mail.',
    `token: ${token}`,
    `sent_at: ${stamp}`,
    '',
    'このメールは、大学メールから個人Gmailへの転送とCodex日報連携を確認するためのテストです。',
    '確認してください。',
    '実際の課題・締切・提出依頼ではありません。'
  ].join('\n');

  GmailApp.sendEmail(
    TEST_UNIVERSITY_RECIPIENTS.join(','),
    subject,
    body,
    { name: 'Codex Gmail Task Export Test' }
  );
  Logger.log(`Sent university forwarding test mail to ${TEST_UNIVERSITY_RECIPIENTS.join(', ')}; token=${token}`);
}

function exportUniversityForwardingTest() {
  const folder = getOrCreateFolder_(DRIVE_FOLDER_NAME);
  const today = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'yyyy-MM-dd');
  const addressQuery = buildAddressQuery_(UNIVERSITY_FORWARDING_TEST_ADDRESSES);
  if (!addressQuery) {
    throw new Error('UNIVERSITY_FORWARDING_TEST_ADDRESSES is empty.');
  }

  const query = `in:inbox ${addressQuery} newer_than:${UNIVERSITY_FORWARDING_TEST_DAYS_BACK}d`;
  const records = [];
  GmailApp.search(query, 0, UNIVERSITY_FORWARDING_TEST_MAX_THREADS).forEach(thread => {
    thread.getMessages().forEach(message => {
      if (!message.isInInbox()) return;

      const plainBody = normalizeText_(message.getPlainBody()).slice(0, 6000);
      const subject = normalizeText_(message.getSubject());
      const from = normalizeText_(message.getFrom());
      const to = normalizeText_(message.getTo());
      const cc = normalizeText_(message.getCc());
      const receivedAt = message.getDate();

      records.push({
        exported_at: new Date().toISOString(),
        received_at: receivedAt.toISOString(),
        date: Utilities.formatDate(receivedAt, Session.getScriptTimeZone(), 'yyyy-MM-dd'),
        source: 'gmail',
        kind: 'university',
        label: SOURCE_LABEL_NAME,
        thread_id: thread.getId(),
        message_id: message.getId(),
        from,
        to,
        cc,
        matched_university_addresses: findMatchedUniversityAddresses_([from, to, cc].join('\n')),
        matched_tutoring_addresses: [],
        subject,
        task_hints: extractTaskHints_(subject + '\n' + plainBody),
        snippet: plainBody.slice(0, 1000),
        body_excerpt: plainBody
      });
    });
  });

  const payload = JSON.stringify({
    exported_at: new Date().toISOString(),
    labels: [SOURCE_LABEL_NAME],
    query,
    count: records.length,
    records
  }, null, 2);

  const fileName = `mail-univ-forwarding-test-${today}.json`;
  const existing = folder.getFilesByName(fileName);
  while (existing.hasNext()) {
    existing.next().setTrashed(true);
  }
  folder.createFile(fileName, payload, 'application/json');
  Logger.log(`Exported ${records.length} forwarded university mail record(s) to ${fileName}.`);
}

function getThreadKind_(thread) {
  const labelNames = thread.getLabels().map(label => label.getName());
  if (labelNames.indexOf(TUTORING_LABEL_NAME) !== -1) return 'tutoring';
  if (labelNames.indexOf(SOURCE_LABEL_NAME) !== -1) return 'university';
  return 'mail';
}

function findMatchedUniversityAddresses_(text) {
  const lower = String(text || '').toLowerCase();
  return UNIVERSITY_ADDRESSES.filter(address => lower.indexOf(address.toLowerCase()) !== -1);
}

function findMatchedTutoringAddresses_(text) {
  const lower = String(text || '').toLowerCase();
  return TUTORING_ADDRESSES.filter(address => lower.indexOf(address.toLowerCase()) !== -1);
}

function getOrCreateLabel_(name) {
  return GmailApp.getUserLabelByName(name) || GmailApp.createLabel(name);
}

function getOrCreateFolder_(name) {
  const folders = DriveApp.getFoldersByName(name);
  if (folders.hasNext()) return folders.next();
  return DriveApp.createFolder(name);
}

function normalizeText_(value) {
  return String(value || '').replace(/\s+/g, ' ').trim();
}

function looksActionable_(text) {
  return /締切|期限|提出|申請|登録|回答|返信|確認|予約|面談|授業|休講|補講|奨学金|授業料|履修|成績|レポート|課題|deadline|submit|application|register|reply|confirm/i.test(text);
}

function shouldIgnoreMessage_(from, text) {
  const fromText = String(from || '');
  const bodyText = String(text || '');
  const hardIgnoredText = [
    /^\s*\[TEST\]/i,
    /Codex\/Obsidian automation test mail|実際の課題・締切・提出依頼ではありません/i
  ].some(pattern => pattern.test(bodyText));
  if (hardIgnoredText) return true;

  const ignoredSender = IGNORE_FROM_PATTERNS.some(pattern => pattern.test(fromText));
  if (!ignoredSender) return false;
  return IGNORE_TEXT_PATTERNS.some(pattern => pattern.test(bodyText));
}

function extractTaskHints_(text) {
  const hints = [];
  const normalized = normalizeText_(text);
  const patterns = [
    /(締切|期限|提出期限|回答期限|申請期限)[：:\s]*([^。．\n]{0,80})/g,
    /([0-9]{4}[\/\-年][0-9]{1,2}[\/\-月][0-9]{1,2}日?[^。．\n]{0,80})/g,
    /([0-9]{1,2}月[0-9]{1,2}日[^。．\n]{0,80})/g,
    /(提出|申請|登録|回答|返信|確認|予約|出席|支払|振込|受講)[^。．\n]{0,80}/g
  ];

  patterns.forEach(pattern => {
    let match;
    while ((match = pattern.exec(normalized)) !== null) {
      const hint = normalizeText_(match[0]);
      if (hint && hints.indexOf(hint) === -1) {
        hints.push(hint);
      }
    }
  });

  return hints.slice(0, 8);
}


