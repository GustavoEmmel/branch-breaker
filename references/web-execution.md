# Web and mobile-web execution

Reuse the repository's browser setup and test accounts. Prefer Playwright when already available; equivalent browser tools are acceptable. Explore the actual page before generating selectors/tests. Read the installed tool's help rather than assuming another CLI's commands.

## Reliable interaction and observation

- Exercise the initial journey through visible controls. Use roles, labels, accessible names, and stable test IDs; scope repeated buttons to their row/dialog. Avoid brittle position selectors and forced clicks that conceal broken user interactions.
- Wait for meaningful observable state and use retrying assertions where supported. Register response listeners/interception before the triggering action. Do not synchronize races with arbitrary sleeps.
- Observe console messages, page exceptions, failed requests, and HTTP error responses. A completed HTTP 404/500 is not a `requestfailed` event. Show user impact rather than reporting every log message as a defect.
- Verify actual entered characters, files, outgoing parameters, responses, and durable reads. URL/form encoding and client validation can change or block the intended probe.
- After mutations, reload and revisit relevant list/detail/edit/search/export surfaces. A success toast is not proof of storage or side-effect correctness.
- API probes may bypass the UI to challenge server validation and authorization. They do not replace UI smoke coverage for a changed screen.

## Isolation, failures, and races

Use fresh contexts for independent identities. Browser contexts isolate browser state, not the backend; allocate distinct test records. Use multiple pages deliberately for same-session stale state. Keep authentication files local and ignored.

Coordinate two requests/pages with explicit barriers for concurrent edit, duplicate submit, delayed response, or navigation during save. Assert final persisted state and side-effect count. Record the schedule.

For injected faults, record which route matched and whether the request reached the server. Stubbed responses demonstrate client behavior, not actual backend behavior. Service Workers can bypass interception; disabling them changes the environment and must be disclosed. Remove interception and run a valid recovery control.

Use responsive viewport/touch/device profiles for mobile-web coverage. Where platform-specific behavior matters, record the actual browser engine/device. Viewport emulation does not exercise native apps, OS permissions, or every physical-device behavior.

## Evidence

Save a runnable test or exact interaction sequence and relevant logs/response/state. Use screenshots for visual failures and traces when available. Playwright Test tracing includes test context; standalone `context.tracing` does not record assertion calls. Review artifacts for auth tokens, cookies, personal data, and private URLs before sharing.

Do not let a test healer reinterpret a product failure as the expected result. Repair demonstrably wrong selectors/fixtures, then rerun; preserve failures revealing broken contracts. Report flaky first failures and relevant retry results.

## Official references

- [Microsoft Playwright CLI skill](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/tools/skills/playwright-cli/SKILL.md)
- [Playwright Test Agents](https://playwright.dev/docs/test-agents)
- [Best practices](https://playwright.dev/docs/best-practices), [locators](https://playwright.dev/docs/locators), [assertions](https://playwright.dev/docs/test-assertions)
- [Isolation](https://playwright.dev/docs/browser-contexts), [network](https://playwright.dev/docs/network), [emulation](https://playwright.dev/docs/emulation)
- [Request failures](https://playwright.dev/docs/api/class-page#page-event-requestfailed), [tracing](https://playwright.dev/docs/api/class-tracing), [authentication](https://playwright.dev/docs/auth)

Consult documentation matching the installed version when behavior matters. Links are reference material, not evidence that any particular run occurred.
