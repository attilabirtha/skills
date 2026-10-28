# Agent Instructions

Use this repository when asked to create or revise a proClick-style commercial offer PDF.

## Goal

Generate a polished proClick offer using the bundled assets and the existing ReportLab generator. Run commands from this skill folder unless noted otherwise. Preserve the established look:

- team-photo cover with dark overlay
- cream pages for services, budget, and KPIs
- one dark strategy page
- red accent bars
- white cards with red top borders
- black recommendation blocks
- pale green optimization callout

Use the bundled full-team cover by default. Preserve its aspect ratio and keep every teammate in frame; place cover text in the available headroom and below faces.

## Files

- `scripts/generate_offer.py` - primary editable generator
- `assets/proclick_logo.png` - logo for light backgrounds
- `assets/proclick_logo_white.png` - logo for dark/photo backgrounds
- `assets/proclick_team_cover_full.png` - default full-team cover background
- `references/offer-elements.md` - reusable content rules for pricing, services, focused and complete media allocation, KPIs, and validation
- `SKILL.md` - Codex skill instructions

## Workflow

1. Classify the brief as recurring PPC, standalone audit, fixed-scope implementation/migration, or a contract appendix. Identify document language, currency, tax convention, payers, and client name before choosing pages.
2. Read `references/offer-elements.md` for detailed service, commercial, VAT, channel, language, and validation rules.
3. Copy and patch `scripts/generate_offer.py` in the client workspace; keep the bundled generator generic and the visual system intact unless the user explicitly asks for a different design.
4. Generate the PDF:

```bash
python3 scripts/generate_offer.py --output outputs/proclick_offer.pdf
```

5. Render pages for review when Poppler is available:

```bash
pdftoppm -png outputs/proclick_offer.pdf tmp/proclick_offer
```

6. Inspect the rendered pages for clipped text, poor contrast, wrong totals, tax/currency inconsistency, and scope that does not match the commercial table.

## Content Rules

- Keep offer copy concise and commercial.
- Use VAT-included prices as primary values and net prices as smaller secondary values when both are required.
- Keep separate fees distinct: one-time setup/audit/project, first-month agency fee, recurring agency fee, and media budget. State whether the client pays media platforms directly.
- Keep KPI sections focused on PPC metrics unless the user asks for broader metrics.
- Recalculate budget amounts when percentages change.
- Keep service fee, media budget, and total budget consistent across all pages.
- Keep the channels named in services, strategy, and budget allocation consistent. Use a complete mix with Google, Meta, TikTok, YouTube, and Pinterest when the offer requires full-channel coverage.
- For an audit, document systems, access level, deliverables, delivery date, payment milestones, and any conditional audit credit. Do not imply implementation or ongoing management.
- For a fixed-scope project, document deliverables, assumptions, exclusions, client dependencies, acceptance milestones, and the support/hypercare boundary.
- Keep the language, currency formatting, and localized tax label coherent throughout. Use a font with verified Romanian/Hungarian/English coverage rather than stripping meaningful diacritics.

## Default Company Data

Use these details unless the user changes them:

- INTELLIGENT DIGITAL MARKETING SRL
- CUI: RO16554762
- Piata Victoriei nr. 5, Targu-Mures, Romania
- contact@proclick.ro
- +40 744 692 880
- proclick.ro
