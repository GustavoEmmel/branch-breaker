# Full-stack quality for a branch QA run

Use this guide while mapping impact, then read only the recipes relevant to the changed behavior and its consumers. These are Branch Breaker's operational adaptations; [learning sources](learning-sources.md) identifies the public material that informed them.

## Choose risks before tools

Name the affected user, their goal, the important failure, and how it would be observed. Consider the dimensions below without turning a small change into a whole-system audit. Choose high-impact, plausible risks first and record deferred/blocked applicable checks. Missing tools do not make a risk irrelevant. Reuse the project's harness; book examples are not a tool-installation checklist.

| Dimension | When it matters | Useful branch-focused evidence |
|---|---|---|
| Exploratory | New behavior, ambiguous assumptions, unexpected observations | A short charter plus varied inputs/actions and real user consequences |
| Automated functional | Business rules, API/component changes, shared logic | Focused assertions at the relevant boundary, with a critical real journey retained |
| Continuous | Build/config changes or durable regression candidates | Actual commands, failure visibility, repeatability, and proposed feedback stage |
| Data | Schema, queries, persistence, caches, imports/exports, events | Reconciled records/values before and after, plus affected consumers |
| Visual | Layout, styles, fonts, text, loading/error states | Stable baseline comparison and demonstrated overlap/clipping/unreachable actions |
| Security | Input, identity, permissions, trust boundaries | Controlled exploit/authorization proof; use the existing injection guide |
| Performance | Rendering, request fan-out, queries, algorithms, expensive payloads | Comparable bounded measurements with environment, sample size, and expected target |
| Accessibility | UI controls, navigation, validation, dynamic updates | Actual keyboard/assistive interaction plus targeted automated findings |
| Cross-functional requirements | Recovery, compatibility, localization, operability | Observable resilience and user outcomes under relevant changed constraints |
| Mobile | Native consumers, device APIs, lifecycle, synchronization | Device/build-specific outcomes; use the mobile guide, not viewport substitution |

For a business-rule bug, isolate the rule and verify its user-visible consequence. For an API/message change, exercise the producer and a real consumer contract. For a changed screen, retain browser/native interaction even when service probes are faster. Contract tests establish interface compatibility within their scope, not all end-to-end behavior. Prefer test doubles at uncontrollable external boundaries; state what the doubles cannot establish.

## Data and asynchronous consumers

Use fixtures with known expected results: empty and populated states, boundary values, duplicates, old/new records, and related identities. Validate relationships and totals before the probe. After a change, reconcile source records against API, read model/cache, export, and message consumer where relevant. Check types, precision, null/default semantics, uniqueness, and row counts as the contract requires; a matching count alone can hide incorrect values.

For migrations, use a disposable database and supported old/new schema paths. Verify preserved values and compatible readers; test rollback only when supported. For async flows, correlate a unique operation/record ID, wait with a bounded deadline, and check duplicates, out-of-order delivery, retries, or partial failure where relevant. Distinguish legitimate eventual consistency from a missed update. Do not use arbitrary sleeps or assume exactly-once semantics without a contract. Record deterministic seed/time/cache conditions and clean up owned fixtures.

## Accessibility and visual usability

Use the affected journey with keyboard navigation: focus order/visibility, activation, dialog entry/exit, and form-error recovery. Inspect accessible names/roles and dynamic feedback; use an available screen reader for claims about actual announcements. Exercise zoom/text scaling and relevant long/localized content. Combine automated auditing with interaction; automated success alone cannot establish accessibility or WCAG conformance. State the criteria/tool/device actually checked. Native equivalents belong in the native harness.

For visual comparisons, hold browser/OS, viewport, fonts, fixture data, locale, and loading state stable. Inspect the changed area and affected consumers across relevant supported sizes. Stabilize incidental time/animation without hiding the behavior being tested. Do not regenerate snapshots to make failures pass or mask the changing component. Separate rendering noise and intentional design changes from clipping, lost controls, illegible feedback, and layout regressions. Without an approved baseline, report observed usability failures and the limit on regression attribution.

## Bounded performance evidence

Select a user-relevant metric and workload from existing requirements, SLOs, budgets, or a comparable base revision. Record data size, concurrency, duration/sample count, warm/cold cache, runtime/device, and network conditions. Start with local measurement, request/query counts, or a small controlled workload; avoid unbounded stress or paid/shared-service load.

Compare like-for-like runs and inspect variability, errors, throughput, and relevant latency/resource measures. A percentile needs enough observations to be meaningful; do not derive production capacity from a few local requests or treat one slow response as a regression. A known target violation or reproducible baseline regression supports a finding. If neither target nor reliable baseline exists, retain the measurement and risk without inventing a universal latency threshold. A local bounded pass is not load/capacity certification.

## Recovery, compatibility, and feedback

For relevant changes, interrupt a controlled dependency, restart an owned worker/app, exercise a compatible older client/record, or change locale/timezone. Verify recovery, retained data, deduplication/conflict rules, and actionable user feedback. Observe whether available logs/errors let the operation be identified without leaking secrets; do not demand a new telemetry platform. Keep resilience probes local and bounded.

Run fast focused checks first, then targeted integration/contract checks and a small critical end-to-end set. Add selected nonfunctional probes where risk warrants them; the sequence is adaptive, not a universal test-count ratio. Read existing CI definitions to place regression recommendations; never rewrite them during a QA-only task. A test that only works with a developer's hidden state is a reliability risk: capture its prerequisites. Record initial failures and reruns, separate flaky harness behavior from intermittent product failures, and preserve the failed evidence.

For each defect, propose a focused behavioral assertion at the earliest useful feedback stage. Recommend the relevant validation/contract improvement when supported. A missing performance target or conflicting requirement is an explicit prevention opportunity, not permission to invent a defect. Finish the applicable matrix, report residual risk, and stop rather than collecting more tests for a larger count.
