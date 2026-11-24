# {{PROJECT_NAME}}

<a href="{{PAGES_BASE}}/docs/implementation-status/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/implementation-status/status-dark.svg">
    <img alt="{{PROJECT_NAME}} build status" src="docs/implementation-status/status-light.svg">
  </picture>
</a>

Click the diagram for the interactive version: hover a component for its details, filter by status,
click through to its repository.

**Updating the status:** edit [`docs/implementation-status/components.json`](docs/implementation-status/components.json), then run
`python3 docs/implementation-status/_generate.py` and commit the regenerated files.

## Documents

| | |
|---|---|
| [Architecture](docs/architecture.md) | Requirements, quality goals, constraints, decisions, risks |
| [Naming convention](docs/naming-convention.md) | Names, scopes and labels |
| [Acceptance tests](acceptance-tests/acceptance-tests.md) | Tests per requirement, with their acceptance criteria |
| [Procedures](docs/procedures/README.md) | Every procedure, by layer |
| [Animations]({{PAGES_BASE}}/docs/animations/) | Each procedure, step by step |

<!--
  Front page rules (delete this comment once read):
  - Keep this file short: the status diagram and one table row per top-level document.
  - Add a row when a new document lands at docs/ root (e.g. a component spec).
  - Each folder has its own README describing what belongs in it.
-->

## Repository layout

```
acceptance-tests/          How the delivered system is accepted, test by test
docs/
  architecture.md          The architecture document: the single entry point
  naming-convention.md     How every object is named and labelled
  <component>.md           One specification per component we build
  procedures/              One file per operational procedure, plus 00-interfaces.md
  animations/              Generated step-by-step HTML walkthroughs of the procedures
  implementation-status/   Generated build-status diagram, edited through components.json
  images/                  Static diagrams referenced by the documents
  drafts/                  Proposals under discussion, not yet agreed
  review/                  Assessments of code or designs produced outside this repo
```
