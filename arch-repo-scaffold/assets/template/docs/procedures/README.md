# Procedures

One file per operational procedure: what triggers it, what it reads and writes, and every step
in order, written so an engineer can build it without asking questions. This README is the index
**and** the place that explains how the procedures fit together.

## What goes here

- **`00-interfaces.md`**: every external call the procedures make, with real payloads and
  responses. Read before implementing any procedure.
- **`NN-verb-object.md`**: one procedure per file, e.g. `03-create-hosted-cluster.md`,
  `13-upgrade-hosted-cluster-workers.md`. Numbers are assigned once and never reused or
  reordered; the index below groups them by layer.
- This **README**: the index tables, a short "shape of it" diagram, and cross-cutting rules that
  apply to every procedure.

## What does not go here

- Code. Procedures describe behaviour; implementation lives in the implementation repos.
- Component internals (a controller's model and reconcile loop). Those go in a spec at `docs/`
  root; the procedure links to it.
- Rejected or undecided flows: `../drafts/`.

## How to write a procedure

Every procedure file follows this shape:

```markdown
# 04 :: Update NodePool

**Animation:** [`../animations/04-update-nodepool.html`](../animations/04-update-nodepool.html)

| | |
|---|---|
| **Trigger** | Customer, changing a worker count up or down |
| **Workflow id** | `update-nodepool-<cluster>-<node-type>`, one in flight per pair |
| **Runs on** | Git, then the hub's queue to watch convergence |
| **Writes** | Git only |
| **Ends at** | ArgoCD synced. **Not** at nodes ready. |

> One sentence on the single most important thing about this procedure.

---

## 1 :: Purpose
## 2 :: Inputs
| Field | Type | Required | Notes |
|---|---|---|---|
| `desired_total` | int | ✅ | **Absolute total**, never a delta |

## 3 :: Process flow
| # | Phase | Runs on | Action | On failure |
|---|---|---|---|---|
| 1 | `validating` | brain | `desired_total >= 3`, cluster exists | Terminal |
| 2 | `reading-current` | git | Read current replicas in one clone | Retry |

## 4 :: What happens next, and why it is not here
## 5 :: Idempotency
## 6 :: Gaps
```

Rules:

1. **Every step has an `On failure`** entry: Retry, Terminal, Compensate, or a human action.
2. **State the end point explicitly** in the header table, and what it is *not*.
3. **Idempotency is a section, not an afterthought**: the dedup key, and why a replay is safe.
4. **Gaps are listed honestly**, numbered, with links to the procedures that share them.
5. A procedure built from others says so ("04 then 01") instead of repeating their steps.

---

## The shape of it

<!-- A small ASCII diagram of how the procedures relate: who triggers what, and where the loops
     meet. Example:

```
CUSTOMER                        CONTROLLER
    |                                |
  04 update nodepool            reads demand + supply
  03 create cluster                  |
    |                           01 add server / 02 remove server
   Git -> ArgoCD -> hub  <-----  observed state
```
-->

## Interfaces

| | Reference | Covers |
|---|---|---|
| 00 | [Interfaces and Data Exchange](00-interfaces.md) | Every call the procedures make, with real payloads |

## <Layer name>

<!-- One table per layer (e.g. Inventory, Tenant clusters, Upgrades). Columns vary by what
     matters for that layer: Trigger, Composed of, Order, Note. -->

| | Procedure | Trigger |
|---|---|---|
| 01 | [<Verb object>](01-verb-object.md) | |

---

## Cross-cutting notes

<!-- Rules that hold for every procedure. Examples:

**Absolute, never deltas.** Every count that crosses a boundary is the desired total.

**Workflow ids are the dedup key.** Stable per target, with the mutable value in the payload.

**Create, verify, never overwrite.** An existing resource is success once its identity fields
match, and a conflict for a human when they do not.
-->
