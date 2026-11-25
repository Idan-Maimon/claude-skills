# claude-skills

Personal [Claude Code](https://claude.com/claude-code) skills. Each folder is one skill with a
`SKILL.md` at its root.

## Architecture documentation

| Skill | What it does |
|---|---|
| [arch-repo-scaffold](arch-repo-scaffold/README.md) | Generates a new architecture repository modelled on the kubevirt-workflows layout, with a README in every folder explaining what belongs there, with examples |
| [arc42-section-01](arc42-section-01/SKILL.md) … [arc42-section-12](arc42-section-12/SKILL.md) | One skill per arc42 section, each guiding you through it interactively and drafting it: introduction and goals, constraints, context, solution strategy, building blocks, runtime, deployment, crosscutting concepts, decisions, quality, risks, glossary |
| [arc42-review](arc42-review/SKILL.md) | Reviews one arc42 section or the whole document for accuracy, completeness and consistency across sections |
| [arc42-lint](arc42-lint/SKILL.md) | Checks that IDs are consistent across arc42 sections: interfaces §3↔§5, deployment coverage §5↔§7, quality tags §1↔§10, ADR to risk links §9↔§11 |

## Diagrams

| Skill | What it does |
|---|---|
| [mermaid](mermaid/SKILL.md) | Renders Mermaid diagrams (flowchart, gantt, sequence, state, ER, C4) to PNG or SVG with a local mermaid-cli. Needs Node.js; install steps are in the skill under *Reinstalling* |

## Skill development

| Skill | What it does |
|---|---|
| [skill-creator](skill-creator/SKILL.md) | Creates and edits skills, runs evals and benchmarks them. Anthropic's skill, Apache-2.0, see [its licence](skill-creator/LICENSE.txt) |

## Install

Claude Code loads skills from `~/.claude/skills/`. Symlink each skill there so edits in this repo
take effect immediately:

```bash
ln -s ~/claude/claude-skills/<skill> ~/.claude/skills/<skill>
```

Or link every skill in the repo at once:

```bash
for d in ~/claude/claude-skills/*/; do ln -sfn "${d%/}" ~/.claude/skills/"$(basename "$d")"; done
```

## Adding a skill

1. Create `<skill-name>/SKILL.md` with `name` and `description` frontmatter.
2. Put scripts in `<skill-name>/scripts/` and templates or other files in `<skill-name>/assets/`.
3. Symlink it into `~/.claude/skills/` and add a row to the table above.
