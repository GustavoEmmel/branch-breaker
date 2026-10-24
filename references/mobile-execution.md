# Native and hybrid mobile execution

Identify affected runtimes: native Android, native iOS, hybrid WebViews, mobile browsers, and shared backend contracts. A responsive web build or shared JavaScript test does not establish native behavior.

## Select an executable route

Use configured Maestro, Appium, Detox, XCUITest, Espresso, or available native automation. Inspect supported builds, installed drivers, devices, fixtures, and commands first. Do not assume a framework exists because the app uses React Native or Flutter. A compatible installed app/build and reachable test backend are required.

- Appium: inspect the installed platform driver and discover actual native/WebView contexts; do not guess names or capabilities.
- Detox: use the existing build/configuration. Synchronization can prevent an intended in-flight interaction; use supported controls narrowly and restore them afterward.
- Maestro: check installed command support and defaults. Launch/reset/permission defaults can invalidate persistence or denial probes. Verify entered text, especially Unicode on Android and secure inputs on iOS.
- Native platform tests/device tools: use supported actions and evidence paths; don't add a new framework solely to satisfy this skill.

Without usable device/build/driver/credentials, continue code/shared-contract/API probes and mark the missing native platform incomplete. Do not substitute browser emulation. A human can perform a precisely described step when necessary, but label it user-reported unless the agent observes the result.

## Platform-specific attacks

| Area | Actions to select from | Observable postcondition |
|---|---|---|
| Input/keyboard | Paste versus typing, emoji/combining marks, multiline, length boundary, Next/Done, keyboard during validation | Actual value reached app/backend; actions/errors reachable; keyboard respects form contract |
| Lifecycle | Background during save, resume, terminate/relaunch after success, cold-start deep link | Correct draft policy and durable state; no duplicate/lost mutation or stale identity |
| Navigation | Android system back; iOS in-app back/swipe; dismiss nested modal; repeated/deferred deep link | Correct stack and cancel/commit behavior; no protected screen bypass |
| Permissions | Unset, denied, granted, revoked between sessions where supported | Usable fallback/recovery; no unauthorized sensor/file access or unexpected side effect |
| Connectivity | Offline launch, disconnect during write, reconnect, retry, queued replay | Controlled recovery, consistent sync state, no lost or duplicate operation |
| Layout | Small supported screen, supported rotation while editing, larger accessibility text | Inputs preserved; actions/errors reachable; no unintended submission |
| Hybrid boundary | Native → WebView → native, session transfer, bridge input, back/keyboard, deep link | Correct identity, escaped data, synchronized state, and navigation |
| App/version boundary | Old local records, supported upgrade path, changed API response consumed by another client version | Compatible reads/writes or documented migration/error; no silent data loss |

Do not clear app data between saving and verifying persistence. Do not replace background/resume with a cold relaunch. Use unique fixtures and disposable devices for reset/permission experiments. Avoid device-wide cleanup such as clearing a personal device's keychain. Verify actions the harness actually performed and note platform differences.

Record OS/device or simulator/emulator, app identifier, build/revision, backend target, harness/driver version, reset strategy, and screenshots/video/log excerpts. Pair backend durable reads with native UI observations. Explain physical-device behaviors the simulator cannot establish.

## Official references and version-sensitive caveats

- [Maestro platforms](https://docs.maestro.dev/get-started/supported-platform), [launchApp](https://docs.maestro.dev/reference/commands-available/launchapp), [inputText](https://docs.maestro.dev/reference/commands-available/inputtext)
- [Maestro back](https://docs.maestro.dev/reference/commands-available/back), [orientation](https://docs.maestro.dev/reference/commands-available/setorientation)
- [Appium drivers](https://appium.io/docs/en/latest/ecosystem/drivers/), [contexts](https://appium.io/docs/en/latest/guides/context/)
- [Detox setup](https://wix.github.io/Detox/docs/introduction/project-setup/), [synchronization](https://wix.github.io/Detox/docs/articles/design-principles/), [device API](https://wix.github.io/Detox/docs/api/device/)

At writing, Maestro documents restart and granted-permission defaults for `launchApp`, Android Unicode limitations in `inputText`, and Android/web-only `back`. Detox documents platform limits for permission APIs. Check installed-version docs before relying on these; a harness limitation is a coverage gap, not a product defect.
