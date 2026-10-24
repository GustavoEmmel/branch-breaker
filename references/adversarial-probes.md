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

For interpolation risks, use harmless local canaries in the relevant context. Do not mistake accepted punctuation for an injection vulnerability. Prove an unintended effect inside the authorized test environment before reporting one. Never issue destructive SQL, shell operations, or payloads that beacon to external hosts.

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
