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

## Signature block (verbatim)

```
https://www.proclick.eu/

Attila Birtha

Managing Partner

Mobile: +40 744 692 880

Email: attila.birtha@proclick.ro

Address: P-ța Victoriei nr. 5, Târgu Mureș, ROMANIA

Follow us on:  https://www.facebook.com/proclick.eu
https://www.instagram.com/proclick_eu/  https://twitter.com/proClick_eu
http://www.linkedin.com/company/3019254
```

## Gotcha

When drafting through the Gmail API, his Gmail **auto-signature is not applied** — so the
block must be written into the body, as above. Flag a possible duplicate signature if he
sends from the Gmail UI with its own signature enabled.

## Language of the record

Anything the counterparty can see — email body, **and any calendar event or CRM record
created alongside it** — is written in **their** language. See #9 in
`comms-to-odoo-design.md`. Internal notes stay English.

## Reference

- `references/writing-style.md` — email: full guide with templates and anti-patterns.
- `references/whatsapp-style.md` — WhatsApp: measured 3-word style, smiley conventions,
  language mixing, no-signature rule.
