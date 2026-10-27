# Local findings report

Write `report.md` and place sanitized evidence/reproductions beside it. Use the user's language; preserve code, payloads, and command output exactly. No issue tracker or PR is required.

For an explicitly plan-only request, deliver the proposed coverage, assertions, prerequisites, and limits as **PLAN ONLY — validation not run by request**. Do not assign an execution pass/fail verdict, fabricate build identity/evidence, or call unexecuted-by-request probes blocked. Reserve blocked status for genuinely unavailable prerequisites.

## Report contents

1. **Verdict and impact:** `FAIL`, `INCOMPLETE`, or `PASS (scoped)`; reason, most important observed impact, and whether coverage is incomplete.
2. **Tested scope:** repository/branch, HEAD, base/merge-base, dirty changes included/excluded, start/end revision status, feature contract, origin PR if matched, runtime/build identity. Record attribution limits.
3. **Environment:** target type, browser/device/OS and build, account roles/fixture IDs without credentials, startup/test commands, relevant tool versions, real versus mocked dependencies.
4. **Impact and coverage matrix:** changed behavior → downstream consumer → invariant/source → probe → platform → `passed`, `failed`, `blocked`, `not run`, or `not applicable`, with evidence/reason. Include primary flow, invalid/boundary inputs, relevant unchanged consumers, and platform/state/failure probes. Do not inflate coverage with unexplained counts.
5. **Confirmed findings:** stable IDs, severity, affected journeys/platforms, exact reproductions, expected/actual results, durable state, and evidence below. Keep unverified risks and ambiguous requirements separate.
6. **Checks, limitations, cleanup:** check commands/results, blocked dependencies/platforms, unobserved side effects, interrupted/time-limited probes, remaining fixtures/processes, artifact paths, next actions.

Record the full-stack selection pass: relevant user goals and quality dimensions, chosen test layers, outcomes, and remaining risk. Group genuinely irrelevant dimensions with reasons; keep blocked/deferred applicable probes visible. Include fixture validation and environment/baseline details when needed to interpret the evidence. Accessibility, performance, and visual results must state their measured scope rather than imply conformance, production capacity, or approved appearance from limited checks.

Include explicit coverage rows for query injection, XSS, CSS injection, JavaScript injection, and prompt injection. Each row identifies the reachable input/sink and result/evidence, or a concrete reason for `not applicable`, `blocked`, or `not run`. For injection findings, include the payload and benign control, the violated trust boundary, protections active during the attempt, and the observed consequence. For LLM probes, distinguish model output, attempted tool use, and actual authorized/blocked execution; state model/configuration and attempts. A rejected tool request alone does not prove authorization bypass; identify a separate established model-policy violation before calling the request itself a defect. Do not label accepted special characters or a generic error as an exploit.

## Finding format

```markdown
### BB-001 — Concrete failure and user impact

- Severity: P1 / P2 / P3 / P0 when warranted
- Attribution: introduced / pre-existing / unknown, with comparison evidence
- Affected flow/platform: feature and downstream consumers
- Location: verified path:line; root-cause location unconfirmed when unknown
- Preconditions: revision/build, role, fixture, initial state
- Reproduce:
  1. Exact action/command with exact payload and setup.
  2. Trigger and independent read/next consumer.
- Expected: contract and its source
- Actual: observed UI/API/output plus persisted state/side-effect difference
- Reproducibility: attempts and outcomes; schedule/seed for timing-sensitive probes
- Evidence: relative artifact links, sanitized excerpts, runnable repro
- Fix direction: relevant contract/layer to inspect; distinguish inference
- Regression prevention: setup and behavioral assertion, smallest useful test layer, existing test location, and local/PR/scheduled feedback stage; recommendation only unless changes were requested
```

Use **P0** for demonstrated critical widespread data loss/security/availability impact; **P1** for a serious broken core flow, unauthorized access, or corruption; **P2** for a substantive edge-case/secondary-flow defect; **P3** for a minor reproducible usability defect. Severity depends on demonstrated context, not the attack's label. Style preferences are not findings.

## Evidence checks before delivery

- Each finding has an observed failure, reproducible setup/input, independent expected outcome, and consequence. Never fabricate output or claim an unexecuted source-only hypothesis was tested.
- Locations match the tested revision. Mark inferred causes and unknown attribution. Pre-existing failures can matter without being blamed on the branch.
- Rejected mutations were checked for side effects; successful mutations for durability where applicable. Missing essential postconditions remain coverage gaps.
- No auth state, tokens, cookies, passwords, personal data, or unrelated private logs. Review screenshots/traces too. Redact secrets while preserving the failing input's shape.
- `PASS (scoped)` has actual execution and no unexplained applicable probe blocked/not run. `FAIL` retains gaps. Blocked before execution means `INCOMPLETE`, with setup evidence and next step.
- No-findings reports say what ran and remains uncertain, never “bug-free.”

The final chat answer exposes useful findings and links the full local report. Offer PR publication only if a matching PR exists.
