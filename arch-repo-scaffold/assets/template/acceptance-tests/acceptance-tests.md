# {{PROJECT_NAME}} - Acceptance Tests

## 1. Purpose of the Document

To document the acceptance tests related to the implementation of the {{PROJECT_NAME}}.

## 2. Normative

### Normative Language Interpretation

For the purposes of this document, the following terms are to be interpreted as normative
requirements.

The word "must" indicates an absolute requirement and denotes a condition that is mandatory for
compliance.

The word "should" indicates a recommended practice, which is not mandatory but is strongly advised
unless a justified alternative is documented.

The word "may" indicates a permissible action and grants discretion without obligation. The word
"could" indicates a possible option or capability and does not imply a requirement or
recommendation.

A "test passed" condition indicates that all mandatory criteria defined in the applicable test
procedure have been satisfied and the system is considered compliant with the specified
requirement.

A "test failed" condition indicates that one or more mandatory criteria have not been satisfied,
and the system is considered non-compliant until corrective actions are taken and the test is
successfully re-executed.

A "test NA" condition indicates that the test could not be executed because a component it depends
on is not yet available. A test marked NA must be executed once that component is delivered.

<!--
  Add one "### <TOPIC> (MUST REQUIREMENT)" block per rule that applies to every test,
  e.g. "GITOPS (MUST REQUIREMENT)": all state changes go through Git, and commits reference
  the test ID. Delete this comment once done.
-->

### Evidence Document

For all tests whose acceptance criteria cannot be fully validated through version control, system
status or configuration review alone, an additional Evidence Document must be supplied. This
document must enumerate all relevant evidence (commands and their output, workflow ids and their
history, metric names and their measured values) and its explicit correlation to the applicable
test name and test identifier. Each item must be clearly annotated as compliant or non-compliant
relative to the defined acceptance criteria.

---

## 3. <Requirement area> (R1)

<!-- One sentence: which procedures this section exercises and what it proves. -->

**Prerequisites:**

1.

**Tests**

| ID | Test | Procedure | Acceptance Criteria | Result |
|---|---|---|---|---|
| P1 | | | | |
