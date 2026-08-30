# Example: low-risk shared preference

## Request

Add a user preference that controls whether completed checklist items remain visible. Android and iOS already use the same shared presentation state and local settings repository.

## Design classification

- Outcome is clear and local.
- No new sensitive data, service, contract, migration, or platform API.
- Existing settings ownership and dependency direction remain unchanged.
- RFC: not warranted.
- ADR: not warranted.

## Ownership

- Preference model and deterministic filtering rule: shared business or presentation source set, following the repository's existing boundary.
- Persistence mapping: existing shared data adapter.
- Android and iOS hosts: no behavior change.

## Degraded behavior

If stored data is absent or unreadable, use the product's documented default and expose the normal settings error behavior. Do not silently convert a corrupt value into an unrelated preference.

## Tasks

1. Add the preference and boundary-case tests.
2. Map it through the existing settings repository.
3. Add reducer or presentation tests for visible and hidden completed items.
4. Compile both targets and exercise the setting on Android and iOS.

## Truthful handoff

If shared tests pass and both targets compile, report `Automated-tested` for the shared rule and `Compiled` for each target. Do not call the preference runtime-parity complete until it is observed on both platform surfaces.
