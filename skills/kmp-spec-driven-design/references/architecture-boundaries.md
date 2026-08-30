# Architecture boundaries

Use the target repository's architecture when it is explicit. Otherwise, use this as a reference model rather than a mandatory module layout.

## Placement questions

Ask in order:

1. Is the behavior deterministic and valid for every target? Prefer `commonMain`.
2. Does it depend on APIs available only to a subset of targets? Prefer the narrowest valid intermediate source set.
3. Does it integrate a platform capability such as lifecycle, push, secure storage, deep links, billing, or accessibility APIs? Keep the adapter in the platform source set and expose a small shared boundary.
4. Is it a wire or persistence representation? Map it at the boundary; do not let it define the domain model.
5. Is it UI state or navigation? Keep it outside pure business rules even when the presentation is shared.

Kotlin's official guidance is that `commonMain` compiles to all declared targets and cannot use platform-specific APIs. Platform and intermediate source sets should exist because their target set requires them, not as miscellaneous folders.

## Reference layering

```text
domain / business rules       <- no UI, transport, persistence, or platform APIs
contract / wire compatibility <- versioned messages and protocol outcomes
data / adapters               <- mapping, persistence, caches, and transports
shared presentation           <- state, intents, effects, and shared UI
platform hosts                <- lifecycle and native integrations
server                        <- authorization, orchestration, and persistence adapters
```

Useful dependency tests:

- Can the domain compile without Android, Apple, Compose, serialization, database, and network dependencies?
- Can a transport schema evolve without forcing the domain to use nullable or optimistic defaults?
- Can shared presentation be tested without launching a platform host?
- Is every `expect` declaration a real platform boundary rather than a shortcut around design?
- Does each platform host delegate deterministic behavior to shared code?

## Contract boundaries

When data crosses devices or processes, specify:

- protocol version and compatibility policy;
- stable semantic identifiers;
- unknown enum and unknown message handling;
- canonical timestamps and local elapsed-time behavior;
- entity revision or idempotency keys where races are possible;
- authorization and ownership rules;
- which side is authoritative;
- retry, duplicate, reordering, and partial-delivery outcomes.

Unknown values must degrade to an explicit unsupported or unknown state. They must not become a successful, safe, paid, authenticated, or otherwise optimistic default.
