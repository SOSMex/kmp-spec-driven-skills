# Example: higher-risk offline shared checklist

## Request

Allow two devices to update a shared checklist while one is offline, then reconcile when connectivity returns without repeating completed actions.

## Design classification

- Multi-device coordination, persistence, offline reconciliation, ordering, and duplicate delivery are affected.
- A feature spec defines the intended user behavior.
- An RFC is required before implementation to agree on authority, revisions, conflict semantics, retry, and rollback.
- An ADR follows only if the accepted proposal creates a durable synchronization decision.

## Required design

- Stable checklist, item, actor, device, and operation identifiers.
- Explicit server authority and per-entity or operation revision.
- Idempotent commands and deterministic duplicate handling.
- Defined outcomes for stale updates, concurrent edits, unknown operations, incompatible clients, cancellation, and permanent rejection.
- A local queue that preserves intent without treating delivery as confirmation.
- Presentation states for pending, reconciled, rejected, offline, retrying, and incompatible.

## Ownership

- Reconciliation invariants and operation outcomes: pure shared rules.
- Versioned messages: contract boundary independent from domain types.
- Queue, persistence entities, and mappings: data layer.
- Authorization, ordering, revisions, and canonical acceptance: server.
- Connectivity and lifecycle adapters: thin platform source sets.

## Required evidence

1. Pure tests for ordering, duplicate operations, stale revision, concurrent edits, rejection, and incompatible versions.
2. Contract compatibility tests for current and supported prior clients.
3. Repository and server integration tests for disconnect, retry, and reconciliation.
4. Android and iOS compilation and runtime flows.
5. Physical two-device evidence with one device disconnected, local continuation, reconnection, and a coherent final state.

Passing JVM tests proves the reconciliation rules are automated-tested. It does not close the physical two-device gate.
