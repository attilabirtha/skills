---
name: proclick-price-offer
description: Create or update branded proClick commercial offer PDFs that replicate the latest proClick proposal style. Use when asked to prepare, revise, restyle, or regenerate a proClick/proClick offer, pricing proposal, PPC/eCommerce marketing offer, or client PDF using the current proClick visual system, including client-specific scope, channel mix, cover layout, and pricing mode.
---

# proClick Price Offer

## Purpose

Create polished proClick offer PDFs with the current proClick visual system. The skill supports recurring PPC engagements, paid audits, fixed-scope digital projects, and contract appendices; choose the commercial model before adapting the layout.

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
- `proclick_team_cover_full.png` for the default full-team cover background

Do not redraw the logo manually. Use these files directly.

Use the full-team cover by default. It is a portrait composition of the official proClick team photo, with every team member fully inside the frame.

If the current offer uses a newer official full-team photo from the repo/workspace, prefer it over the bundled asset. Keep the image aspect ratio intact; never stretch or crop team members out of the cover image.

## Generator

Use `scripts/generate_offer.py` as the starting point for a standard recurring PPC/eCommerce offer. It is a visual-system template, not a universal pricing calculator.

Run:

```bash
python3 scripts/generate_offer.py --output outputs/proclick_oferta_client.pdf
```

The script uses ReportLab and local system fonts. If `reportlab` is missing, install it in the active Python environment or use the bundled workspace runtime when available. For a client-specific or non-recurring proposal, copy the generator into the working offer folder and adapt the copy; keep the bundled skill portable and generic.

## References

Read `references/offer-elements.md` when the offer needs detailed service modules, pricing mode rules, focused or complete media allocation options, scope-specific channel rules, CSS Partner wording, PPC KPI wording, cover-layout guidance, or final validation rules.

## Workflow

1. Identify the offer archetype, client language, currency, VAT convention, and whether media is paid by the client directly or invoiced by ProClick.
2. Copy and adapt `scripts/generate_offer.py` in the working offer folder when client-specific content is needed. Do not bake one client's scope, price, date, or company name back into the bundled template.
3. Keep the visual system intact: cream background, dark strategy spread, red accent, white cards, dark conclusion blocks.
4. Update client-specific text, service wording, fees, payment terms, scope boundaries, KPIs, and company/contact data.
5. Match the requested tax mode consistently: `TVA inclus`, `net + TVA`, `+ VAT`, or the language-appropriate equivalent. Do not infer that a media budget has the same tax treatment as agency services.
6. Generate the PDF into the current workspace `outputs/` directory.
7. Render the final PDF to PNG with `pdftoppm` and inspect every affected page before delivering.

## Content Pattern

Choose a structure that fits the offer archetype rather than forcing every offer into a six-page PPC proposal.

### Recurring PPC launch or management

1. Cover: client name, offer title, total budget, service fee, media budget, objective.
2. Services: six-card grid with service titles and concise details.
3. Strategy: dark page with three-stage launch approach.
4. Channels or media allocation: either a channel-role table or a budget-allocation table, depending on the brief.
5. Commercial model: setup fee, monthly fee, media budget, and scope notes.
6. KPI/reporting/company: PPC KPIs, reporting cadence, scope notes, company data.

### Standalone audit

1. Cover: audit scope, price, delivery window, and audit systems.
2. Audit workstreams: for example Google Ads, Meta, GA4/GTM, Merchant/feed, SEO, or cross-channel measurement.
3. Methodology and required access, normally read-only for an audit.
4. Deliverables and a prioritized 30/60/90-day plan or equivalent decision framework.
5. Commercial terms: audit fee, milestones, validity, and any conditional credit toward a future engagement.

### Fixed-scope implementation or migration

1. Cover: project result, fixed price, and timeline.
2. Scope and deliverables, including what is explicitly excluded.
3. Delivery phases and client responsibilities or acceptance points.
4. Commercial table with fixed fee and payment milestones that reconcile to the project total.
5. Launch, warranty/hypercare, and separately approved ongoing support if applicable.

## Default Offer Elements

- Use one pricing mode consistently across the document:
  - `TVA inclus` as primary values with net values below, or
  - `net + TVA` as primary values when the user explicitly asks for prices without VAT.
- Choose the media mix by objective, budget, and scope: use a focused mix for concentrated launch pressure, or a broader mix only when the brief explicitly includes those channels.
- Mention CSS Partner support in the feed/Shopping service card when Google Shopping is included.
- Keep the first-month strategy realistic: validate tracking, messages, and products sellable for promotion and sales before scaling.
- If channels are explicitly excluded from the scope, remove them from both narrative text and channel tables.
- On the cover, keep headline text in available headroom and pricing cards below faces. Do not obscure faces or crop team members.
- Distinguish one-time setup/audit/project fees from recurring management fees. If first-month and month-two pricing differ, show both phases in the cover, commercial table, and summary block.
- Treat platform media as a separate cash flow when the client pays Google, Meta, TikTok, or another platform directly. State the payment path rather than automatically attaching agency VAT language to it.
- Use an audit credit only when it is explicit, conditional, and commercially approved; name the trigger and whether the fee is credited or waived.
- For a project with staged payments, ensure each milestone percentage and amount adds to the stated project total.
- Carry the chosen document language through headings, tax labels, commercial terms, and any appendix. Use a font that has been checked for that language; do not silently strip meaningful diacritics from Romanian or Hungarian copy.

## Style Rules

- Keep Romanian offer text professional and direct.
- Prefer concise service descriptions over long paragraphs.
- Focus KPI tables on PPC metrics unless the user asks for broader business KPIs.
- Keep monetary values internally consistent across cover, media allocation, and narrative text.
- Keep scope wording internally consistent across service cards, channel tables, commercial page, and cover summary.
- For audit and migration offers, replace irrelevant media-allocation and recurring-KPI pages with methodology, deliverables, access, timeline, and payment information.
- State client dependencies where they affect delivery: account access, tracking, product feed, site/platform access, creative assets, approvals, or data exports.
- Separate included work, optional work, and exclusions. Examples of separately priced work include creative production, content, complex feed fixes, custom development, and out-of-scope integrations.
- Preserve proClick company details unless the user explicitly changes them:
  `INTELLIGENT DIGITAL MARKETING SRL`, `CUI: RO16554762`, `Piata Victoriei nr. 5, Targu-Mures, Romania`, `contact@proclick.ro`, `+40 744 692 880`, `proclick.ro`.
