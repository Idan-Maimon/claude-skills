# claude-skills

Personal [Claude Code](https://claude.com/claude-code) skills. Each folder is one skill with a
`SKILL.md` at its root.

| Skill | What it does |
|---|---|
| [arch-repo-scaffold](arch-repo-scaffold/SKILL.md) | Generates a new architecture repository modelled on the kubevirt-workflows layout, with a README in every folder explaining what belongs there, with examples. [Layout overview](arch-repo-scaffold/README.md) |
| [mermaid](mermaid/SKILL.md) | Renders Mermaid diagrams (flowchart, gantt, sequence, state, ER, C4) to PNG or SVG with a local mermaid-cli. Needs Node.js; install steps are in the skill under *Reinstalling* |

## Install

Claude Code loads skills from `~/.claude/skills/`. Symlink each skill there so edits in this repo
take effect immediately:

```bash
ln -s ~/claude/claude-skills/<skill> ~/.claude/skills/<skill>
```

## Adding a skill

1. Create `<skill-name>/SKILL.md` with `name` and `description` frontmatter.
2. Put scripts in `<skill-name>/scripts/` and templates or other files in `<skill-name>/assets/`.
3. Symlink it into `~/.claude/skills/` and add a row to the table above.
