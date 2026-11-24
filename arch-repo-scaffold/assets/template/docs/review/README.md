# review/

Assessments of work produced **outside** this repo, such as an implementation branch, a vendor
design or another team's plan, measured against this architecture.

## What goes here

- A code or design assessment: what was reviewed, against what, what is good, what must change.
- A corrected version of an external plan, when the correction is easier to read as a whole.

## What does not go here

- Our own proposals: `../drafts/`.
- Changes to the architecture that a review prompts. Make them in the architecture doc and
  reference the review from the commit.

## Rules

1. **Pin what was reviewed**: repo, branch and commit hash, with the date. A review of a moving
   target is worthless a week later.
2. **State the method**, including what was *not* done (e.g. "tests were not run").
3. **Cite the architecture by ID** for every issue (AD23, C7), so the fix can be checked against
   the rule.
4. Every issue has a **suggested fix**; end with the suggested order to tackle them.
5. Name `<subject>-assessment.md`, e.g. `update-nodepool-assessment.md`.

## Example

```markdown
# Assessment: `update-nodepool` and the server-lifecycle domain

| | |
|---|---|
| **Branch assessed** | `team-redbull/workflows` → `feat/update-nodepool` at `43c8ee2` (2026-11-16) |
| **Assessed against** | `docs/architecture.md` (AD21–AD31) |
| **Scope** | The server-lifecycle domain only |
| **Out of scope** | The branch's changes to other domains |
| **Method** | Code and design notes read. **Tests were not run** |

---

## Summary
What is strong, then the numbered issues that need attention.

## Issues and suggested fixes
### 1. A scale-down hands used workers back to the pool as they are (AD23)
**Where:** `activities/scale_down.py`. **Why it matters:** … **Fix:** …

## Suggested order
```
