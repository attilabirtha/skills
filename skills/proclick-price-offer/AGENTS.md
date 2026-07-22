# Agent Instructions

Use this repository when asked to create or revise a ProClick-style commercial offer PDF.

## Goal

Generate a polished ProClick offer using the bundled assets and the existing ReportLab generator. Run commands from this skill folder unless noted otherwise. Preserve the established look:

- team-photo cover with dark overlay
- cream pages for services, budget, and KPIs
- one dark strategy page
- red accent bars
- white cards with red top borders
- black recommendation blocks
- pale green optimization callout

## Files

- `scripts/generate_offer.py` - primary editable generator
- `assets/proclick_logo.png` - logo for light backgrounds
- `assets/proclick_logo_white.png` - logo for dark/photo backgrounds
- `assets/proclick_team_cover.png` - cover background
- `references/offer-elements.md` - reusable content rules for pricing, services, focused and complete media allocation, KPIs, and validation
- `SKILL.md` - Codex skill instructions

## Workflow

1. Read the user request and identify changes to client name, offer title, budgets, services, channel mix, KPI wording, and company details.
2. Read `references/offer-elements.md` if the offer needs detailed services, VAT handling, channel choices, or validation rules.
3. Patch `scripts/generate_offer.py`; keep the visual system intact unless the user explicitly asks for a different design.
4. Generate the PDF:

```bash
python3 scripts/generate_offer.py --output outputs/proclick_offer.pdf
```

5. Render pages for review when Poppler is available:

```bash
pdftoppm -png outputs/proclick_offer.pdf tmp/proclick_offer
```

6. Inspect the rendered pages for clipped text, poor contrast, wrong totals, and inconsistent budget sums.

## Content Rules

- Keep offer copy concise and commercial.
- Use VAT-included prices as primary values and net prices as smaller secondary values when both are required.
- Keep KPI sections focused on PPC metrics unless the user asks for broader metrics.
- Recalculate budget amounts when percentages change.
- Keep service fee, media budget, and total budget consistent across all pages.
- Keep the channels named in services, strategy, and budget allocation consistent. Use a complete mix with Google, Meta, TikTok, YouTube, and Pinterest when the offer requires full-channel coverage.
- Use ASCII text in PDF content unless Romanian font rendering is verified.

## Default Company Data

Use these details unless the user changes them:

- INTELLIGENT DIGITAL MARKETING SRL
- CUI: RO16554762
- Piata Victoriei nr. 5, Targu-Mures, Romania
- contact@proclick.ro
- +40 744 692 880
- proclick.ro
