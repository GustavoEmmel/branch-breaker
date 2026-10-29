# Challenge the change from the user's perspective

Use this guide for affected user journeys on web, mobile web, and native apps, including backend changes that alter visible behavior. Review the branch and its plausible downstream effects, not the entire product. Combine this walkthrough with the existing functional, visual, and accessibility checks instead of duplicating them. No extra interview or approval stage is required.

## Establish who benefits and what changes for them

Infer the intended user, goal, context, and success from requirements, existing journeys, product language, available research, and real consumers. State unsupported assumptions. Use relevant role, familiarity, device, language, or accessibility differences; do not invent personas, research participants, analytics, or a universal "average user."

Describe the journey before and after in a few steps: entry → decision/input → action → feedback → useful outcome. Verify the base when claiming a regression; otherwise label the comparison as unverified. Ask:

- What user problem does this solve, and can the user recognize the benefit? A technically correct feature can still introduce an unnecessary decision, prerequisite, or detour.
- Does the change fit the user's existing mental model and vocabulary? Can a returning user still find the task? Does a first-time user have the information needed to act?
- What effort, uncertainty, loss of control, or risk does it add? Does that burden serve a known purpose, such as preventing an irreversible mistake or protecting an account?
- Does the outcome help the next step or another affected role? Follow changed data/defaults/status into the next screen, notification, export, or device where relevant.

Challenge an approved requirement when its user tradeoff is unclear, but report the question and evidence instead of rewriting the product goal. Missing research is uncertainty, not proof that nobody needs the feature. Extra clicks or confirmation are not automatically bad; judge them against task complexity, consequences, and established safeguards.

## Walk the journey without privileged knowledge

Start at the user's normal entry point, not a route known only from source. At meaningful decisions, record what the screen communicates, the action it appears to offer, the observed result, and whether the user can recognize success. Do not claim you know what real users thought. If recovery requires a hidden route, developer console, database inspection, or a fact absent from the UI, that is not successful user recovery even when those tools help diagnose it.

Select probes for the change rather than applying every row to every screen:

| Lens | Challenge and evidence |
|---|---|
| Entry and orientation | Can the intended role find the task from normal navigation and tell where they are? Check affected links, back behavior, and return paths. Preserve context, filters, and progress when promised. |
| Words and decisions | Do labels and content explain the actual consequence, units, required input, and scope? Look for ambiguous primary actions, unexplained jargon, conflicting instructions, or defaults that silently change the user's intention. |
| Task effort and control | Check repeated entry, forced rework, irrelevant decisions, and unexpected navigation. Try back, cancel, edit, undo, or a supported alternative. Preserve intentional confirmation and security controls. |
| State and trust | Exercise relevant empty, loading, partial, success, disabled, and permission states. Can users distinguish waiting, saved locally, queued, and completed? Compare feedback with actual durable state; a success message after a failed write is a concrete defect. |
| Mistakes and recovery | Make a plausible mistake; inspect whether feedback identifies the problem and offers an actionable next step without losing valid work. Retry after a controlled failure; verify feedback and the saved outcome. Use existing bounded failure fixtures. |
| Hierarchy and consistency | Inspect actual rendered content: is the next action distinguishable, is necessary information grouped and readable, and do interactive elements look/behave consistently? Compare affected shared components, design tokens, and platform conventions. Consistency violations need a user consequence or a clearly established design contract. |
| Layout and input | Exercise relevant supported sizes, long/localized content, text scaling, keyboard/focus, and touch input. Look for clipping, obscured controls, overflow, misleading truncation, crowded targets, and content hidden by dialogs or the on-screen keyboard. Use applicable platform guidance rather than one universal pixel threshold. |
| Choice and consent | Verify that labels, defaults, exits, and emphasis reflect the real action and let users make an informed choice. Test unexpected opt-ins, hard-to-reverse actions, or concealed consequences with synthetic fixtures; describe the observed behavior without inventing legal claims. |

On native mobile, select relevant platform back/dismiss behavior, safe areas, keyboard presentation, permission denial, lifecycle interruptions, and touch/assistive interaction using the mobile execution guide. A desktop screenshot or browser mobile viewport cannot validate those native behaviors. On web, include responsive and keyboard interactions where the change can affect them. Do not require every device class for an unrelated change.

Use existing components/design-system guidance as the starting point for visual review, not a mandate to preserve an intentional redesign. Judge spacing, typography, color, density, and motion by hierarchy, legibility, consistency, and task impact. Avoid imposing a personal style, fashionable layout, or arbitrary beauty score. A visual baseline helps attribute a change; its absence does not prevent demonstrating an overlapping control or misleading label. A screenshot can establish visible clipping; it cannot establish successful navigation, screen-reader announcements, or persistence.

## Turn critique into useful evidence

Keep three kinds of output distinct:

| Classification | What supports it | How to report it |
|---|---|---|
| Confirmed UX/UI defect | Executed interaction or directly observed rendering with a reproducible failure and an independently justified expected outcome: user task, clear UI promise, established contract, or applicable criterion | Use the normal finding format and impact-based severity. Include role, journey step, exact label/action, state, viewport/device, and screenshot/trace plus outcome where relevant. No exception or crash is required for a serious usability defect. |
| Heuristic concern / improvement opportunity | A concrete observed friction or inconsistency with a plausible but unverified effect on comprehension, effort, or choice | Describe evidence, relevant heuristic/context, uncertainty, suggested improvement, and a focused validation method. Keep outside confirmed defects and severity counts; it alone does not trigger FAIL. |
| Product hypothesis / open question | An assumption about need, value, preference, or an unresolved tradeoff | State the assumption, why this change raises it, and what evidence would resolve it. Do not claim conversion, satisfaction, churn, or preference improvements without measurements. |

Heuristics are diagnostic aids, not absolute product requirements. Expert inspection does not replace research with representative users. Lack of a user study alone is not an execution blocker; record it as a limitation unless the requested scope required that study. Missing actual UI execution for a selected interaction probe is a real coverage gap. Source-only concerns remain unverified; supplied screenshots support only the states they show.

Prefer a few material observations over cosmetic nitpicks. Suggest the smallest change that addresses the user's difficulty and how to check it: a specific behavioral assertion, a comparable walkthrough, or a targeted usability task when human understanding is uncertain. Do not invent an automated assertion for whether people like a design. Do not implement redesigns or add approval gates during QA. Deduplicate with accessibility/functional findings while retaining their user impact.

Finish with a brief user-perspective assessment: intended benefit, observed ability to complete the task, added friction/tradeoffs, and unresolved assumptions. The execution verdict remains evidence-based; it is not a certification of "best UX." Primary sources and their scope are listed in [learning sources](learning-sources.md).
