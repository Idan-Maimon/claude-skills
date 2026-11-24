# acceptance-tests/

How the delivered system is accepted. This is the contract with whoever builds and operates it:
a requirement in [`../docs/architecture.md`](../docs/architecture.md) is met when its tests here
pass.

## What goes here

- **`acceptance-tests.md`**: the test specification. One section per requirement (R1, R2…),
  each with its prerequisites and a table of tests.
- **Evidence documents** produced while running the tests, named
  `evidence-<yyyy-mm-dd>-<environment>.md`, e.g. `evidence-2026-12-01-test-site.md`.
- Supporting fixtures a test needs (sample manifests, input files), in a sub-folder named after
  the test ID, e.g. `p2/hosted-cluster.yaml`.

## What does not go here

- Unit or integration tests of code. They live with the code, in the implementation repos.
- How a procedure works. That is [`../docs/procedures/`](../docs/procedures/README.md); a test
  names the procedure it exercises and checks its outcome.
- Quality scenarios. They are defined in the architecture doc (section 2.1); a test may verify one.

## Rules

1. **Every test traces to a requirement.** The section heading carries the R-ID:
   `## 3. Provisioning (R1)`.
2. **Test IDs are stable**, prefixed by section: `P` provisioning, `M` modification, `U` upgrade,
   `D` deletion. Add new letters for new requirement areas. Never renumber.
3. **Acceptance criteria are observable.** Each criterion names where to look: a status, a Git
   commit, a workflow id, a metric. "Works correctly" is not a criterion.
4. **Use the normative words** defined in the spec (must, should, may) and nothing softer.
5. **Results** are `Passed`, `Failed` or `NA` (a dependency is not delivered yet). The `Result`
   column stays empty in the spec and is filled in a copy for each test run.

## Example

```markdown
## 3. Provisioning (R1)

**Prerequisites:**

1. Customer MCE `ocp4-test-mce-five-a` with admin access
2. The platform workflows and the Inventory Controller deployed

**Tests**

| ID | Test | Procedure | Acceptance Criteria | Result |
|---|---|---|---|---|
| P2 | Create a hosted cluster on bare metal | 1. Create `ocp4-test-eck-five-a` on `ocp4-test-mce-five-a`.<br>2. One NodePool per zone, 2 replicas each. | 1. HostedCluster Available; 6 workers Ready, 2 per zone.<br>2. Workflow `provision-cluster-ocp4-test-eck-five-a` Completed, no failed activity.<br>3. Git: day1 file merged to `main`.<br>4. ArgoCD: Application Synced to the merge commit and Healthy. | |
```
