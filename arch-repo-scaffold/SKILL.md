---
name: arch-repo-scaffold
description: Generate the folder structure for a new architecture repository, modelled on the kubevirt-workflows repo layout (architecture doc, naming convention, procedures, animations, implementation-status diagram, acceptance tests, drafts, reviews, images). Every generated folder gets a README explaining what belongs there, with examples. Use when the user wants to start, bootstrap, scaffold or initialise a new architecture repo, design repo or documentation repo.
---

# Architecture repo scaffold

Generates a new architecture repository with the same layout as `~/claude/kubevirt-workflows`.
Every folder gets a `README.md` that says what belongs there, what does not, the naming rule,
and a worked example. The core documents are created as skeletons with their section headings in
place.

## Layout produced

```
<repo>/
├── README.md                      Front page: status diagram + documents table
├── .gitignore
├── acceptance-tests/
│   ├── README.md
│   └── acceptance-tests.md        Skeleton: normative language, one section per requirement
└── docs/
    ├── README.md                  What sits at docs/ root (architecture, naming, component specs)
    ├── architecture.md            Skeleton: requirements, quality, constraints, decisions, risks…
    ├── naming-convention.md       Skeleton: names, zones/scopes, labels
    ├── procedures/
    │   ├── README.md              Procedure index + the procedure file format
    │   └── 00-interfaces.md       Skeleton: every external call the procedures make
    ├── animations/README.md       Generated, self-contained HTML walkthroughs
    ├── implementation-status/
    │   ├── README.md
    │   ├── components.json        Starter data
    │   └── _generate.py           Builds status-light/dark.svg and index.html (stdlib only)
    ├── images/README.md           Static diagrams referenced by the docs
    ├── drafts/README.md           Proposals not yet agreed
    └── review/README.md           Assessments of external code or designs
```

## Steps

1. **Collect the inputs.** Ask only for what the user has not already given:
   - **Project name**, e.g. `OCP KubeVirt platform` (required)
   - **Destination directory** (required). Default to `~/claude/<kebab-case-name>`.
   - **Document ID**, the number that prefixes the architecture title (e.g. `70` gives
     `# 70 :: OCP Kubevirt`). Optional; omit it and the title has no prefix.
   - **GitHub Pages base URL**, e.g. `https://<owner>.github.io/<repo>`. Optional; it is used for the
     animation and status links. Without it the links are relative.

2. **Run the generator:**

   ```bash
   python3 ~/.claude/skills/arch-repo-scaffold/scripts/scaffold.py \
     --name "<Project name>" --dest <dir> [--id 70] [--pages-url https://owner.github.io/repo]
   ```

   It never overwrites an existing file; it lists anything it skipped. Add `--dry-run` to preview.
   The script also runs `_generate.py` once so the status SVGs and HTML exist from the first commit.

3. **Report** the tree that was created (`find <dir> -not -path '*/.git/*' | sort`) and tell the
   user where to start: `docs/architecture.md` section 1 (Requirements), because everything else
   gets its ID from there (R-IDs drive acceptance tests and procedures).

4. **Offer, do not do:** `git init` plus a first commit, and creating the GitHub repo. Both need
   the user's go-ahead. The arc42 skills (`arc42-section-01` to `-12`) can help fill the
   architecture doc section by section.

## Conventions the templates encode (from kubevirt-workflows)

- Section headings use `## N :: Title`. Procedures use `# NN :: Title`.
- IDs are stable and never reused: `R` requirements, `SC` quality goals and scenarios, `C`
  constraints, `AD` decisions, `R` risks (in their own table), `P`/`M`/`U`/`D` acceptance tests.
- Generated artefacts (animations, status diagram) are produced by a `_generate.py` script that
  sits beside them. Edit the source and re-run; never hand-edit the output.
- Lowercase kebab-case for every folder and file name. Number procedures `NN-verb-object.md`.
- Drafts are marked `(DRAFT, for discussion)` in the title and move out of `drafts/` once
  agreed.

## Changing the template

The template tree is at `~/.claude/skills/arch-repo-scaffold/assets/template/`. Placeholders:
`{{PROJECT_NAME}}`, `{{TITLE_PREFIX}}`, `{{PAGES_BASE}}`, `{{DATE}}`. Any file added to the tree
is copied into new repos.
