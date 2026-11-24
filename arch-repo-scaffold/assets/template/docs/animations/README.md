# Animations

One animation per procedure, walking its flow step by step. Each step shows the real call,
payload and response beneath the diagram.

**Open them from GitHub Pages** (the links below), or open a file locally in any browser. Each
file is self-contained, with no dependencies and no network calls, so it also works air-gapped.

| Key | Action |
|---|---|
| → / ← | Next / previous step |
| Space | Play / pause |
| `#step=7` on the link | Open on step 7 |

Base address: `{{PAGES_BASE}}/docs/animations/`

## What goes here

- **`NN-verb-object.html`**: one generated file per procedure, with the same number and name as
  the procedure in [`../procedures/`](../procedures/README.md).
- **`_generate.py`**: the single source for every animation. Steps, payloads and diagrams are
  defined there.
- This **README**: the index, grouped by the same layers as the procedures index.

## What does not go here

- Hand-written HTML. The next run of `_generate.py` overwrites it.
- Animations with no procedure behind them. Write the procedure first. A draft animation for a
  flow under review is allowed if its index row says **(draft, for review)**.

## Index

<!-- One table per layer, mirroring ../procedures/README.md. A procedure with no animation keeps
     its row with "No animation". Example:

| # | Animation | Procedure |
|---|---|---|
| 04 | [Update NodePool]({{PAGES_BASE}}/docs/animations/04-update-nodepool.html) | [04](../procedures/04-update-nodepool.md) |
| 06 | No animation | [06](../procedures/06-create-kv-cluster.md) |
-->

| # | Animation | Procedure |
|---|---|---|

---

## Changing an animation

All animations are generated from `_generate.py`. Edit a step there and run:

```
python3 _generate.py
```

Never edit the HTML by hand: the next run overwrites it.

**Starting from scratch:** copy `_generate.py` from an existing architecture repo that has one
(e.g. `kubevirt-workflows/docs/animations/_generate.py`) and replace its step definitions.
