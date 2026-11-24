# drafts/

Proposals under discussion that are **not yet agreed**. Nothing here is authoritative; the
architecture doc is.

## What goes here

- A design question with options and a recommendation, written up for a decision meeting.
- A new procedure or component spec before it is agreed.
- Analysis supporting a decision that is still open (scenarios, cost of each option).

## What does not go here

- Agreed content. Once agreed, move it: decisions become AD rows in `../architecture.md`,
  procedures move to `../procedures/`, specs move to `docs/` root. Then **delete the draft**.
- Reviews of other people's work: `../review/`.
- Personal notes and scratch files.

## Rules

1. The title ends with **`(DRAFT, for discussion)`**.
2. The file ends with a **`## To discuss`** section: the numbered questions the meeting must
   answer.
3. Name after the question, lowercase kebab-case: `mce-vm-placement.md`, not `draft-v2.md`.

## Example

```markdown
# MCE and tenant VMs on shared KubeVirt hosts (DRAFT, for discussion)

## 1. What can share one host today
## 2. Scenarios
| # | Scenario | Outcome |
|---|---|---|
| S1 | One host lost in az1 | One MCE master and up to four tenant VMs lost; quorum holds |

## 3. Recommendations
## 4. Why bin-packing does not cancel the anti-affinity
## 5. The cost of a required rule
## 6. To discuss
1. Do we accept a preferred rule, or require hard separation?
```
