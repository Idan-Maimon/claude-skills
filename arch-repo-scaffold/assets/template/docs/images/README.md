# images/

Static images embedded by the documents: deployment views, context diagrams, exported
whiteboards.

## What goes here

- **Rendered diagrams** referenced from a document, e.g. `deployment-view.png` embedded by
  `architecture.md` section 7.1 as `![Deployment View](images/deployment-view.png)`.
- **The diagram source beside its render**, with the same base name, so it can be regenerated:
  `deployment-view.drawio` + `deployment-view.png`, or `context.mmd` + `context.png`.

## What does not go here

- Images no document links to. If nothing embeds it, delete it.
- Generated status diagrams: `../implementation-status/`.
- Animations: `../animations/`.
- Screenshots of chats, slides or PDFs used as a substitute for writing the content down.

## Rules

1. Name after **what it shows**, lowercase kebab-case: `deployment-view.png`,
   `runtime-create-cluster.png`. Not `diagram1.png` or `Screenshot 2026-11-03.png`.
2. PNG for diagrams (render at 2x so text stays sharp), SVG when the tool exports clean SVG.
3. When you change the source, re-render and commit both in the same commit.

## Example

```
images/
├── deployment-view.drawio
├── deployment-view.png        ← architecture.md §7.1
├── context.mmd
└── context.png                ← architecture.md §8.3
```

Render a Mermaid source with:
`~/claude/tools/mermaid/node_modules/.bin/mmdc -i context.mmd -o context.png -b white -s 2`
