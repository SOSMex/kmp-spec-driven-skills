# Contributing

Contributions are welcome when they make Kotlin Multiplatform work safer, clearer, or easier to verify.

## Good contributions

- A concrete KMP failure mode plus a rule that prevents it.
- A clearer decision boundary between a task, spec, RFC, and ADR.
- A target-aware verification technique that avoids overstating parity.
- A realistic evaluation case with observable expected invariants.
- A correction grounded in official Kotlin, Gradle, Android, Apple, or agent-skill documentation.

## Scope

Keep the repository focused on agent workflows. A Gradle plugin, project generator, full application template, or CI product should begin as a separately discussed proposal.

Skills must not assume one architecture, dependency injection framework, backend, or UI toolkit. They may provide a reference layering model, but must first discover and respect the target repository's own instructions.

## Change workflow

1. Describe the failure mode or outcome.
2. Update the smallest relevant skill or reference.
3. Add or update an evaluation case.
4. Run `python3 scripts/validate.py`.
5. Confirm Markdown links resolve and no private data or credentials are present.
6. Open a focused pull request describing the behavior change and validation.

## Writing guidance

- Use direct, imperative instructions.
- Explain non-obvious KMP constraints, not general programming concepts.
- Keep vendor-specific installation notes separate from the core workflow.
- Use exact evidence language: compiled, automated-tested, emulator-tested, physically-tested, store-submitted, or released.
- Treat RFCs as proposals and ADRs as durable decisions; neither replaces a feature specification.
