# Authoring validation

Initial authoring validation: 2026-10-24. Latest instruction update: 2026-10-30.

## Version 1.5 search/filter completeness update

Added explicit off-page search/filter coverage and a named P1 severity rule for confirmed collection-wide controls that operate only on loaded/paginated subsets. The procedure verifies eligible records outside the actual prefetch/cache window, traces UI/API/provider behavior, challenges pagination state, and distinguishes intentional local scope from hidden implementation limits.

Independent review tightened ranking/cap semantics, page-warming diagnostic controls, and severity consistency. A fresh-context agent applied the final instructions to seven synthetic evidence cases: frontend subset-only search and backend filtering after pagination were classified P1; unauthorized records, complete local datasets, and explicitly page-local controls were not falsely flagged; source-only suspicion stayed unverified; insufficient off-page fixtures remained a coverage gap. Its plan for 150 records accounted for page size, prefetch ambiguity, text/status/combined controls, cursor resets, and independent result evidence. This was a plan-only instruction evaluation, not execution against a search application.

Skill-format, local reference/anchor, and whitespace checks passed. The unchanged installer was run successfully; shared, Codex, Cursor, and Claude paths retain the updated skill. No target product code or installer behavior changed, and no live search campaign or PR comment was performed for this update.

## Version 1.4 UX/UI and user-perspective update

Added a branch-scoped walkthrough of user value, task effort, language, navigation, feedback, recovery, hierarchy, and platform-appropriate interaction. Confirmed usability defects remain impact-ranked findings; heuristic concerns and product hypotheses are reported separately without invented user research, aesthetic scores, or automatic failure for justified tradeoffs. Local and optional PR reports retain this distinction. Public primary guidance and access limits are recorded in the source map.

Independent instruction review found no actionable conflicts with evidence requirements, global/web/mobile scope, minimal interaction, or PR-comment consent. All 17 installer regression tests pass, including rejecting a checkout missing the new UX/UI reference. Skill format, UI metadata, local Markdown links, and whitespace checks passed. Re-ran the global installer and verified that shared, Codex, Cursor, and Claude paths expose the same updated guide without replacing working links.

A fresh-context agent applied the skill to a disposable web draft editor with a base revision, a changed save handler, documented user contracts, and three passing server-rule tests. Using the real in-app browser, it reproduced rejected saves that claimed success and erased entered work on desktop and a mobile-web layout with 375 CSS pixels of content width. Independent API reads confirmed that the rejected draft was absent; the base revision displayed the error and preserved input. Valid saves/reloads, keyboard navigation, and a stored-input canary provided additional controls. Screenshots and reproductions were retained locally. This checks one small synthetic workflow, not general defect-detection effectiveness or mobile-device coverage.

## Version 1.3 full-stack quality update

Expanded risk selection using the verified public sources documented in `references/learning-sources.md`. Added guidance for test-layer choice, fixture validation, data reconciliation, accessibility, visual comparison, bounded performance, recovery, and regression-test placement. Independent review found no actionable scope/provenance issues and confirmed that branch focus, injection coverage, minimal interaction, and PR-comment consent remain intact.

All 17 installer regression tests pass with both new reference files included in complete-install validation. Skill format, UI metadata, local documentation links, and all four global installation paths were verified. This authoring update does not establish that any application passed accessibility, visual, performance, or resilience testing; those procedures were not run against a live target.

An independent agent applied the draft to two synthetic planning requests: a localized web checkout and a backend inventory event pipeline. Its plans selected relevant layers and downstream assertions, preserved missing-baseline/device limits, avoided invented findings, and recommended regression placement without CI edits. This was a plan-only behavioral check, not application execution. It exposed ambiguous execution/verdict wording for explicitly planning-only requests; the final skill now provides a clear plan-only exception and labels validation as not run.

## Version 1.2 injection coverage update

Added explicit applicability, execution, and reporting requirements for query injection, XSS, CSS injection, JavaScript injection, and prompt injection. Reviewed controlled exploit oracles and false-positive distinctions against the primary OWASP references linked in the adversarial guide. Each class now requires an evidence-backed result or an explanation of missing/inapplicable coverage, including downstream and stored-input paths.

This update changes instructions and documentation only. Skill format and local reference checks passed; the existing installer was unchanged. No live injection campaign or target-model security evaluation was performed during this authoring update. The guidance is not a claim that any application has passed these security checks.

## Version 1.1 installation update

`python3 -m unittest discover -s tests -v` passes all 17 installer regression tests in isolated temporary homes. Coverage includes fresh installation for all three agents, existing plain-copy migration, preservation of user files and unrelated link targets, idempotent reruns, broken/self-referencing links, paths with spaces, `CODEX_HOME`, missing source files, and unsafe ancestry in both directions. A subprocess test installs with stdin closed and reruns through Claude's installed link.

Applied the installer to the author's account: preserved the old shared copy in backups, retained the working Codex/Claude links, and created the missing Cursor link. Verified all four global paths resolve to one Git checkout. A second run through the Claude link made no link replacements or additional backups and created no nested self-link. These are filesystem/discovery-path checks; launching all three agent applications was not part of the test.

The skill now explicitly skips routine setup/plan-approval questions and keeps the final PR-comment consent. Publication selection and approval are combined when multiple PRs match. Agent-enforced permission prompts remain outside the skill's control.

## Format and installation

- Passed the Codex skill-creator frontmatter/scaffold validator.
- Checked skill naming, description length, Codex UI metadata, and local reference links.
- Installed at user scope, with a global Codex link resolving to the canonical skill directory.
- Checked that skill instructions contain no application-specific paths, startup commands, or required project configuration.

## Executed forward evaluation

A separate agent followed the skill against a disposable Python HTTP API with a correct baseline, a feature branch, documented contracts, and three passing existing tests. The evaluation used real loopback HTTP requests, fresh processes/fixtures, saved reproductions, independent reads, and baseline comparisons. Application source files were preserved.

The feature run executed 19 focused scenarios: 10 passed and 9 failed. The failures reduced to three distinct confirmed defects:

| Defect | Why ordinary happy-path coverage missed it |
|---|---|
| A rejected bulk update still persisted invalid data | Returning an error was insufficient; the subsequent read exposed the write |
| A decomposed Unicode label disappeared from search | Saving worked, but the unchanged search consumer used a different normalization contract |
| Export corrupted commas, quotes, and newlines | Simple labels exported successfully; structured CSV parsing exposed column/row damage |

Each defect also had a minimal reproduction. Two baseline controls passed. The generated evidence recorded that started processes stopped and source content remained unchanged.

The evaluator encountered the expected defect list during agent discovery. This is therefore a **known-defect execution and reporting check**, not a blind bug-discovery benchmark or a detection-rate claim.

## Review and limits

Review tightened source fingerprinting for already-dirty files and PR matching for verified fork checkouts. Web and mobile guidance was checked against primary Playwright, Maestro, Appium, and Detox documentation linked in the execution references.

The initial authoring evaluation did not execute a real browser/native-device session or GitHub comment submission. Version 1.4 adds the small browser exercise described above; native-device behavior, actual user research, and live PR-comment submission remain untested in this authoring work. No report was posted to a live PR. Future evaluations should exercise native flows, unavailable-device handling, origin/fork matching, and approval/retry behavior with disposable resources.

Skill format checks do not prove agent behavior. The forward evaluation establishes that this run produced executable probes and useful findings beyond the existing suite; it does not guarantee the same outcome in every codebase.
