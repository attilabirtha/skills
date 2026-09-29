# Attila Birtha — WhatsApp style

Derived from **387 sent messages across 29 chats** (sampled 2026-09-29 via the n8n
`get-whatsapp-channel-history` workflow).

WhatsApp is a **different register from email**: no greeting ceremony, no signature,
ASCII only, and much shorter. Do not carry email formality over.

---

## Measured shape

| Metric | Value |
|---|---|
| Median length | **3 words** |
| Mean length | 5.0 words |
| ≤ 3 words | **53%** |
| ≤ 6 words | 76% |
| ≤ 12 words | 94% |
| Longest | 65 words (rare, purposeful) |
| Contains a smiley/emoji | 16% |

**No signature. Ever.** Unlike email, nothing is appended.

---

## The rules

1. **3 words is the target, not the minimum.** Half of all messages are ≤3 words.
2. **No greeting when continuing a conversation.** Greeting only when opening one.
3. **No diacritics.** ASCII Hungarian and Romanian throughout: *koszonom, erteni, termekekre, naptarba, feljottem*.
4. **Smileys are typed, not emoji:** `:)`, `:))`, `:)))`, `:))))`, occasionally `:))\`.
   Unicode 🙂 appears but is much rarer.
5. **Laughter is spelled:** `hahaha`.
6. **Languages mix freely, even inside one sentence.** Hungarian and Romanian in the same chat.
7. **Typos and shortenings are natural** — reproduce the register, don't polish it:
   *akko* (akkor), *adsig* (addig), *par prc* (pár perc), *teledonszam*, *vakacion*, *m4?*
8. **Bare data drops** — a URL, an email, a file, no commentary: `edebereczki@gmail.com`, `lorandd@gmail.com#pwd`, raw links.
9. **When he asks for something, it stays a single line:** *"Nezd meg legyszives"* · *"Salut, vezi slack"*

---

## Openers actually used

`Szeva.` · `Szeva` · `hali` · `Hali.` · `hy` · `hi` · `Hi` · `Szia.` · `szia.` ·
`Salut,` · `Buna dimineata` · `Jo reggelt`

Sometimes the greeting fuses with the message — **no space**: `szia.meddig?`

---

## Acknowledgements (the most common message type)

`ok` · `oki` · `igen` · `da` · `jo` · `good` · `All good` · `Persze` · `mukodik` ·
`most` · `par prc` · `akko jovok` · `Feljottem` · `Zsenialis` · `aztaaaaa` · `uhh` · `xar`

---

## Business asks, WhatsApp-terse

> `Nezd meg legyszives`
> `Koszi. Kuld At kerlek a konfirmalast Danielanak is. Olvasd el a papirt ha kell vmit meg csinaljunk`
> `ne valtoztassak arakat teves termekekre`
> `Le kell elenorizd a termekekkel egyutt`
> `jelentkezik ujra 15 ora utan`
> `Salut, vezi slack`
> `Multumesc pt. discutie.`
> `Szia. Eden hivja Dorat at delutanra, ha nincs programotok`

Note the imperative form — *"Nezd meg"*, *"Kuld At"*, *"Olvasd el"* — direct, no cushioning.

---

## Longer messages — when they happen

Only when the content genuinely requires it: instructions, explanations, emotional repair,
or pasted reference text. Even then, plain and unformatted:

> `Meg kell erteni eloszor is. Ha valami nem sikerult az valoszinuleg hianyos adatok (kodok miatt)`

> `In nici un caz nu mi-am propus sa te ranesc. In capul meu probabil are alta conotatie, fata de ce a ajuns la tine.`

> `Tegyuk be a naptarba, maskepp nem tortenik meg. 🙂 Iroda, kavehaz, edzoterem, barmi megy. Ha ezen a heten inkabb delelott.`

> `Pe serviciile PPC o luna iti pot Storna daca te ajuta. In rest e foame si la noi, si sustinem din linia de credit la linia de plutire.`

---

## Anti-patterns — he never does this on WhatsApp

- ❌ A signature block (that's email only)
- ❌ `Bună ziua,` / `Dear …` — far too formal
- ❌ Diacritics
- ❌ Bullet lists and headings
- ❌ Multi-paragraph messages without a reason
- ❌ Correcting his own typos

---

## Email vs WhatsApp — the contrast

| | Email | WhatsApp |
|---|---|---|
| Median length | 1–3 sentences | **3 words** |
| Greeting | always | only when opening |
| Signature | **always** | **never** |
| Diacritics | by register (formal RO yes) | **never** |
| Smileys | almost none | 16% (`:)` `:))`) |
| Polish | fairly clean | typos kept |
