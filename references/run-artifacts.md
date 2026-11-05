# Run artifacts and team sharing

Use this guide at run setup, during evidence capture, and at delivery. Artifact creation is part of normal local QA and needs no setup questionnaire. The [report contract](report-contract.md) governs findings and verdicts.

## Location and lifecycle

Default to the **target project's/worktree's** `.tmp/branch-breaker/<run-id>/`, never the global skill installation. Use a UTC timestamp plus a random suffix for uniqueness; an optional short tested SHA is useful, but do not interpolate raw branch names into paths. Honor an explicitly requested output path instead. Create a new directory without overwriting an existing run; never clean earlier runs automatically.

Check existing path components before writing. Do not follow a `.tmp`, `branch-breaker`, or run-directory symlink into another location, or replace a conflicting file. If the requested/default location is unsafe or unwritable, use a fresh safe OS temporary directory and disclose the actual location and unmet requested/default location. Continue useful QA; if no location is writable, deliver the report or plan in chat and state that file artifacts could not be created.

Record source status/fingerprints before creating the directory. Generated files are run output, not implementation changes: exclude only the exact paths created for this run from source comparisons, and disclose generated untracked files separately. Never ignore all `.tmp` changes, alter `.gitignore`/project configuration, stage artifacts, or commit them by default. For execution runs, begin `report.md` with **IN PROGRESS — validation not complete**, append observations during execution, and finalize it with the evidence-based verdict. If execution stops before required checks finish, do not retain a completed-pass claim; preserve already confirmed failures and the unfinished coverage. Artifact-generation failures are reported separately from the product verdict. Explicitly plan-only requests follow the `plan.md` exception below.

## Execution-run bundle

```text
.tmp/branch-breaker/<run-id>/
  report.md                 # Full technical report with evidence links
  evidence/                 # Sanitized responses, logs, reproductions as needed
  share/
    summary.md              # Portable good/bad/gaps summary with embedded images
    slack.txt               # Concise message ready to copy
    jira.txt                # Structured issue-description/comment draft
    evidence-index.md       # Attachment inventory, provenance, missing captures
    screenshots/            # Actual reviewed captures, only when available
  share.zip                 # Reviewed share/ contents, when archive tooling exists
```

Do not create fake screenshots or empty evidence files to fill this layout. Keep one reviewed screenshot copy in `share/screenshots/`; link to it from the full report with a relative path. Keep supporting local evidence under `evidence/`, and include relevant sanitized excerpts in the sharing summary so teammates do not need your local filesystem. For plan-only requests, write `plan.md` labeled **PLAN ONLY — validation not run by request**, with proposed checks and prerequisites; do not create execution summaries, capture screenshots, or assign an execution verdict. If the user requests no files, deliver the plan in chat without creating a run directory.

The report and all sharing drafts must agree on run ID, tested revision/build, dirty/unpushed scope, verdict, finding IDs/severities, and coverage limits. Describe:

- **What worked:** meaningful behavior actually observed, the checked contract, platform/state, and supporting evidence. Examples include a completed happy path, preserved data after reload, or a rejected invalid write with no side effects. If nothing was verified, say so; do not manufacture positives or equate green unit tests with complete UI coverage.
- **What failed:** confirmed findings with user impact, severity, attribution, concise reproduction, expected/actual result, and evidence. When none were observed, say that within the tested scope. Keep UX opportunities, hypotheses, and gaps separate.
- **What remains uncertain:** blocked/not-run checks, unsupported devices, missing screenshots, and the next useful action. Successful checks must not dilute a FAIL or hide incomplete coverage.

## Capture screenshots during the run

For exercised web/mobile UI, capture representative successful states and each material UI/visual failure when the tools permit it. Include before/action/after states when one frame cannot explain the issue. Use actual browser/device screenshots from the tested build, captured close to the observation. Never generate an illustrative mockup or silently reuse another run's image as evidence. API-only runs should use real response/log excerpts and explain that screenshots are not applicable.

Give each image a stable ID and descriptive filename, such as `BB-001-after-rejected-save.png` or `PASS-001-saved-detail.png`. In `share/evidence-index.md`, record relative filename, linked finding/check ID, capture time, revision/build, platform/device/viewport, state/step, caption, and any redaction. Record supplied/user-captured evidence as such. Do not invent unknown capture metadata. A screenshot shows a visible state; pair it with action logs, requests, or durable reads for claims about persistence, authorization, or recovery.

Prefer synthetic fixtures and safe recapture. Inspect image pixels as well as filenames, URLs, logs, and text for credentials, auth state, private customer/personal data, and unrelated content. Mark redactions explicitly and preserve the relevant failure; if an asset cannot be safely shared, omit it and state why. Do not put unsafe raw captures, browser profiles, cookies, HAR files, or unreviewed traces in `share/` or its archive. Missing screenshot capability is an artifact limitation; it is a test-coverage gap only when the underlying required visual/interaction assertion also could not be established.

## Prepare portable Slack/Jira drafts

`share/summary.md` is the portable entry point: feature/run identity, verdict and impact, what worked, what failed, gaps, material UX concerns, focused reproductions/fix direction, and captioned relative image links. Keep enough evidence inline for the report to be useful without private local logs. Use repository-relative source paths rather than workstation home paths in shareable text; include real remote links only when verified and appropriate for the intended audience.

`share/slack.txt` is a short plain-text message: feature/branch and tested SHA, verdict, key successes, prioritized findings with IDs/severities, gaps, and attachment filenames. `share/jira.txt` includes a proposed title plus environment/revision, what worked, confirmed findings with numbered reproduction steps and expected/actual outcomes, gaps, and attachments. It can be copied into a description or comment; it does not create an issue or map severity to a project's Jira priority automatically. Use readable plain text and simple bullets, avoiding assumptions about Markdown rendering, API document formats, mentions, or link previews. Never put `file://`, absolute local links, or relative image URLs in paste text as though teammates can open them. List the exact screenshot filenames to attach instead; the portable Markdown summary uses relative links after extraction.

After reviewing `share/`, make `share.zip` from an explicit allowlist of its reviewed regular files when an existing archive tool is available. Include `summary.md`, the two drafts, the evidence index, and selected screenshots using relative paths. Exclude symlinks, path escapes, raw `evidence/`, previous runs, source checkouts, auth files, and the archive itself. Do not recursively archive the entire run/project directory. Verify the archive member list, readability, and that internal image links resolve. If archive creation is unavailable, deliver the sharing folder and describe the missing archive; do not install a global tool just for packaging.

Before delivering an execution bundle, check referenced files exist, screenshots match their captions/IDs, text and image privacy review is complete, and summary/drafts preserve the full report's verdict and material gaps. Return clickable absolute local paths to the report, summary, drafts, screenshots, and archive that actually exist; for plan-only or unwritable-output cases, return only the permitted/available deliverable. This local preparation does not imply anything was uploaded or posted.

## Posting only when requested

Do not send Slack messages, create/update Jira issues/comments, or upload attachments merely because drafts were created. Do not add a routine Slack/Jira approval questionnaire. If the user explicitly requests publication, use the prepared exact content and identified destination through an available connector; ask only for missing destination/authorization details after the content is ready. Existing explicit authorization counts. Confirm which attachments are included, verify destination identity, and report actual resulting URLs or any delivery failure. Text-posting authorization alone does not authorize uploading unrelated traces or the whole local run folder. If a submission outcome is ambiguous, check the destination for this run's message/comment before retrying to avoid duplicates. No connector or login is required to prepare the files.

Keep the existing [origin PR reporting](pr-reporting.md) behavior: offer the finished report only for a verified matching PR and obtain consent unless already authorized. Preserve observed successes, confirmed failures, and gaps when condensing that comment; local image links do not become hosted attachments automatically.
