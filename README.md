# Branch Breaker

A global agent skill that validates branch changes like a skeptical senior QA engineer: run the feature, challenge its assumptions, follow the change into other flows, and return reproducible findings.

Works with **web, mobile web, native Android, native iOS, hybrid apps, and supporting APIs/services**. It discovers the current project's tools and conventions. Install it once at user scope; no repository owns it or needs special configuration.

## What it does

1. Resolves the branch/base and relevant uncommitted changes, then identifies the build actually being tested.
2. Maps changed code to callers, shared components, schemas, storage, queues, caches, and downstream consumers.
3. Runs existing checks and the normal feature journey, then probes invalid input, Unicode, boundary values, state transitions, authorization, races, failures, and recovery.
4. Checks final state and adjacent flows: a rejected save must not mutate data; a saved label must still work in search/export; offline retries must respect the application's duplicate-handling contract.
5. Produces a local report with severity, exact reproductions, expected/actual behavior, affected flows, evidence, and fix direction.
6. Finds a related open PR on `origin`, when available, and **asks before posting the report as a comment**.

It executes within disposable test environments and preserves product code. It does not silently implement fixes or weaken tests. Missing tools/devices produce explicit coverage gaps. `PASS (scoped)` means the described checks passed, not that the app is bug-free.

## Install globally

Install from `GustavoEmmel/branch-breaker`:

```sh
npx skills add GustavoEmmel/branch-breaker -g
```

Choose your agents interactively, or target Codex:

```sh
npx skills add GustavoEmmel/branch-breaker -g -a codex
```

The `-g` flag installs at user scope. The [Skills CLI](https://github.com/vercel-labs/skills) currently requires Node.js 22.20 or later. The skill itself is Markdown and has no runtime dependency; test execution uses the target application's tools.

Manual installation for Codex, with no Node.js requirement:

```sh
mkdir -p "$HOME/.agents/skills" "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/GustavoEmmel/branch-breaker.git "$HOME/.agents/skills/branch-breaker"
ln -s "$HOME/.agents/skills/branch-breaker" "${CODEX_HOME:-$HOME/.codex}/skills/branch-breaker"
```

Use an unused destination; these commands intentionally do not overwrite existing skills. For other agents, use their user-level skill directory or the global CLI installer. Start a new agent session if needed to refresh skill discovery.

## Use it

In any application checkout:

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
- [Web execution](references/web-execution.md) and [mobile execution](references/mobile-execution.md): runtime-specific guidance
- [Report contract](references/report-contract.md): actionable findings and evidence requirements
- [PR reporting](references/pr-reporting.md): origin matching and consent before publication
- [Validation](VALIDATION.md): checks performed and their limits

## Inspiration

[The Judge](https://agent-skills.techleads.club/skills/the-judge/) informed the emphasis on evidence and actionable findings. [Microsoft's Playwright CLI skill](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/tools/skills/playwright-cli/SKILL.md) and [Playwright Test Agents](https://playwright.dev/docs/test-agents) informed the browser exploration and reproduction workflow. Platform references are linked in the execution guides.

This is an original skill, not a fork or copied implementation. It uses the [Agent Skills format](https://agentskills.io/specification) and includes Codex UI metadata.

MIT licensed. Copyright © 2026 GustavoEmmel.
