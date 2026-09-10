---
name: proclick-presentation
description: Create or restyle proClick-branded presentations, pitch decks, case studies, and service or product briefings using the proClick brand book and official assets. Use for proClick slides or presentation requests; standalone commercial offer PDFs belong to proclick-price-offer.
---

# proClick Presentation

Apply proClick identity to the user's presentation brief. This skill provides the brand and layout system; it does not substitute agency promotion for the requested subject.

## Sources and precedence

Read [the brand book](references/brand-book.md) before authoring. Use [design tokens](assets/brand-tokens.json) for exact values and [slide layouts](references/slide-layouts.md) for composition guidance.

The user's explicit direction and supplied template take precedence. Otherwise use the **presentation** palette, derived from the existing agency deck. Use the **offer** palette only when matching a price-offer reference, and the **web** palette only when matching the website. Keep a selected palette coherent across a new deck. Preserve existing variants when editing an existing deck.

Use the bundled official logos and photography. Inspect a supplied screenshot, photo, or deck before deciding how to crop or place it. Source facts and figures from the current brief, not from examples or remembered agency claims.

## Authoring workflow

1. Infer audience, language, format, and objective from the current request. When unspecified, use the brief's language and editable 16:9 PowerPoint. Honor requests for PDF, Google Slides, or HTML rather than forcing PowerPoint.
2. Select the smallest narrative that answers the audience's questions. A service presentation may cover problem, proposed workflow, scope, evidence, delivery plan, and next step. Include pricing only when the user requests it or supplies it as part of the brief. Do not automatically add paid-media channels, budgets, or a six-card service grid to an unrelated deck.
3. Use the available presentation authoring capability. In Codex with the Presentations skill installed, read its current implementation and validation guidance and use its supported engine. Do not copy API wrappers from historical agency slide scripts. If an editable format cannot be produced, explain the limitation before changing formats.
4. Use the layout reference as a set of adaptable compositions. Keep headline, captions, charts, tables, and required diagrams editable. A mockup screenshot may remain a raster image, with its interpretation in separate editable text.
5. For mockup-heavy decks, alternate overview, full-width screenshot, and one focused detail. Show the app at readable scale. Label synthetic screens and data as illustrative. A generated interface does not establish implemented functionality.
6. Put sources for claims and assets in slide notes, and visible assumptions beside any claim that depends on them. Review typography, source fidelity, image proportions, text fit, and factual consistency on every rendered slide.
7. Save a new version unless replacement is requested. Return the actual requested deck. Add a PDF companion only when requested or useful to the brief.

## Brand-specific decisions

- Write the brand as **proClick** in prose. Use the original raster logo instead of recreating the wordmark with text, drawing it, or asking an image model to regenerate it.
- Default new slides to warm paper, near-black text, and restrained coral accents. Use charcoal for section breaks or strategy slides. Pale green is an optional recommendation surface, not decoration on every page.
- The reference agency deck uses Aptos Display headings and Aptos body. Verify availability. Arial is the practical fallback already used in the offer generator; record any substitution, rather than assuming that a font is installed.
- Keep all pictured team members inside the frame and place type away from faces. Prefer a contained wide photo or an uncropped photo beside text over a forced full-bleed crop.
- Preserve the user's language and proper diacritics. The old offer generator's ASCII conversion is an implementation limitation, not a brand rule.
- Do not carry old agency metrics, partner badges, client endorsements, or commercial rates into a new deck without current supporting evidence. Client marketing results cannot substantiate an AI product result.
- For pricing slides, keep currency and tax basis explicit and consistent. Keep service fees separate from media or platform usage costs when those categories apply. Do not invent a VAT rate or treat an example fee as an approved price.

## Bundled resources

- `assets/proclick_logo.png`: light-background logo.
- `assets/proclick_logo_white.png`: dark-background logo.
- `assets/proclick_team_wide.jpg`: wide team photography.
- `assets/proclick_team_cover_full.png`: portrait full-team composition.
- `references/brand-book.md`: canonical foundation, mode rules, voice, and contact record.
- `assets/brand-tokens.json`: machine-readable styles, with sources separated from new defaults.
- `references/slide-layouts.md`: reusable cover, evidence, process, screenshot, and closing layouts.
- `references/sources.json`: provenance and source hashes for this version.

For the intended division of responsibilities: use this skill for presentations and the existing `proclick-price-offer` for standalone commercial offer PDFs. Reading this skill never grants permission to publish, send, or modify external accounts.
