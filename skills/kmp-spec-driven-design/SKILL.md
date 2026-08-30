---
name: kmp-spec-driven-design
description: Turn an accepted feature outcome into an implementation-ready Kotlin Multiplatform design. Use before tasks or code when work spans shared and platform source sets, modules, contracts, persistence, offline behavior, backend coordination, or requires deciding whether an RFC or ADR is warranted.
---

# KMP spec-driven design

Design the smallest coherent cross-platform slice before implementation.

## Inputs required

- Repository instructions and contribution rules.
- Accepted outcome, boundaries, acceptance criteria, and non-goals.
- Relevant existing modules, source sets, contracts, tests, RFCs, and ADRs.
- Supported targets and any required runtime or physical-device evidence.

If the outcome or acceptance criteria are materially ambiguous, stop and clarify them before designing.

## Workflow

1. **Discover the project shape.** Inspect settings, module build files, source sets, target declarations, existing dependency direction, and nearby tests. Do not assume module names or Gradle tasks.
2. **Define the vertical slice.** State the user-visible outcome, entry point, success path, degraded paths, and explicit non-goals.
3. **Classify the decision risk.** Use [the RFC and ADR decision guide](references/rfc-adr-decision-guide.md). A spec defines behavior; an RFC seeks agreement on a risky proposal; an ADR records an accepted durable choice.
4. **Assign ownership.** Put deterministic behavior in the broadest valid shared source set. Keep platform integrations thin. Use [the architecture boundary guide](references/architecture-boundaries.md) while respecting stricter repository rules.
5. **Design contracts and state.** Define versioning, unknown-value behavior, concurrency/idempotency rules, authoritative timestamps, error outcomes, and compatibility boundaries when data crosses a process or device boundary.
6. **Design degraded behavior.** Cover loading, offline, stale, partial, retry, duplicate delivery, cancellation, and incompatible-version behavior where relevant.
7. **Build a target-aware verification plan.** Name the behavior to prove on shared logic, each supported platform, backend, and required device combination. Discover actual tasks during implementation; do not invent them here.
8. **Produce implementation inputs.** Update or propose the necessary spec, plan, task breakdown, RFC, ADR, and verification matrix. Keep requirements, proposals, decisions, and evidence visibly distinct.

## Required output

Report:

- outcome and non-goals;
- risk classification and rationale;
- module/source-set ownership;
- dependency and contract boundaries;
- state and degraded-path model;
- ordered vertical-slice tasks;
- verification matrix by target;
- open decisions and named owner approvals.

Use the repository's own artifact format when it exists. Otherwise adapt the templates in [`../../templates/`](../../templates/).

## Stop conditions

Do not implement when:

- a behavior-changing question lacks an accountable owner;
- a risky proposal still requires RFC agreement;
- a durable decision is presented as accepted without evidence;
- privacy, authorization, billing, safety, or compatibility behavior is unspecified;
- platform support is claimed without a verification path.

Do not create an abstraction, framework, intermediate source set, or service unless it protects a demonstrated boundary or requirement.
