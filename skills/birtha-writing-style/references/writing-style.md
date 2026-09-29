# Attila Birtha — email writing style (full reference)

Derived from ~30 sent messages, Sep 2026 (`attila.birtha@proclick.ro`).
Goal: mail written by an agent should be indistinguishable from his own.

---

## TL;DR rules

1. **Body is 1–3 sentences.** Often one. Never a paragraph of context.
2. **No closing line.** The last sentence is followed directly by the signature block.
3. **Signature block is always present** — even on a one-word reply (`Achitat.`) and internal mail.
4. **Every mail has a next step** — an ask, a commitment, or "I already did X".
5. **Never restate the thread.** He answers the question and stops.
6. **Never open with pleasantries.** No "Hope you are well", no "I hope this finds you".

---

## Greeting by register

| Register | Greeting |
|---|---|
| RO formal (new/external client) | `Bună ziua,` |
| RO informal (existing partner, vendor, support) | `Salut,` / `Salut!` |
| HU — **new** contact | `Jó napot,` |
| HU — already known | `Szia,` |
| HU — personal / friend | `Szia` |
| EN | `Hi <FirstName>,` or just `<FirstName>,` |
| Internal (colleague) | **no greeting at all** — often no body either |

**Closings:** usually **none**. When casual: `Koszi`, `Thx`.

---

## Language & diacritics

Inconsistent by design — match the register, not a rule:

- **RO formal** → proper diacritics: *"Bună ziua… Ne bucurăm că doriți să reluăm discuțiile… mă pot adapta după programul dumneavoastră"*
- **RO informal** → diacritics dropped: *"Atasat regasesti oferta… Sa-mi dai un ok te rog pe mail si dau la colegi de saptamana viitoare."*
- **HU** → diacritics dropped: *"Kertem a bankot nezze meg. En most repulok :D"*
- **EN** → abbreviations and first names: *"Thx for your mail."* · *"What information do **u** need about this project?"*

The EN shortcuts **"u"** and **"Thx"** are in-character — do not "correct" them.

**Emoji:** rare. `:D` appears in casual/personal mail only.

---

## Signature (always present — fetch it, never copy)

The signature is **HTML maintained with the site and it changes**, so it is not reproduced
here. Render it at write time:

```bash
~/.opencode/skill/birtha-writing-style/scripts/get-signature.sh            # attila
~/.opencode/skill/birtha-writing-style/scripts/get-signature.sh <name>     # any colleague
```

Canonical artefact: `attilabirtha/proclick.ro` → `public/signatures/*.html`
(live: `https://www.proclick.eu/signatures/attila`). See SKILL.md for the full notes —
redirects, seasonal logos, and the fact that the signature's email may differ from the
address he sends from.

The block appears on **internal** mail and on **one-word** replies — never omit it for
shortness, and never type it from memory.

---

## Subject lines

- Replies keep `Re:`. Forwards keep `Fwd:`.
- New business mail: **lowercase, descriptive, zero fluff** → `oferta de pret Audit PPC & Tracking`
- Internal HU: terse, lowercase → `arhivatorul szerzodes modositasok`
- Often the **subject carries the whole message**; the body is just signature + attachment.

---

## Templates per type

**Proposal / offer sent**
> `Salut,`
> `Atasat regasesti oferta pentru <X>.`
> `Sa-mi dai un ok te rog pe mail si dau la colegi de saptamana viitoare.`

**Meeting confirmation** (confirm + state what he already did)
> `Da, vineri de la 11:00 este ok pentru noi.`
> `V-am și trimis invitația.`

**Soft decline + alternatives**
> `Din păcate, miercuri nu este o zi potrivită pentru mine.`
> `Săptămâna aceasta mă pot adapta după programul dumneavoastră fie astăzi, fie vineri.`

**Explaining a change** (e.g. someone dropped from CC)
> `Eu nu mai sunt asociat în agenția Franc, prin urmare nu i-am mai inclus în CC pe foștii mei colegi.`

**Vendor / admin confirmation** — one word:
> `Achitat.`

**Payment / commitment (EN)**
> `Adam,`
> `Thx for your mail. Next time cc also suport@proclick.ro.`
> `We'll make sure funds will be available tomorrow.`

**Enquiry reply (EN)** — two direct questions:
> `Hi Jeroen,`
> `What information do u need about this project?`
> `Would u like to have an online meet and discuss briefly about the possible implementation?`

**External partner re-engagement (RO, warmer)**
> `Bună ziua,`
> `Ne bucurăm că doriți să reluăm discuțiile; suntem în continuare interesați de proiect.`

---

## Habits worth copying

- **Corrects the counterparty's process politely but flatly:** *"Next time cc also suport@proclick.ro."*
- **Requests acknowledgement:** *"Sa-mi dai un ok te rog pe mail…"*
- **Names the follow-up owner and timing:** *"…dau la colegi de saptamana viitoare."*
- **Warm only when reviving a relationship**, not as an opener.
- **Uses colloquial tags with vendors:** *"…nu ne folosim de IP-ul dedicat asai?"*

## Anti-patterns — he never does this

- ❌ More than ~3 sentences in the body
- ❌ "I hope this email finds you well" / "Sper că sunteți bine"
- ❌ Re-summarising the thread back to the reader
- ❌ A closing line ("Best regards", "Cu stimă") — **except** a deliberately formal letter
- ❌ Long apologies — `Din păcate, …` and move on
- ❌ Bullet lists in short replies (bullets appear only in offers / scope / agenda documents)
- ❌ Emoji outside casual or personal mail

---

## When longer is correct

Meeting briefs, proposals, agendas and scopes **are** longer. There, keep the greeting, the
direct asks and the signature block — only the middle expands. The invitation draft for
`driedfruits.ro` (2026-09-29) is the reference example: greeting → confirmation → Meet link →
agenda → what to prepare → next step → signature. **No closing line.**
