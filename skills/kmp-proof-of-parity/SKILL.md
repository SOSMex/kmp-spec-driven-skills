---
name: kmp-proof-of-parity
description: Verify an implemented Kotlin Multiplatform change across shared logic, Android, iOS, backend, degraded states, and required device combinations. Use before pull-request readiness, release claims, or statements that behavior has cross-platform parity.
---

# KMP proof of parity

Report the strongest evidence actually observed for each claimed behavior and target.

## Inputs required

- Accepted spec, plan, tasks, and relevant RFCs or ADRs.
- Changed files and affected module/source-set graph.
- Supported targets and explicit acceptance criteria.
- Available build environment, emulators/simulators, devices, services, and test accounts.

## Workflow

1. **Define the claim.** List each behavior being presented as complete and the targets, states, and device combinations it affects.
2. **Inspect the implementation path.** Trace shared rules, mappings, platform adapters, backend behavior, and UI surfaces. Do not infer coverage from filenames.
3. **Discover executable checks.** Inspect Gradle tasks, Xcode schemes, scripts, CI, and repository instructions. Use the real project tasks rather than a fixed command list.
4. **Run the smallest complete automated matrix.** Cover pure shared behavior, contract compatibility, mapping, platform compilation/tests, backend tests, and static checks as applicable. Use [the testing matrix](references/testing-matrix.md).
5. **Exercise runtime behavior.** Validate the relevant happy path and degraded paths on each platform. For multi-device, lifecycle, push, deep-link, platform accessibility, or hardware-sensitive behavior, gather the required real-device evidence.
6. **Reconcile results with acceptance criteria.** Record failures, unavailable environments, contradictory evidence, and untested states instead of resolving them by inference.
7. **Assign evidence levels.** Use [the evidence vocabulary](references/evidence-levels.md) independently for every target and claim.
8. **Produce the handoff.** Report exact commands or workflows, results, artifacts, remaining gates, and the narrowest truthful readiness statement.

## Required output

Use a matrix with:

- behavior or acceptance criterion;
- target/environment;
- evidence level;
- command, test, screenshot, log, or distribution link;
- result;
- residual gate and owner.

Also report changed scope, regressions checked, unavailable evidence, and whether the pull request is reviewable. Use [`../../templates/verification-report.md`](../../templates/verification-report.md) when the repository has no format.

## Claim rules

- Compilation proves compilation only.
- A shared test does not prove platform UI or integration behavior.
- An Android emulator does not prove iOS behavior.
- A simulator does not prove push delivery, camera, Bluetooth, background execution, or other device-sensitive behavior.
- Two processes on one machine do not automatically prove a physical two-device flow.
- Uploading an artifact does not prove installation or runtime behavior.
- Store submission is not release.
- A public health endpoint does not prove authenticated or private routes.

When the required environment is unavailable, report the gate precisely and stop the broader claim. Never manufacture parity from partial evidence.
