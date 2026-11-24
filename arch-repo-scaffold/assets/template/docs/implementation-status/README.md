# implementation-status/

The build-status diagram shown on the front page: every component of the system, grouped into
lanes, coloured by status, linked to its repository. The interactive version is `index.html`
(hover for details, filter by status, table view).

## What goes here

| File | Edited by | Purpose |
|---|---|---|
| `components.json` | **You** | The only source. Lanes, components, statuses, flows between lanes |
| `_generate.py` | Rarely | Renders the files below. Standard library only |
| `status-light.svg`, `status-dark.svg` | Generated | Embedded in the front page; GitHub picks one per reader theme |
| `index.html` | Generated | Interactive version, served by GitHub Pages |

## What does not go here

- Hand edits to the SVGs or HTML. The next run overwrites them.
- Plans and dates. A component's `note` says what is done and what is not, not when it will be.

## Updating

```bash
# 1. edit components.json (and set "updated" to today's date)
python3 docs/implementation-status/_generate.py
# 2. commit components.json and the three generated files together
```

## `components.json` format

| Key | Meaning |
|---|---|
| `title` | Diagram heading |
| `updated` | ISO date shown as "Status as of …" |
| `statuses` | The status keys and their labels: `done`, `partial`, `todo`, `external` |
| `lanes[]` | Rows of the diagram, top to bottom: `id`, `title`, `subtitle`, `components[]` |
| `lanes[].components[]` | `name`, `owner` (team or `org/repo`), `status`, `note`, optional `link` |
| `flows[]` | Arrows between lanes: `from` and `to` (lane ids), `label` |

## Example component

```json
{
  "name": "add-server-to-mce",
  "owner": "team-redbull/workflows",
  "status": "partial",
  "note": "Bare metal done. Not yet: the create-vm child for VM pools (AD29).",
  "link": "https://github.com/team-redbull/workflows"
}
```

Reference the architecture by ID in notes (AD29, C7) so a reader can follow the reason.
