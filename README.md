# ProClick Price Offer Skill

Reusable AI-agent skill for generating ProClick-style commercial offer PDFs.

The package contains:

- `SKILL.md` - Codex-compatible skill instructions
- `AGENTS.md` - generic instructions for OpenClaw, Claude Code, Cursor, and other AI coding agents
- `scripts/generate_offer.py` - ReportLab generator for the branded PDF
- `assets/` - ProClick logo and cover background assets

## What It Generates

The generator reproduces the look and feel of the ProClick agency offer created for ZEILA:

- cover with team-photo background and dark overlay
- cream interior pages
- dark strategy page
- red ProClick accent rules
- white offer cards with red top borders
- media allocation table
- simplified PPC KPI table
- company data block

## Quick Start

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Generate a PDF:

```bash
python3 scripts/generate_offer.py --output outputs/proclick_offer.pdf
```

## Use With Codex

Copy this folder to:

```bash
~/.codex/skills/proclick-price-offer
```

Then ask:

```text
Use $proclick-price-offer to create a branded ProClick commercial offer PDF.
```

## Use With OpenClaw Or Other Agents

Point the agent to `AGENTS.md` and ask it to follow the workflow. The script is self-contained and can be patched for client-specific offer content.

Example:

```text
Use the instructions in AGENTS.md to create a ProClick-style price offer for a Shopify eCommerce client.
```

## Requirements

- Python 3.10+
- `reportlab`
- optional for visual verification: Poppler `pdftoppm`

## Notes

The included script is intentionally simple and editable. For a new client proposal, patch `scripts/generate_offer.py` content sections, regenerate the PDF, and render pages to PNG for visual review before delivery.
