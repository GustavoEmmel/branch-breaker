# Branch Breaker

A global agent skill that validates branch changes like a skeptical senior QA engineer: run the feature, challenge its assumptions, follow the change into other flows, and return reproducible findings. It selects full-stack quality checks from the risks of the change, including data, accessibility, visual behavior, performance, security, recovery, and mobile behavior.

Works with **web, mobile web, native Android, native iOS, hybrid apps, and supporting APIs/services**. It discovers the current project's tools and conventions. Install it once at user scope; no repository owns it or needs special configuration.

## What it does

1. Resolves the branch/base and relevant uncommitted changes, then identifies the build actually being tested.
2. Maps changed code to callers, shared components, schemas, storage, queues, caches, and downstream consumers.
3. Runs existing checks and the normal feature journey, then probes invalid input, Unicode, boundary values, state transitions, authorization, races, failures, and recovery. Explicitly attempts **query injection, XSS, CSS injection, JavaScript injection, and prompt injection** on applicable surfaces, using controlled local exploit proofs and checking downstream/stored paths.
4. Checks final state and adjacent flows: a rejected save must not mutate data; a saved label must still work in search/export; offline retries must respect the application's duplicate-handling contract.
5. Produces a local report with severity, exact reproductions, expected/actual behavior, affected flows, evidence, fix direction, and the smallest useful regression test to prevent recurrence.
6. Finds a related open PR on `origin`, when available, and **asks before posting the report as a comment**.

It executes within disposable test environments and preserves product code. It does not silently implement fixes or weaken tests. Missing tools/devices produce explicit coverage gaps. `PASS (scoped)` means the described checks passed, not that the app is bug-free.

Injection coverage appears in every report, including a reason when a class has no relevant surface. The agent must demonstrate the trust-boundary violation; accepting punctuation or returning a server error alone is not an exploit. Prompt-injection probes target an application's LLM and tools with synthetic data, while the QA agent treats attack text as untrusted input. “XSS” means cross-site scripting; CSS injection is covered separately as well.

### Full-stack quality improvements

Public materials for Gayathri Mohan's *Full Stack Testing* informed the expanded workflow:

- Select test layers and relevant quality dimensions from the affected architecture and user journey.
- Validate fixture data and follow changes through storage, caches, events, exports, and other clients.
- Check keyboard/focus/error recovery and stable visual comparisons where the UI is affected.
- Measure relevant performance under comparable conditions and existing budgets; preserve uncertainty.
- Recommend a focused regression assertion and feedback stage for every confirmed defect.

This does not force ten test suites, install the book's tool catalogue, change CI, or add a setup questionnaire. The [quality guide](references/full-stack-quality.md) contains the operational checks; the [source map](references/learning-sources.md) separates verified public material from our own adaptations and records access limits.

## Install globally

One install configures **Codex, Cursor, and Claude Code** with no menus or confirmation prompts. Requires Git and Python 3.9+ on macOS/Linux (or WSL):

```sh
mkdir -p "$HOME/.local/share"
git clone https://github.com/GustavoEmmel/branch-breaker.git "$HOME/.local/share/branch-breaker"
python3 "$HOME/.local/share/branch-breaker/install.py"
```

The checkout stays at `~/.local/share/branch-breaker`. The installer creates these global links:

| Location | Purpose |
|---|---|
| `~/.agents/skills/branch-breaker` | Shared skill pointing to the Git checkout |
| `~/.codex/skills/branch-breaker` | Codex compatibility location; respects `CODEX_HOME` if set |
| `~/.cursor/skills/branch-breaker` | Cursor user skill |
| `~/.claude/skills/branch-breaker` | Claude Code user skill |

The [installer](install.py) uses only Python's standard library. It makes filesystem changes; it does not download packages, run `npx`, launch the application, or execute QA. Inspect it before running if desired. Existing copies and conflicting links are preserved under `~/.local/state/branch-breaker/backups/`, outside skill discovery, with a manifest of original paths. Correct links are kept; repeat runs create no nested/self-referencing links. It also repairs the known accidental `branch-breaker/branch-breaker` self-link.

If you already have this repository cloned, run `python3 /path/to/branch-breaker/install.py` instead. Keep that checkout in place: all agent directories use it. If it is already at the recommended location, skip cloning and run the installer. Start a new session in your agent to refresh discovery.

### Update

For the recommended checkout location:

```sh
git -C "$HOME/.local/share/branch-breaker" pull --ff-only
python3 "$HOME/.local/share/branch-breaker/install.py"
```

Use your actual checkout path if different. All three agents read the same updated files. No manual re-copying or agent selection is needed.

## Use it

In any application checkout, invoke `$branch-breaker` in Codex or `/branch-breaker` in Claude Code/Cursor. Natural-language requests work too:

```text
Use $branch-breaker to validate this branch against origin/main.
Include my uncommitted feature changes. Try to break the new flow
and other flows affected by it. Return a local findings report.
```

For web and native mobile:

```text
Use $branch-breaker on the checkout changes for web, Android, and iOS.
Use the project's available browser and native test tools.
Focus on keyboard input, offline retries, lifecycle, and saved state.
```

For review preparation:

```text
Use $branch-breaker as the QA pass for this branch's code review.
Find regressions beyond the existing tests. If there is a related
open PR on origin, show me the report and ask whether to comment it.
```

You can specify a feature, base ref, local URL, test device/build, output directory, or time budget. These are natural-language instructions, not CLI flags.

The skill starts immediately, infers routine choices from the checkout, and executes available checks without a plan-approval pause or setup questionnaire. Missing tools/devices become report gaps while other checks continue. It asks only when essential information cannot be discovered and meaningful progress is impossible, or once at the end before posting to a PR. Agent-enforced tool permission prompts are separate from the skill.

If you explicitly ask for a plan only, it returns proposed probes and prerequisites without executing them or querying PRs, clearly labeled as validation not run.

## Platform coverage

| Target | Execution route |
|---|---|
| Desktop/mobile web | Existing Playwright or available browser automation |
| Native Android/iOS | Existing Maestro, Appium, Detox, XCUITest, Espresso, or native device automation |
| Hybrid | Native and discovered WebView contexts with the configured harness |
| API/CLI/worker/library | Real interface, repository fixtures, and downstream postconditions |

Native execution requires a compatible build and available simulator/emulator/test device. Browser viewport emulation counts only as mobile-web coverage. Unsupported platforms stay visible in the report as incomplete.

## Report and PR behavior

Reports contain a tested revision/build, impact/coverage matrix, findings with exact reproductions and evidence, existing check results, and remaining gaps. Verdicts are `FAIL`, `INCOMPLETE`, and `PASS (scoped)`. Confirmed defects remain failures even if another part of the run is blocked.

Reports stay local by default, using the requested location, the project's artifact convention, or an OS temporary directory. The agent returns the absolute path. A matching PR must be verified against origin and its head identity; unpublished local changes are disclosed. Posting requires explicit approval for the identified PR, uses a comment rather than a formal review, and returns the comment URL. No PR or GitHub access is needed for local QA.

## Contents

- [SKILL.md](SKILL.md): workflow and verdict rules
- [Adversarial probes](references/adversarial-probes.md): input, state, failure, and downstream attack selection
- [Full-stack quality](references/full-stack-quality.md): test-layer selection, data, accessibility, visual, performance, and recovery checks
- [Learning sources](references/learning-sources.md): public book/author sources, supporting documentation, and attribution
- [Web execution](references/web-execution.md) and [mobile execution](references/mobile-execution.md): runtime-specific guidance
- [Report contract](references/report-contract.md): actionable findings and evidence requirements
- [PR reporting](references/pr-reporting.md): origin matching and consent before publication
- [Validation](VALIDATION.md): checks performed and their limits
- [Installer](install.py): noninteractive global installation for all three agents

## Inspiration

[The Judge](https://agent-skills.techleads.club/skills/the-judge/) informed the emphasis on evidence and actionable findings. [Microsoft's Playwright CLI skill](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/tools/skills/playwright-cli/SKILL.md) and [Playwright Test Agents](https://playwright.dev/docs/test-agents) informed the browser exploration and reproduction workflow. Platform references are linked in the execution guides.

This is an original skill, not a fork or copied implementation. It uses the [Agent Skills format](https://agentskills.io/specification) and includes Codex UI metadata.

Agent directory references: [Codex](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills#choose-where-skills-load), [Cursor](https://cursor.com/docs/skills#skill-directories).

MIT licensed. Copyright © 2026 GustavoEmmel.
