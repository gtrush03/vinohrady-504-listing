# Claude Design setup form — copy-paste answers

The three text fields on the Claude Design form, pre-filled. Paste each
block into the corresponding field verbatim. GitHub repo is already
linked to this listing's repo.

---

## 📋 Field 1 — Company name and blurb

```
Vinohrady #504 — Prague 2 Studio Listing

A two-page A4 real-estate listing for a compact turnkey studio (1+kk)
in Královské Vinohrady, Praha 2. Historic late-19th-/early-20th-century
neoclassical apartment house, fully renovated, retrofitted elevator.
Currently tenanted long-term at 19 800 CZK / month all-in (of which
2 800 CZK are service charges), yielding 4,24 % gross on the asking
price. Also Airbnb-proven under Artem's "Friendly apartments in Prague"
program with a 4,89 / 5 rating across 180 reviews and a "Guest
favourite" badge. Asking price 5 600 000 CZK (fixed, single figure —
not a range). Target buyer: Czech- and Russian-speaking private
investor or EU pied-à-terre buyer. Deck tone is calm, editorial,
data-rich — proof-not-hype. Every number in the deck is backed by
sourced research in /research and must be cited inline. Exact m² is
TBD; the deck uses the verbal label "kompaktní studio / компактная
студия / compact studio" until the m² is confirmed.
```

---

## 🎨 Field 2 — Fonts, logos and assets (what to upload)

All three fonts are free on Google Fonts — download the `.ttf` bundles
from these links and drag them into the upload area:

- **Playfair Display** (headings) — https://fonts.google.com/specimen/Playfair+Display → click "Download family"
- **Inter** (body) — https://fonts.google.com/specimen/Inter → click "Download family"
- **JetBrains Mono** (numbers) — https://fonts.google.com/specimen/JetBrains+Mono → click "Download family"

**No logo exists** — this is a one-off listing for a private sale, no
brand mark is needed. If the deck requires a wordmark, set
`Vinohrady #504` in Playfair Display 900.

**Colour swatches** (no upload needed, listed in the notes field below):

| Token       | Hex       |
|-------------|-----------|
| Background  | `#FAF8F4` |
| Ink         | `#1C1B18` |
| Accent gold | `#C9A961` |
| Leaf green  | `#4A5D3F` |
| Muted grey  | `#8A8578` |
| Hairline    | `#E5DFD3` |

---

## 📝 Field 3 — Any other notes?

Paste this entire block into the "Any other notes?" textarea. It covers
layout, voice, content rules, and repo read order.

````markdown
# Design direction — Vinohrady #504

## Output format
- **Two-page A4 portrait PDF, 300 DPI**, plus one PNG hero thumbnail.
- 8 mm margins, no bleed required.
- Trilingual: **Czech primary**, Russian secondary (equal weight,
  smaller), English caption tier. Do not duplicate full paragraphs in
  all three — only the headline and spec labels get all three
  languages; the lead paragraph is CS + short RU line + short EN line.

## Palette (strict)
- `--bg` `#FAF8F4` (warm off-white)
- `--ink` `#1C1B18` (near-black body text)
- `--accent` `#C9A961` (brushed gold — used ONLY on the asking price,
  the "our listing" bar in the valuation chart, and the hairline rule
  under each section title)
- `--secondary` `#4A5D3F` (muted leaf-green — map, yield chips, STR
  proof panel "Guest favourite" chip)
- `--muted` `#8A8578` (captions, sources, meta)
- `--line` `#E5DFD3` (hairline dividers)

## Typography (strict)
- Headings: **Playfair Display** 700 / 900 (serif, editorial)
- Body: **Inter** 400 / 500 (neutral sans, reads well in CS/RU/EN)
- Numbers: **JetBrains Mono** 500 (tabular alignment for prices / m²)
- Caption: Inter 400, tracking +2%

Size scale for A4: H1 64pt, H2 24pt, H3 14pt, body 10.5pt, caption 8pt,
price 48pt JetBrains Mono in gold.

## Page 1 layout
1. **Top 45 %:** full-bleed hero image. Use
   `source-photos/01-facade.jpg` (the ornate neoclassical street
   façade — the strongest anchor for a Vinohrady address) as the hero.
   Overlay typography: "Vinohrady #504" in 64pt Playfair in off-white
   (`--bg` color), bottom-left, with caption line
   `PRAHA 2 · KRÁLOVSKÉ VINOHRADY · KOMPAKTNÍ STUDIO` beneath in gold
   (`--accent`), letter-spaced all-caps.
2. **Middle 35 %:** two columns.
   - Left 60 %: spec block from `brief/fact-sheet.md`, rendered as a
     dense two-column label/value list. Labels in `--muted`, values in
     `--ink`, numbers in JetBrains Mono.
   - Right 40 %: the asking price block.
     - **`5 600 000 CZK`** at 48pt JetBrains Mono in `--accent` gold.
       Single fixed figure — do NOT render a range.
     - Below in small muted: `CZK/m² — upřesní se po potvrzení m²`
       (placeholder; m² is TBD).
     - Below: `Hrubý výnos 4,24 % p.a.`.
     - Thin gold hairline separator.
3. **Bottom 20 %:** 3-sentence editorial lead from `brief/copy.cs.md`
   (CS) + one-sentence RU line (`brief/copy.ru.md`) + one-sentence EN
   caption (`brief/copy.en.md`).

## Page 2 layout
1. **Top 35 %:** 3-comp comparison table from
   `research/02-comparables.md`. Czech only. Tabular mono numerals.
   The "our listing" row is highlighted with a thin gold top + bottom
   rule; no fill. Valuation bar chart renders once the comp set is
   locked — same palette, our-listing bar in `--accent`.
2. **Middle 25 %:** neighborhood map. Pin list + caption from
   `research/03-neighborhood-map.md`. Caption CS + 1-line RU + 1-line
   EN. Transit, walk times to Old Town / Wenceslas Sq., Riegrovy sady,
   Havlíčkovy sady, Manifesto Market.
3. **Bottom 25 % — STR PROOF PANEL (new, not in sister repo):**
   horizontal band presenting the Airbnb track record as hard data.
   - Left third: large figure **`4,89 / 5`** in JetBrains Mono 36 pt,
     `--ink`. Below in muted caption: `180 recenzí`. Small
     `--secondary` leaf-green chip reading `Guest favourite`.
   - Middle third: three mini-stats in a row, JetBrains Mono 18 pt:
     `Check-in 5,0` · `Location 4,8` · `Value 4,8`.
   - Right third: 1-line caption, 10.5 pt Inter —
     *"Průkazná STR výkonnost — Airbnb #504"*. RU line:
     *"Подтверждённые показатели STR — Airbnb #504"*. EN line:
     *"Proven STR performance — Airbnb #504"*.
   - No gold in this band. The leaf-green chip is the only accent.

## Bottom of page 2 — sources footer
Single line, 8pt `--muted`:
`Zdroje: sreality.cz · bezrealitky.cz · ČBA Monitor Q1 2026 · Deloitte
Real Index · Airbnb veřejný výpis #504 · duben 2026`

## Image policy (IMPORTANT)
- **`source-photos/` are the final deck assets.** No upscaling, no AI
  enhancement, no Nano Banana pipeline. Use the 7 phone-shot JPEGs
  as-is. Do NOT apply aggressive filters, HDR, or "enhancement" —
  keep natural. Crop if the layout needs it; do not restyle.
- There are **7 source photos**, all in `source-photos/`:
  `01-facade.jpg`, `02-entrance-hall.jpg`, `03-stairwell-lift.jpg`,
  `04-kitchen-living.jpg`, `05-dining-nook.jpg`, `06-bedroom.jpg`,
  `07-bathroom.jpg`.
- Hero image is **`source-photos/01-facade.jpg`** (the ornate
  neoclassical street façade). Do not pick a different image for the
  hero.
- For a secondary gallery image on page 1 (if the layout calls for
  one), use `02-entrance-hall.jpg` or `04-kitchen-living.jpg`.

## Voice rules
- **No superlatives.** "Zrekonstruovaný činžovní dům v Královských
  Vinohradech" is correct. "Luxurious" / "exclusive" / "unique
  opportunity" are banned.
- **No emojis. No all-caps shouting.**
- **Numbers rule.** Any claim that can have a number has one. Any
  number has a source citation (footnote-style `¹`, `²`).
- **Czech number formatting:** space as thousands separator
  (`5 600 000 CZK`), comma as decimal (`4,24 %`), CZK trails.
- **Russian number formatting:** same rules, correct cases.
- **English number formatting:** commas as thousands
  (`5,600,000 CZK`).
- **The price 5 600 000 CZK is a single fixed figure, not a range.**
  Do not add a from/to spread.
- **Size (m²) is TBD.** Use the verbal label "kompaktní studio /
  компактная студия / compact studio" until confirmed. CZK/m² renders
  as a labelled placeholder, not a fabricated number.
- **Review quotes, if used at all, must be verbatim from
  `research/assets/airbnb-reference-listing.png`.** Do not paraphrase.
  Do not invent.

## Tonal benchmark
The host (Artem) has a live Airbnb listing in the exact Vinohrady
program this unit sits in. Read his blurb as the voice reference —
translated from Airbnb host register into sale-deck register.
Reference URL:
`https://www.airbnb.co.uk/rooms/1097826905142301323`
Local snapshot: `research/assets/airbnb-reference-listing.png`.

## Repo read order
1. `MASTER-BRIEF.md` — fixed facts, non-negotiables
2. `brief/design-system.md` — the full version of these rules
3. `brief/fact-sheet.md` — trilingual spec table, ready to paste
4. `brief/copy.cs.md` / `copy.ru.md` / `copy.en.md` — trilingual copy
5. `research/01-valuation-thesis.md` — the 5,6 M CZK argument with
   20 / 25 / 30 m² scenarios
6. `research/02-comparables.md` — 3-comp table + screenshots
7. `research/03-neighborhood-map.md` — pin list for the map
8. `research/04-rental-yield.md` — LTR 4,24 % gross / 3,64 % net math
   + STR alternative scenario
9. `research/assets/airbnb-reference-listing.png` — full-page Airbnb
   snapshot (tone + review quotes reference)
10. `source-photos/` — 7 photos; hero is `01-facade.jpg`

## Hard rules for the deck
- If a claim doesn't appear in `research/*.md` or on the Airbnb
  snapshot, don't put it in the deck.
- The price is **5 600 000 CZK** — a single fixed figure, never a
  range.
- The asking price gets the ONLY use of gold at 48pt. Do not gild
  anything else that size.
- Do NOT claim amenities that are not on the Airbnb public listing
  (no A/C, no parking — those are not present).
- Sources line at the bottom of page 2 is mandatory.
- The STR proof panel is mandatory on page 2 — it is the proof leg of
  the investment thesis.
````

---

## That's it

The three fields above cover the whole form. GitHub repo is already
linked so Claude Design will pull everything else automatically from
the Vinohrady #504 listing repo.
