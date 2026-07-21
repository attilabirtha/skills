# ProClick Price Offer Skill

Reusable AI-agent skill for generating ProClick-style commercial offer PDFs.

## Quick Start

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Generate a PDF:

```bash
python3 scripts/generate_offer.py --output outputs/proclick_offer.pdf
```

## Files

- `SKILL.md` - Codex-compatible skill instructions
- `AGENTS.md` - generic instructions for OpenClaw, Claude Code, Cursor, and other AI coding agents
- `scripts/generate_offer.py` - ReportLab generator for the branded PDF
- `assets/` - ProClick logo and cover background assets

## Install For Codex

Copy this folder to:

```bash
~/.codex/skills/proclick-price-offer
```

Then ask:

```text
Use $proclick-price-offer to create a branded ProClick commercial offer PDF.
```
