# docs/

The architecture itself. Files at this level are the **agreed, authoritative** documents. The
sub-folders hold procedures, generated artefacts, images, work in progress and reviews.

## What goes at this level

| File | Purpose |
|---|---|
| [`architecture.md`](architecture.md) | The architecture document and the single entry point. Requirements, quality goals and scenarios, constraints, quality controls, decisions, risks, deployment view, context, glossary. Every other document is reachable from here or from the front page. |
| [`naming-convention.md`](naming-convention.md) | How every object is named and labelled, with examples and the reason for each segment. The architecture doc summarises it; this file is the full rule. |
| `<component>.md` | **One specification per component we build**, e.g. `inventory-controller.md`, `kv-capacity-controller.md`. Add one when a component needs more than a row in the decisions table. |

## Sub-folders

| Folder | Holds |
|---|---|
| [`procedures/`](procedures/README.md) | One file per operational procedure, plus `00-interfaces.md` |
| [`animations/`](animations/README.md) | Generated HTML walkthroughs of the procedures |
| [`implementation-status/`](implementation-status/README.md) | Generated build-status diagram |
| [`images/`](images/README.md) | Static images the documents embed |
| [`drafts/`](drafts/README.md) | Proposals not yet agreed |
| [`review/`](review/README.md) | Assessments of code or designs produced elsewhere |

## What does not go here

- Proposals still under discussion: `drafts/`.
- Slides, PDFs and meeting notes. Link to them from the doc that needs them, or leave them out.
- Implementation code. It lives in the implementation repos; `implementation-status/` links to
  them.

## Rules

1. **IDs are stable and never reused.** A removed decision keeps its gap (AD2 deleted, AD3 stays
   AD3).
2. **Cross-reference by ID**, not by prose: "per AD16", "see C7".
3. **Agreed only.** When something becomes agreed in `drafts/`, merge its content here and delete
   the draft.
4. File names are lowercase kebab-case.

## Example: a component specification

A component spec opens with its requirements and ends with what is still open. Skeleton, as
used by `kv-capacity-controller.md`:

```markdown
# KV Capacity Controller — specification

## 1 :: Scope
### 1.1 In scope
### 1.2 Out of scope, with owner
## 2 :: Deployment
## 3 :: Configuration
## 4 :: Inputs
## 5 :: Model
## 6 :: Reconcile loop
## 7 :: Failure behaviour
## 8 :: Observability
### 8.1 Metrics
### 8.2 Alerts
## 9 :: Access
## 10 :: Open items
```

Or requirement-led, as used by `inventory-controller.md`: `## Requirements`, `## Terms`, one
`## R1 · <requirement>` section per requirement, then `## Config`,
`## Why it is built this way`, `## Open`.
