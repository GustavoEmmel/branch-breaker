# Authoring validation

Initial authoring validation: 2026-10-24. Latest instruction update: 2026-10-27.

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

No real browser/native-device session or GitHub comment submission was executed during this authoring validation. Those instructions are reviewed guidance, not demonstrated cross-platform coverage. No report was posted to a live PR. Future evaluations should exercise real browser/native flows, unavailable-device handling, origin/fork matching, and approval/retry behavior with disposable resources.

Skill format checks do not prove agent behavior. The forward evaluation establishes that this run produced executable probes and useful findings beyond the existing suite; it does not guarantee the same outcome in every codebase.
