# Public learning sources and attribution

Research date: 2026-10-27. This is an original extension of Branch Breaker informed by public materials for **Full Stack Testing: A Practical Guide for Delivering High Quality Software**, by **Gayathri Mohan**, first edition, O'Reilly, 2022. It is not a reproduction of the book or a claim to have accessed every chapter or every public discussion.

## Book and author material actually consulted

| Public source | Accessible material | Influence on Branch Breaker |
|---|---|---|
| [O'Reilly first-edition page](https://www.oreilly.com/library/view/full-stack-testing/9781098108120/) | Publisher description and public contents | Breadth of testing dimensions; select beyond functional happy paths |
| [Official free chapter](https://www.thoughtworks.com/content/dam/thoughtworks/documents/books/bk_full_stack_testing_free_capter_en.pdf) | Chapter 1 excerpt, explicitly identified as such by the publisher | Quality across the stack and lifecycle; assess ten dimensions while staying branch-focused |
| [Seven guiding principles in testing](https://www.thoughtworks.com/insights/blog/testing/seven-guiding-principles-testing) — Mohan, 2021 | Public author article | User outcomes, early feedback, prevention, and evidence useful to a developer |
| [Why full-stack testing matters](https://www.thoughtworks.com/en-sg/insights/podcasts/technology-podcasts/why-full-stack-testing-matters) — Mohan interview, 2022 | Public transcript | Architecture-dependent test boundaries, trustworthy fixtures, and exploratory discoveries that can become regression checks |
| [Threat Modeling Guide for Software Teams](https://martinfowler.com/articles/agile-threat-modelling.html) — Mohan and Jim Gumbley, 2025 | Later public coauthored article, separate from the 2022 book | Trace relevant dataflows/trust boundaries and turn risks into concrete abuse probes |

The [2026 second edition](https://www.oreilly.com/library/view/full-stack-testing/9798341636934/colophon01.html) is separate. Its public listing was identified, but its AI-era chapters are not represented here as read content from the first edition. Existing prompt-injection guidance has its own OWASP sources in the adversarial guide.

The [author's publications page](https://gayathri-mohan.com/publications/) and publisher's public preface were also checked for companion material. No official author companion repository was verified; no reader repository is presented as official, and tool exercises behind full-book access were not inspected. The publisher listing is used for edition metadata when the author's early-access wording differs.

## Supporting implementation references

- [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html), Ham Vocke: focused layers, contracts, and selective end-to-end coverage. This is a supporting article, not a chapter authored by Mohan.
- [Pact introduction](https://docs.pact.io/): scope of consumer/provider HTTP and message contract checks. No requirement to install Pact.
- [W3C WAI Easy Checks](https://www.w3.org/WAI/test-evaluate/preliminary/): initial keyboard, focus, labels, errors, and visual-accessibility checks; these do not constitute a full conformance assessment.
- [Grafana k6 thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/): explicit metric criteria for performance checks. Documentation examples are not universal product budgets; no requirement to install k6.

Specific probe recipes, verdict integration, local-only defaults, evidence fields, and regression-placement recommendations are Branch Breaker's own engineering adaptations. Public source availability is not evidence that a target application passed a test. Reuse current project tools and consult their version-appropriate documentation when execution requires it. No book text, diagrams, or companion implementation is bundled.

## UX/UI extension sources

Consulted 2026-10-29 for the separate user-perspective extension; these are not attributed to Mohan's book. The task walkthrough, evidence classes, and report integration are original Branch Breaker adaptations.

| Primary source | Material consulted and application |
|---|---|
| [NN/g: Ten Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) | Public article; questions about state visibility, familiar language, user control, consistency, recognition, and recovery |
| [NN/g: How to Conduct a Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/) | Public article; contextual evaluation and justified tradeoffs, with expert inspection distinguished from research with users |
| [W3C: Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/) | Introduction and relevant pattern/objective index of the public Working Group Note; clear purpose/controls, reduced memory burden, understandable language, and retained work. Supplemental guidance, not mandatory WCAG conformance criteria; not every pattern was reviewed |
| [Apple HIG: Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) | Public Markdown body linked by the page; contextual status and interruption, with accessible and actionable feedback |
| [Apple HIG: Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | Relevant hierarchy, adaptation, and safe-area sections of the linked public Markdown body; legibility, grouping, and reachable controls, without prescribing Apple styling for other products |
| [Android: Principles of Navigation](https://developer.android.com/guide/navigation/principles) | Public page; predictable navigation, distinguishing Back/Up and respecting deep-link context where applicable |

These sources inform questions and evidence collection, not a claim of universal best design or knowledge of a particular product's users. Current platform criteria should be checked when an actual finding depends on them. No source diagrams, templates, or implementation code are bundled.
