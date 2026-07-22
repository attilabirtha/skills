---
name: proclick-price-offer
description: Create or update branded ProClick commercial offer PDFs that replicate the look and feel of the ProClick agency presentation and the ZEILA price offer. Use when asked to prepare, revise, restyle, or regenerate a ProClick/proClick offer, pricing proposal, PPC/eCommerce marketing offer, or client PDF using the established ProClick visual style.
---

# ProClick Price Offer

## Purpose

Create polished ProClick offer PDFs with the same visual system as the ZEILA proposal:

- cover with team-photo background, dark overlay, white logo, large white headline
- warm cream interior pages
- dark strategy page
- red ProClick accent bars and card borders
- white service cards with red top rule
- black conclusion blocks and pale green recommendation blocks
- official ProClick company data and assets
- price hierarchy with VAT-included values primary and net values secondary

## Assets

Use bundled assets from `assets/`:

- `proclick_logo.png` for light backgrounds
- `proclick_logo_white.png` for dark/photo backgrounds
- `proclick_team_cover.png` for cover background

Do not redraw the logo manually. Use these files directly.

## Generator

Use `scripts/generate_offer.py` as the starting point for ProClick offer PDFs.

Run:

```bash
python3 scripts/generate_offer.py --output outputs/proclick_oferta_client.pdf
```

The script uses ReportLab and local system fonts. If `reportlab` is missing, install it in the active Python environment or use the bundled workspace runtime when available.

## References

Read `references/offer-elements.md` when the offer needs detailed service modules, VAT pricing hierarchy, focused or complete media allocation options, CSS Partner wording, PPC KPI wording, or final validation rules.

## Workflow

1. Copy or patch `scripts/generate_offer.py` only when the offer content needs to change.
2. Keep the visual system intact: cream background, dark strategy spread, red accent, white cards, dark conclusion blocks.
3. Update client-specific text, budget splits, service wording, KPIs, and company/contact data.
4. Generate the PDF into the current workspace `outputs/` directory.
5. Render the final PDF to PNG with `pdftoppm` and inspect the affected pages before delivering.

## Content Pattern

Use this structure unless the user asks otherwise:

1. Cover: client name, offer title, total budget, service fee, media budget, objective.
2. Services: six-card grid with service titles and concise details.
3. Strategy: dark page with three-stage launch approach.
4. Media allocation: table with channel percentages, amounts, and role.
5. KPI/reporting/company: PPC KPIs, reporting cadence, Shopify/eCommerce notes, company data.

## Default Offer Elements

- Display VAT-included prices as the main values. Display net prices below them in smaller muted text.
- Choose the media mix by objective and budget: use a focused mix for concentrated launch pressure, or a complete mix with Google, Meta, TikTok, YouTube, and Pinterest when the offer requires full-channel coverage.
- Mention CSS Partner support in the feed/Shopping service card when Google Shopping is included.
- Keep the first-month strategy realistic: validate tracking, messages, and products sellable for promotion and sales before scaling.

## Style Rules

- Keep Romanian offer text professional and direct.
- Prefer concise service descriptions over long paragraphs.
- Focus KPI tables on PPC metrics unless the user asks for broader business KPIs.
- Keep monetary values internally consistent across cover, media allocation, and narrative text.
- Use ASCII text in generated PDFs to avoid glyph issues unless the environment has verified Romanian font rendering.
- Preserve ProClick company details unless the user explicitly changes them:
  `INTELLIGENT DIGITAL MARKETING SRL`, `CUI: RO16554762`, `Piata Victoriei nr. 5, Targu-Mures, Romania`, `contact@proclick.ro`, `+40 744 692 880`, `proclick.ro`.
