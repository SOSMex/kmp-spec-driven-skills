# RFC and ADR decision guide

## Artifact roles

| Artifact | Question it answers | State |
| --- | --- | --- |
| Task | What small, accepted work should be performed? | Actionable |
| Spec | What behavior and outcome are required? | Product contract |
| Plan | How will the accepted behavior be delivered and verified? | Implementation intent |
| RFC | Should we agree to this broad or risky proposal? | Proposed until resolved |
| ADR | Which durable technical choice was accepted, and why? | Proposed or accepted explicitly |
| Verification report | What was actually proven? | Evidence, not intent |

## Decision router

Use a task alone when the behavior is already clear, local, reversible, and low risk.

Use a spec and plan when the change introduces normal product behavior across multiple files or layers but does not require broad architectural agreement.

Add an RFC before implementation when the proposal materially affects one or more of:

- realtime or multi-device coordination;
- authentication or authorization;
- privacy, sensitive data, retention, or deletion;
- billing or entitlements;
- persistence schema or migration;
- versioned external contracts or compatibility;
- offline reconciliation or conflict resolution;
- a new external service, framework, or background process;
- a costly operational dependency;
- a safety-sensitive default or failure mode.

Create or update an ADR only after the durable choice is accepted. Typical ADR subjects include dependency direction, source-of-truth ownership, persistence technology, synchronization semantics, contract-version strategy, and platform-integration boundaries.

## Guardrails

- An RFC does not authorize implementation by itself.
- An ADR does not define user acceptance criteria.
- Marking an ADR `Accepted` requires named decision evidence according to the repository's governance.
- A merged implementation is not proof that the design decision was intentionally accepted.
- If a proposal is easily reversible and local, document it in the plan instead of creating ceremony.
