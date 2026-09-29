---
name: birtha-writing-style
description: |
  Write emails and WhatsApp messages in Attila Birtha's personal voice — terse and direct,
  register-matched per channel. Covers Romanian (formal and informal), Hungarian and English.

  Triggers when asked to:
  - "draft an email", "write to <client>", "reply to this", "follow up with <client>"
  - "draft a WhatsApp reply", "reply on WhatsApp", "message <person>"
  - "write it in my style", "in Attila's voice", "make it sound like me"
  - draft any outbound mail on behalf of proclick.eu / proclick.ro / birtha.ro
---

# Attila Birtha — writing style

Applies to **any outbound email or message** written on Attila's behalf, in any language.

## Channel matters more than the person

He is a **different writer per channel**. Pick the register first, then read that reference.

| Channel | Register | Signature | Reference |
|---|---|---|---|
| **Email** | formal/informal by counterparty | **always** | `references/writing-style.md` |
| **WhatsApp** | terse — median **3 words** | **never** | `references/whatsapp-style.md` |

Do not carry email formality into WhatsApp, or WhatsApp terseness into a client email.

## Before writing

Read the reference for the channel. They contain per-type templates, measured stats,
real examples, and explicit anti-pattern lists. Do not invent the voice — copy it.

## Non-negotiables

1. **Body is 1–3 sentences.** Short replies are one sentence. Never a wall of text.
2. **No closing line.** The last sentence runs directly into the signature block.
   No "Best regards", no "Cu stimă" (unless deliberately writing a fully formal letter).
3. **The signature block is always present** — including on one-word replies and internal mail.
4. **Every mail carries a next step** — an ask, a commitment, or what he already did.
5. **Never open with pleasantries.** No "Hope you are well" / "Sper că sunteți bine".
6. **Never restate the thread** back to the reader.

## Match the register

| Counterparty | Greeting | Diacritics |
|---|---|---|
| RO formal (new/external client) | `Bună ziua,` | yes — *"Bună ziua… săptămâna"* |
| RO informal (partner, vendor, support) | `Salut,` / `Salut!` | dropped — *"Atasat regasesti… saptamana"* |
| Hungarian contact | `Szia,` | usually dropped |
| English | `Hi <FirstName>,` or `<FirstName>,` | `Thx`, `u` are in-character |
| Internal colleague | **none** | subject carries the message; body often empty |

## Drafting procedure

1. Identify the register from the counterparty and the thread tone.
2. Write the point in 1–3 sentences, with the next step explicit.
3. Append the signature block verbatim.
4. **Do not add a closing line.**
5. If the mail is a meeting brief, proposal, or agenda — longer **by design** — keep the
   greeting, the direct asks and the signature block; only the middle expands.

## Signature — always fetch, never copy

The signature is **HTML maintained with the website** and it changes over time.
**Never copy its values into a draft, and never hardcode them here.** Render it at write time:

```bash
~/.opencode/skill/birtha-writing-style/scripts/get-signature.sh          # attila (default)
~/.opencode/skill/birtha-writing-style/scripts/get-signature.sh hunor    # any colleague
```

It fetches the published file and prints a plain-text block ready to paste as the
email signature. Source order: **live site → local checkout fallback**.

### Canonical artefact

| | |
|---|---|
| GitHub | `attilabirtha/proclick.ro` → `public/signatures/*.html` |
| Local | `~/Development/proclick.ro/public/signatures/` |
| Live | `https://www.proclick.eu/signatures/attila` |

Team variants sit alongside: `hunor`, `claudiu`, `paula`, `daniela`, `andras`, `antonia`,
plus a legacy `attila_birtha`.

### Things that are easy to get wrong

- The site **308-redirects** `/signatures/<name>.html` → `/signatures/<name>`. Follow it
  (the script does).
- The block is a two-column HTML table: portrait with an `#E84C3C` divider, the proClick
  logo, then the detail lines and social icons.
- **The signature's email may differ from the address he sends from.** Use whatever the
  script prints — do not "correct" it.
- `assets/` carries **seasonal logo variants** (`proclick2x-xmas.png`,
  `proclick2x-hearts.png`). The HTML picks one; don't substitute filenames.
- Gmail does **not** apply the HTML signature to API-created drafts — that is why we render
  text. When he sends from the Gmail UI, its own signature may also apply; flag a possible
  duplicate rather than guessing.

## Language of the record

Anything the counterparty can see — the email body, **and any calendar event or CRM record
created alongside it** — is written in **their** language: Romanian for RO contacts,
Hungarian for HU contacts, English only when they write in English. Internal notes stay
English. This applies to event titles and descriptions, not just the mail.

## Reference

- `references/writing-style.md` — email: full guide with templates and anti-patterns.
- `references/whatsapp-style.md` — WhatsApp: measured 3-word style, smiley conventions,
  language mixing, no-signature rule.
