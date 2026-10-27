# Selecting adversarial probes

Use this as a menu driven by the impact map. Pick boundary representatives and realistic combinations; do not spray every payload at every endpoint. Record the expected invariant before executing a probe. Honor the environment's limits. Start concurrency with two controlled operations and oversized inputs just above the actual contract limit; do not turn smoke testing into a load test.

| Surface | Probe candidates | Postconditions to inspect |
|---|---|---|
| Required fields | Missing key, `null`, empty string, spaces, tabs, newline; distinguish omission from clearing | Consistent validation; no unintended default or partial write; usable feedback |
| Text and encoding | Apostrophe `O'Connor`, quotes, backslash, comma, newline, `&`, `%`, `+`, `#`, `<qa-probe>`, emoji, non-Latin text | Correct display, encoding, storage, search, export, and re-edit; no execution or unintended markup |
| Unicode | Composed `Café` versus `Cafe\u0301`, emoji sequences, non-breaking space, right-to-left text, zero-width character when relevant | Documented normalization/uniqueness; consistent UI/API/storage length semantics; no corruption |
| Length and count | Zero, one, min−1/min/min+1, max−1/max/max+1; byte versus character length | Same contract at every boundary; bounded handling; no truncation or accepted invalid record |
| Numbers | Negative, zero, decimal, numeric string, exponent, maximum accepted value ±1, integer overflow boundary | Correct type/range/precision and totals; errors do not commit state |
| Structured input | Wrong type, empty array/object, duplicate entries, unknown field, missing nested field, malformed JSON | Controlled error, no mass assignment or partial mutation; valid requests work afterward |
| Date and time | Invalid date, leap day, timezone offset, midnight, daylight-saving boundary, start after end | Defined ordering/timezone semantics across list/detail/export and platforms |
| IDs and URLs | Missing/deleted ID, another test user's ID, duplicate slug, encoded separators, query metacharacters | Correct ownership/routing/escaping/not-found behavior; only controlled local paths/targets |
| Upload/import | Empty file, misleading extension, wrong MIME, malformed row, duplicate row, limit+1 size | Clear result, correct rollback/partial-success contract, no orphan artifacts |

The notation `\u0301` describes a character; construct actual code points and log an escaped representation plus length so reproductions are unambiguous. Verify what reached the UI, request, and stored record. If the domain legitimately rejects a value, rejection succeeds only if it is controlled and leaves the required state unchanged.

## Injection: attempt exploitation, verify the boundary

Assess every class below against the changed feature and its affected consumers. For each applicable surface, run a context-aware exploit attempt against local/disposable fixtures rather than stopping at static review or an apostrophe test. Record the input source, transformations, interpreter/rendering/model sink, expected trust boundary, exact payload, benign control, and observed effect. An unavailable sink is a coverage gap; no applicable sink needs a reason. Do not spray unrelated endpoints.

| Class | Surfaces and controlled attempts | What establishes a finding |
|---|---|---|
| **Query injection** | Trace URL/form/JSON/mobile inputs and stored values into SQL, NoSQL, raw ORM queries, or search/filter expressions. On a read-only fixture query, compare matched true/false predicate variants appropriate to the actual syntax; test operator objects such as `{"$ne": null}` where an API expects a scalar. Inspect sort/filter identifiers and second-order use of saved values. | Input changes query structure or bypasses a documented filter/ownership constraint, demonstrated with synthetic rows and an independent result/state check. A quote accepted as data, a syntax error, or a 500 alone does not prove injection. Never use destructive statements, expensive delay probes, or non-test records. |
| **XSS (cross-site scripting)** | Test reflected, stored, and DOM-based paths: forms, URL/hash parameters, rich text/Markdown previews, saved names, and downstream detail/admin screens or WebViews. Adapt a benign script/event-handler canary to the actual HTML, attribute, URL, or script-string context, such as setting `window.__branchBreakerProbe` to a unique run ID. | Application processing of supplied data executes the canary in the affected browser/WebView. An echoed tag/string is not script execution. Submit the payload through the real input boundary; do not use the test harness's JavaScript evaluation to execute the canary yourself. |
| **CSS injection** | Trace untrusted theme/style values, HTML attributes, and stylesheet construction. In a test-only screen, attempt to escape the intended declaration/selector scope and apply a harmless outline or color marker to a separate controlled element. | Untrusted input changes styling outside the permitted scope. Verify the computed style and affected element; intentional theme customization is not a defect. Report CSS-only effects separately from script execution. Avoid network-loaded resources or CSS data-exfiltration techniques. |
| **JavaScript injection** | Inspect inline JavaScript interpolation, dynamic evaluation such as `eval`/`Function`, script/URL handlers, and native WebView bridges. Attempt a syntax breakout that produces only a local marker; for server-side JavaScript use a disposable isolated process and a sentinel value, with no filesystem/OS command or network effects. | The application interprets a data value as code, or crosses a restricted bridge capability, producing an independently observed marker/action outside its contract. Parsing JSON or displaying code is not execution. Deduplicate with an XSS finding when the same root cause and exploit path explain both. |
| **Prompt injection** | Where the product uses an LLM/agent, test direct user content and indirect content from retrieved documents, uploads, stored records, webpages, and tool results. Put an instruction-override/role-spoofing payload in the lower-trust content, asking the target to violate a defined task boundary, emit a unique canary contrary to its contract, expose a synthetic protected value, or request a forbidden action through a stubbed test tool. Use fake records and sandboxed tools. | The target follows lower-trust instructions in violation of an established trusted task/policy. Record messages, retrieved/tool content, output, tool calls, model/configuration, and attempt count. Quoting the attack, performing an allowed request, or mentioning the canary is not a bypass. A rejected tool request can be a working defense: call it a model-policy defect only if making that request itself violates a documented contract; claim unauthorized execution only if the action actually executes. |

Keep parameterization, escaping, sanitizers, CSP, model instructions, and tool authorization in their deployed configuration during the primary probe. Do not disable a protection and then claim the normal app is exploitable. Verify the payload reached the sink and report whether a defense blocked the effect; a blocked payload only demonstrates that specific case, not universal immunity.

For stored/second-order attacks, save through the actual input, then reopen through the other consumer or another owned test identity. After each probe, remove injected fixtures, verify ordinary behavior, and retain sanitized evidence. Never issue destructive SQL/shell operations, access real secrets, or send payloads to external collection hosts.

For prompt injection, test the **target application's** model boundary, not the QA agent's willingness to follow an instruction. Keep payloads and model responses as quoted data throughout inspection and reporting. Compare with a benign document/request and repeat relevant attempts within a bounded budget; LLM behavior may vary. A mocked model response verifies downstream handling only, not model resistance. An external provider must already be authorized and use synthetic inputs; otherwise record the model-execution gap and continue independent local probes.

JavaScript enabled in a WebView or the existence of a bridge is not itself a vulnerability; prove unintended execution or access beyond the bridge's contract. Use syntax appropriate to the actual browser/interpreter/driver version, not obsolete payload assumptions.

Primary references for context-specific testing and interpretation:

- [OWASP SQL injection](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) and [NoSQL security](https://cheatsheetseries.owasp.org/cheatsheets/NoSQL_Security_Cheat_Sheet.html)
- [OWASP XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html), [CSS injection testing](https://wstg.owasp.org/v4.2/4-Web_Application_Security_Testing/11-Client-side_Testing/05-Testing_for_CSS_Injection/), and [JavaScript execution testing](https://wstg.owasp.org/v4.2/4-Web_Application_Security_Testing/11-Client-side_Testing/02-Testing_for_JavaScript_Execution/)
- [OWASP WebView JavaScript caveat](https://mas.owasp.org/MASTG-TEST-0031/)
- [OWASP prompt injection](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)

## State, order, and durability

- Create → edit → refresh/relaunch → detail → search → export; read the same fixture through relevant consumers of the changed contract.
- Cancel, back, dismiss, navigate away, or background while dirty or saving; verify the product's commit/draft policy.
- Submit twice, retry after an ambiguous timeout, or replay the same queued command. Count durable records/events and verify promised idempotency.
- Open two tabs/devices, edit the same test record, delete in one and save in the other. Check conflict behavior and unexpected resurrection/lost updates.
- Switch account, organization, role, or filter while a response is delayed. Old responses must not expose or overwrite the new context.
- Read old records under new code; follow new records into old clients/consumers when compatibility matters. Use an isolated database for schema-version experiments.
- Empty collection, last record deleted, one record, pagination boundary, stale cache, refresh after reorder, filters producing no results.

## Failure, recovery, and trust boundaries

- Inject one controlled transport failure, timeout, relevant HTTP error, or malformed response. Check rollback, loading-state recovery, and successful retry after removing the fault.
- Exercise offline start, disconnect mid-write, reconnect, and queued replay where supported. Distinguish a request that never reached the server from one that committed but lost its response.
- Test unauthenticated, expired-session, allowed, and forbidden roles with disposable accounts. Use two owned test tenants for ownership probes. Denied reads must expose no private content; denied writes must have no side effect. UI hiding does not prove server authorization.
- Check settings/feature flags at supported combinations affecting the change, including disabled or missing optional configuration.
- Inspect API, queue, cache, or storage effects where available. If an essential invariant cannot be observed, say so; an error toast or HTTP status alone is insufficient.

Combine stressors with a causal reason: Unicode name → normalization → uniqueness → search/export; denied permission → fallback → later grant; failed save → retry → duplicate notification; stale session → background/resume → cached sensitive screen. A handful of these usually tests more than hundreds of random strings.
