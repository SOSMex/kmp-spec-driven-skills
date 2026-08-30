# Testing matrix

Select checks according to the changed behavior and repository instructions. Do not run every category mechanically.

| Area | Typical evidence | Failure paths to include |
| --- | --- | --- |
| Pure shared rules | `commonTest` or module tests | boundaries, invalid inputs, unknown values, time and locale |
| Contracts | serialization and compatibility tests | unknown enum, old/new version, missing field, duplicate message |
| Data and mapping | repository, mapper, cache, and transport tests | stale cache, offline, partial response, retry, cancellation |
| Shared presentation | reducer/store/view-model tests and UI tests | loading, empty, stale, error, retry, duplicate effect |
| Android | target compilation, unit/instrumented tests, emulator/device flow | lifecycle, process recreation, deep link, permissions, accessibility |
| iOS | target compilation, XCTest or repository checks, simulator/device flow | lifecycle, deep link, permissions, accessibility, native bridge |
| Server | unit/integration/contract tests | authorization, concurrency, idempotency, rollback, incompatible client |
| Multi-device | synchronized runtime evidence | reconnect, reordering, duplicate delivery, clock skew, one-device loss |
| Distribution | signed artifact and store evidence | signing, installability, review state, public version identity |

## Risk-proportional selection

Low-risk shared logic normally requires focused tests plus affected target compilation.

Platform integration requires the relevant platform runtime evidence in addition to shared tests.

Contracts, persistence, auth, privacy, billing, realtime, offline reconciliation, and safety-sensitive behavior require both automated failure-path coverage and the environment-specific evidence named by the accepted plan.

## Evidence capture

Record:

- repository revision and dirty state;
- exact task, workflow, or manual procedure;
- target and environment identity;
- pass, failure, skip, or unavailable result;
- artifact paths or stable links;
- date for live services or store state;
- any difference between local and CI results.

Prefer machine-readable test output and durable CI links. Screenshots support visible UI claims but do not replace logs or tests for hidden behavior.
