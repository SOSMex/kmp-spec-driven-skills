# Example: from outcome to truthful evidence

This walkthrough shows how the two skills cooperate without treating a design proposal as implementation evidence.

## Accepted request

> Let a signed-in user save a small checklist on one device, continue reading it offline, and see the same content on Android and iOS. Concurrent editing and multi-device synchronization are outside this slice.

## 1. Run `kmp-spec-driven-design`

The design skill first inspects the repository instead of assuming module names, source sets, or Gradle tasks. A good result should establish:

- the observable outcome and the explicit exclusion of concurrent editing;
- the repository's existing ownership for the checklist model, persistence adapter, and shared presentation;
- the product-defined outcome for missing, stale, unreadable, and offline data;
- whether persistence migration or sensitive data changes make an RFC necessary;
- an ordered vertical slice and target-aware verification matrix;
- any decision that still needs an accountable owner.

If the repository already has a local persistence boundary and the change is reversible, an RFC or ADR may be unnecessary. If the request changes a durable persistence contract or migration strategy, the skill should identify the corresponding decision gate rather than silently choosing one.

## 2. Implement against the accepted artifacts

Implementation is intentionally outside the design skill. The coding agent or contributor should follow the accepted spec, plan, tasks, RFCs, and ADRs in the target repository.

The implementation may place deterministic checklist behavior in shared code and keep Android or iOS storage integration behind thin platform adapters. That placement is evidence only after inspecting the actual repository; it is not a universal module prescription.

## 3. Run `kmp-proof-of-parity`

Assume the resulting evidence is:

- shared checklist and mapping tests pass;
- the Android and iOS targets compile;
- the checklist is exercised successfully on an Android emulator, including an offline read;
- iOS is not launched;
- no physical devices or store builds are involved.

The verification skill should produce a matrix similar to this:

| Claim | Target | Highest evidence | Remaining gate |
| --- | --- | --- | --- |
| Checklist and mapping rules | Shared test environment | `Automated-tested` | None for the covered pure behavior |
| Checklist runtime flow | Android emulator | `Emulator-tested` | Physical-device evidence only if the accepted plan requires it |
| Checklist runtime flow | iOS | `Compiled` | Simulator or device runtime observation |
| Offline read | Android emulator | `Emulator-tested` | iOS offline runtime observation |
| Public availability | Android and iOS | No distribution evidence | Store submission and independent release verification |

## Truthful handoff

> Shared checklist behavior is automated-tested, Android is emulator-tested for the covered online and offline paths, and iOS compiles. iOS runtime parity, physical-device evidence, store submission, and release remain unproven.

This statement is narrower than "the feature is fully cross-platform," but it is reproducible and tells the next contributor exactly what to validate.
