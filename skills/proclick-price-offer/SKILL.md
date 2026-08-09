---
name: proclick-price-offer
description: Create or update branded proClick commercial offer PDFs that replicate the latest proClick proposal style. Use when asked to prepare, revise, restyle, or regenerate a proClick/proClick offer, pricing proposal, PPC/eCommerce marketing offer, or client PDF using the current proClick visual system, including client-specific scope, channel mix, cover layout, and pricing mode.
---

# proClick Price Offer

## Purpose

Create polished proClick offer PDFs with the current proClick visual system:

- cover with team-photo background, dark overlay, white logo, large white headline
- warm cream interior pages
- dark strategy page
- red proClick accent bars and card borders
- white service cards with red top rule
- black conclusion blocks and pale green recommendation blocks
- official proClick company data and assets
- flexible pricing display: either `TVA inclus` hierarchy or `net + TVA`, depending on the brief

## Assets

Use bundled assets from `assets/` by default:

- `proclick_logo.png` for light backgrounds
- `proclick_logo_white.png` for dark/photo backgrounds
- `proclick_team_cover.png` for default cover background

Do not redraw the logo manually. Use these files directly.

If the current offer uses a newer or wider team photo from the repo/workspace, prefer that asset over the default portrait cover. Keep the image aspect ratio intact; never stretch the cover image.

## Generator

Use `scripts/generate_offer.py` as the starting point for proClick offer PDFs.

Run:

```bash
python3 scripts/generate_offer.py --output outputs/proclick_oferta_client.pdf
```

The script uses ReportLab and local system fonts. If `reportlab` is missing, install it in the active Python environment or use the bundled workspace runtime when available.

## References

Read `references/offer-elements.md` when the offer needs detailed service modules, pricing mode rules, focused or complete media allocation options, scope-specific channel rules, CSS Partner wording, PPC KPI wording, cover-layout guidance, or final validation rules.

## Workflow

1. Copy or patch `scripts/generate_offer.py` only when the offer content needs to change.
2. Keep the visual system intact: cream background, dark strategy spread, red accent, white cards, dark conclusion blocks.
3. Update client-specific text, budget splits, service wording, KPIs, and company/contact data.
4. Match the pricing mode requested by the user: `TVA inclus` or `net + TVA`. Do not mix them.
5. Generate the PDF into the current workspace `outputs/` directory.
6. Render the final PDF to PNG with `pdftoppm` and inspect the affected pages before delivering.

## Content Pattern

Use this structure unless the user asks otherwise:

1. Cover: client name, offer title, total budget, service fee, media budget, objective.
2. Services: six-card grid with service titles and concise details.
3. Strategy: dark page with three-stage launch approach.
4. Channels or media allocation: either a channel-role table or a budget-allocation table, depending on the brief.
5. Commercial model: setup fee, monthly fee, media budget, and scope notes.
6. KPI/reporting/company: PPC KPIs, reporting cadence, scope notes, company data.

## Default Offer Elements

- Use one pricing mode consistently across the document:
  - `TVA inclus` as primary values with net values below, or
  - `net + TVA` as primary values when the user explicitly asks for prices without VAT.
- Choose the media mix by objective, budget, and scope: use a focused mix for concentrated launch pressure, or a broader mix only when the brief explicitly includes those channels.
- Mention CSS Partner support in the feed/Shopping service card when Google Shopping is included.
- Keep the first-month strategy realistic: validate tracking, messages, and products sellable for promotion and sales before scaling.
- If channels are explicitly excluded from the scope, remove them from both narrative text and channel tables.
- On the cover, move text lower when needed so the team faces remain visible and the image stays readable.

## Style Rules

- Keep Romanian offer text professional and direct.
- Prefer concise service descriptions over long paragraphs.
- Focus KPI tables on PPC metrics unless the user asks for broader business KPIs.
- Keep monetary values internally consistent across cover, media allocation, and narrative text.
- Keep scope wording internally consistent across service cards, channel tables, commercial page, and cover summary.
- Use ASCII text in generated PDFs to avoid glyph issues unless the environment has verified Romanian font rendering.
- Preserve proClick company details unless the user explicitly changes them:
  `INTELLIGENT DIGITAL MARKETING SRL`, `CUI: RO16554762`, `Piata Victoriei nr. 5, Targu-Mures, Romania`, `contact@proclick.ro`, `+40 744 692 880`, `proclick.ro`.
