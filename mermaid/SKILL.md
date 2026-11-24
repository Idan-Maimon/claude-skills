---
name: mermaid
description: Render Mermaid diagrams (flowchart, gantt, sequence, state, ER, C4) to PNG or SVG using the locally installed mermaid-cli. Use when asked to draw, diagram, chart, or visualise something, or to re-render an existing .mmd file.
---

# Mermaid rendering

`mermaid-cli` is installed locally at `~/claude/tools/mermaid`. It is **not** on PATH.

## Render

```bash
MMDC=~/claude/tools/mermaid/node_modules/.bin/mmdc
$MMDC -i diagram.mmd -o diagram.png --size 2400 -b white -s 2
```

- `--size` is the max width or height in px. Use 2400 for wide gantt charts, 1600 otherwise.
- `-s 2` is the scale factor. Always use it for PNG or text is blurry.
- `-b white` avoids a transparent background that looks broken in docs.
- `-t <theme>`: base, dark, default, forest, neutral, neo, redux.
- There is **no** `-w` / `--width` flag. Use `--size`.
- Output `.svg` or `.pdf` by changing the extension, or force with `-e`.
- Markdown input renders every fenced ```mermaid block in the file.

## Always look at the result

Render, then `Read` the PNG. Mermaid silently produces ugly output: labels
overflowing their bars, clipped text, mislabelled axes. Do not hand over a
diagram you have not seen.

## Gantt gotchas

- `tickInterval 1week` can render a bogus label at the left edge. Use
  `tickInterval 2week` with `axisFormat %d %b`, which is reliable.
- Add `todayMarker off` unless the chart is meant to show today.
- Long task names spill outside the bar to the right. Keep names short and put
  the detail in the surrounding prose, not in the chart.
- `:crit` renders red, `:active` light blue, `:done` grey. Use them to carry
  meaning, and say in the caption what the colours mean.
- Milestones (`:milestone, id, <date>, 0d`) are good for gates between phases.

## Storing diagrams

Keep the `.mmd` source next to the rendered image and commit both. The source is
the thing that gets edited; the image is what people look at.

## Reinstalling

```bash
mkdir -p ~/claude/tools/mermaid && cd ~/claude/tools/mermaid
npm install @mermaid-js/mermaid-cli
```

On macOS (Homebrew `node`), the local `npm install` works as-is: Puppeteer
downloads its own Chrome / chrome-headless-shell into `~/.cache/puppeteer`, no
system Chrome or extra config needed. If that cache is ever missing, run
`npx puppeteer browsers install chrome-headless-shell` from this directory.
