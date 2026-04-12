# Refresh Participant Research Log Updates

Re-read every participant Google Doc research log listed in
`.participant-logs-allowlist`, identify what has changed since the last run,
and update two facilitator-facing markdown files under
`data/output/participant_updates/`.

This skill is the `tais_04_2026` branch analogue of the global
`refresh-project-context-from-gdocs` skill, re-targeted at participant
research logs instead of team project-context docs.

## Inputs

- `.participant-logs-allowlist` at the repo root — required. Each
  non-comment line is `<participant_key>  <google-doc-url>`. The
  participant_key must match a file in `config/participants/<key>.yaml`.
- Optional argument: a single participant_key. When present, the skill
  only refreshes that participant's doc and leaves the rest of
  `log.md` / `review_queue.md` untouched.

If the allowlist file does not exist, or exists but contains no
non-comment entries, stop and tell the user — do not invent participants.

## Preconditions

- The `gdoc` CLI must be installed and authenticated. If any `gdoc`
  invocation returns an auth error, stop and tell the user to run
  `gdoc auth`, then re-run the skill.
- **READ-ONLY gdoc usage.** Only these subcommands are allowed:
  `gdoc cat`, `gdoc info`, `gdoc tabs`, `gdoc comments`, `gdoc comment`.
  Never call `gdoc edit`, `gdoc write`, `gdoc new`, `gdoc cp`,
  `gdoc reply`, `gdoc resolve`, `gdoc reopen`, `gdoc delete-comment`,
  `gdoc share`, or any other write subcommand. (See the global
  `gdoc-reader` skill for the full CLI surface.)

## Change detection — use gdoc's awareness system, not your own

The `gdoc` CLI tracks per-document state under
`~/.config/gdoc/state/<DOC_ID>.json` and prints an awareness banner to
**stderr** before most commands:

- First time touching a doc:
  `--- first interaction with this doc ---`
- No changes since last run:
  `--- no changes ---`
- Changes since last run:
  `--- since last interaction (12 min ago) ---` with lines like
  `✎ doc edited by <user> (v4 → v6)`,
  `💬 new comment #<id> by <user>: "..."`,
  `✓ comment #<id> resolved by <user>`.

**Do not build your own snapshot/hash layer.** Run `gdoc` commands
normally and capture stderr alongside stdout. The banner is the source
of truth for what has changed.

## Procedure

For each `(participant_key, doc_url)` in the allowlist (or just the
requested participant_key if one was passed):

### 1. Metadata

Extract `DOC_ID` from the URL. Run:

```bash
gdoc info <DOC_ID> --json
```

Capture title, owner, and modifiedTime.

### 2. Read the doc

Run, capturing **both stdout and stderr**:

```bash
gdoc cat <DOC_ID> --all-tabs
```

`--all-tabs` is mandatory — participants may add new tabs over time and
any tab not read will silently disappear from the report.

### 3. Interpret the awareness banner

Parse the stderr banner into one of three states:

- **first interaction** — treat every dated entry in the log as new,
  and write a "baselined" line in the chat summary.
- **no changes** — if the participant already has a section in
  `log.md`, record "no changes since <modifiedTime>" in the chat
  summary and skip to the next participant. **However**, if the
  participant has no section in `log.md` yet, treat them as "first
  interaction" (read the full doc, baseline all entries) regardless
  of the gdoc banner — the banner tracks gdoc CLI state, not skill
  output state, so "no changes" only means "nothing to log" when the
  skill has already baselined the participant.
- **since last interaction** — extract the `v<old> → v<new>` version
  bump and any `new comment` / `resolved comment` lines. These feed
  step 5 (review queue population).

### 4. Open comments

Run:

```bash
gdoc comments <DOC_ID>
```

List unresolved comments. Each open comment is a candidate review item
for step 6.

### 5. Identify new entries

Research logs are expected to be organized chronologically with dated
entries (e.g., `## 2026-04-10` or `### Apr 10, 2026`). From the stdout
content:

- Find the most recent date already present for this participant in
  `data/output/participant_updates/log.md`, if the file and section
  exist.
- Keep only entries strictly newer than that date as "new entries".
- For first-interaction docs, keep all dated entries.
- If the participant's log is not dated, fall back to: the entire
  content of any tab whose name contains a date newer than the most
  recent already-logged date, or the raw `v<old> → v<new>` diff hint
  from the banner when no dates can be recovered.

For each new entry, produce a **one-line pointer** (≤120 chars). A
pointer names the topic and gestures at the shape of the change — it
is not a summary and not a restatement. Example:
`2026-04-10 — switched from GPT-2 to Pythia-70M; rerunning probe ablation`.

### 6. Build deep links

Construct the best available anchor for each new entry, in this order
of preference:

1. If the entry lives in a non-default tab, append `?tab=t.<tab_id>`
   from the `gdoc cat --all-tabs` tab markers or `gdoc tabs <DOC_ID>`.
2. If a heading anchor is available from `gdoc cat --annotated` for
   that entry, append `#heading=h.<heading_id>`.
3. Otherwise, fall back to the bare doc URL.

## Output file 1 — `data/output/participant_updates/log.md` (cumulative)

Structure:

```markdown
# Participant research log updates

Last refreshed: YYYY-MM-DD HH:MM

## <participant_key> — <doc title>
Doc: <url> · Owner: <owner> · Last modified: <date>

- YYYY-MM-DD — <one-line pointer> ([link](<deep-link>))
- YYYY-MM-DD — <one-line pointer> ([link](<deep-link>))
```

Rules:

- Per-participant entries sorted by date **descending** (newest first).
- **Merge, never overwrite.** If `log.md` already exists, preserve
  every existing entry and insert new entries at the top of the
  correct participant's section.
- If a participant has no section yet, append a new section at the end
  of the file.
- Update the `Last refreshed` line at the top.
- Do not rewrite historical entries — only add new ones. If a
  participant edited a past entry, log the *edit* as its own new line
  (e.g., `2026-04-10 — edited Apr 3 entry: corrected probe dimensions`)
  rather than mutating the old line.

## Output file 2 — `data/output/participant_updates/review_queue.md` (ephemeral)

Structure:

```markdown
# Facilitator review queue

Generated: YYYY-MM-DD HH:MM

The facilitator deletes items from this file as they are handled.
Unhandled items from prior runs are preserved. This skill NEVER
removes items — only the facilitator does.

## <participant_key>

- [ ] YYYY-MM-DD — <what needs reviewing> ([link](<deep-link>))
  Why: <one-line reason>
```

Populate with any of these, only when newly surfaced by this run:

- A new dated entry containing a direct question, an `@facilitator`
  mention, a blocker, or a proposal that needs a go / no-go decision.
- An open comment from step 4 that is not yet represented in
  `review_queue.md`.
- An inactivity flag: the participant's `modifiedTime` is older than
  14 days. Use `Why: inactive for N days` and link to the doc root.

**Merge rules — do not clobber.** If `review_queue.md` already exists:

- Read the current file.
- Preserve every existing checkbox item verbatim, even checked ones
  the facilitator hasn't deleted yet — the facilitator's model is
  "delete when done", not "check when done".
- Append new items under the right participant section. If the
  participant has no section, create one.
- Never re-add an item the skill surfaced in a previous run: match on
  `<date> — <text>` to dedupe. This is what lets the facilitator
  safely delete items.
- Update the `Generated` line at the top.

This file may be safely deleted by the facilitator at any time. When
that happens, the next run will start a fresh file containing only
items from that run's new changes.

## Final chat summary

After writing both files, print a short per-participant summary:

```
guido     — 3 new entries, 1 review item added
ivan      — no changes
lucia     — first interaction, baselined 7 entries
mateo     — inactive for 18 days (flagged for review)
```

Followed by the paths of the two output files so the facilitator can
open them directly.

## CRITICAL RULES

- **Read-only on Google Docs.** Only `gdoc cat`, `info`, `tabs`,
  `comments`, `comment` are allowed. No writes, no resolves, no
  deletes.
- **Always `--all-tabs` on `gdoc cat`.** New tabs can appear without
  warning.
- **Never clobber `log.md` or `review_queue.md`.** Always merge.
  Existing entries stay; the facilitator is the only one who removes
  review items. (See `feedback_no_overwrite_shared_output.md` in
  user memory — same principle.)
- **Never invent participants.** The allowlist is authoritative. If
  a participant_key in the allowlist has no matching
  `config/participants/<key>.yaml`, warn in the chat summary but
  still process the doc.
- **Do not summarize research content.** Pointers only. The report
  tells the facilitator *where to look*, not *what the content means*.
- **No novelty or idea evaluation here.** This skill only surfaces
  changes. Idea evaluation still goes through `/evaluate-idea` and
  the existing `idea_tracker.md` workflow.
