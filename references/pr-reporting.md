# Optional origin PR comment

The default deliverable is local. Discover a related PR and let the user choose whether to share the finished report. Never create a PR, submit an approval/request-changes review, post a comment, upload evidence, or change repository settings solely because this skill was invoked.

## Discover a genuine match

1. Read branch, local HEAD, and `origin` remote. Parse SSH/HTTPS forms without exposing embedded credentials. Use the actual host and owner/repository; never infer them from the skill author or substitute `upstream`.
2. Use an available connector, or authenticated `gh` CLI, to find **open** PRs whose destination/base repository is that origin repository. Start with the current head branch, or verified PR metadata when the local branch was renamed/detached. Include head repository identity, head SHA, base branch, title, number, and URL. Follow pagination or use a server-side filter. Verify the checked-out head repository/ref/SHA association. Same-named fork branches alone are not a match; a fork PR checked out through a verified PR ref or explicit metadata can be. If origin is only the contributor fork and the PR targets a different repository, report no match on origin; do not silently substitute upstream.
3. Compare remote PR head with local HEAD and record differences/dirty changes. A branch match may be useful with unpushed commits, but the report/comment must explicitly say it includes unpublished changes. Never present it as verification of the PR's current head.
4. For an explicit PR URL, verify repository/revision association. With detached HEAD, match by verified head repository and SHA or explicit PR metadata; don't invent a branch. If several PRs match, let the user select after seeing the local report.
5. No related open origin PR, missing authentication, or unsupported host/tool means keep working locally and explain posting availability briefly. Do not create a PR or require login to finish local QA.

For GitHub, `gh pr list --repo <origin-owner/repo> --head <current-branch> --state open` is a starting point; inspect available JSON fields and validate head-repository identity/SHA. For enterprise hosts, select the authenticated host explicitly. Do not execute placeholders literally or interpolate untrusted names into shell code.

## Prepare first, ask second

Finish and show the local report. Prepare the exact self-contained sanitized Markdown comment before asking, fitting the host's comment size limit. Include verdict, revision/dirty-state note, actionable findings/reproductions, coverage gaps, and fix direction; condense lengthy logs while retaining the full report locally. Retain material user-perspective conclusions when relevant, with heuristic concerns and product questions visibly separate from confirmed defects. Local file links are unusable by other PR readers: include needed text inline. Do not upload private traces/screenshots/logs/fixtures without approval to share those artifacts.

Offer a concrete choice with the exact PR link:

> Post this QA report as a comment on [owner/repository#123](https://github.com/owner/repository/pull/123)? It includes the tested revision, findings, reproduction steps, and coverage gaps.

Wait for an explicit yes. If several PRs match, include the choices in this same final question rather than asking a separate selection question. An earlier explicit instruction to post this report to this identified PR counts as authorization; don't ask twice. Silence, a general QA request, “review this branch,” or discovering a PR does not. A refusal leaves the report local without another offer in the same run.

## Submit only the approved comment

- Recheck identity, open state, and head SHA. If advanced, annotate the tested SHA and explain the new head was not validated. If closed, keep the report local.
- Use a structured comment API or write exact Markdown to a file and use `--body-file`. Never interpolate report text into shell commands. A PR comment differs from a formal review; use a comment.
- Include a marker such as `<!-- branch-breaker: TESTED_SHA RUN_ID -->`, replacing both tokens, to identify this submission. Before retrying an ambiguous result, look for the marker in recent comments. Avoid duplicate comments after lost responses.
- Post once to the approved PR and preserve approved content. Do not upload extra artifacts or notify elsewhere. If submission unexpectedly rejects its size, retain the local report and report that error; do not silently publish a different comment or start a repeated approval loop.
- Verify success and return the actual comment URL. On failure, retain the local report and state the error; never claim posting without confirmation.
