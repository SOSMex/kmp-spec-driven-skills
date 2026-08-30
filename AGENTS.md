# Agent instructions

This repository contains reusable, vendor-neutral skills for Kotlin Multiplatform delivery.

Before editing:

1. Read `README.md` and `CONTRIBUTING.md` completely.
2. Inspect the affected skill, its directly linked references, templates, examples, and evaluation cases.
3. Keep instructions portable across agent vendors and KMP project shapes.
4. Preserve the distinction between requirements, proposals, accepted decisions, implementation, and evidence.
5. Never hardcode project-specific modules, Gradle tasks, credentials, accounts, or private repository facts into a reusable skill.

Every change must keep `SKILL.md` concise, place extended detail one link away under `references/`, and add or update an evaluation case when behavior changes. Run:

```bash
python3 scripts/validate.py
```

Do not claim adoption, platform parity, physical validation, store submission, release, or competition recognition without independently reproducible evidence.
