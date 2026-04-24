# Design-system brief — Vinohrady #504 Listing

This file maps 1:1 to the **Claude Design** setup form. Paste these answers
directly into the form when linking this repo.

---

## Company / Design-system name

**Vinohrady #504 — Prague 2 Studio Listing**

## Blurb

A two-page premium listing for a compact turnkey studio (1+kk) in
**Královské Vinohrady, Praha 2**. Historic late-19th-/early-20th-century
neoclassical apartment house, fully renovated, retrofitted elevator.
Currently tenanted long-term; Airbnb-proven under Artem's "Friendly
apartments in Prague" program with a documented **4,89 / 5** rating
across **180 reviews** and a **Guest favourite** badge. Asking price
**5 600 000 CZK** (fixed). Target buyer: Czech- and Russian-speaking
private investor, or EU pied-à-terre buyer who wants an STR-optional
asset that already pays for itself as LTR. Tone: calm, editorial,
data-rich; proof-not-hype. Every number sourced.

## Deck output spec

- **Format:** A4 portrait
- **Pages:** 2 max (not 1 — trilingual copy + STR proof panel need the room)
- **Bleed / margin:** 8 mm margin, no bleed required
- **Export:** PDF at 300 DPI + PNG hero thumbnail

## Languages — trilingual CS + RU + EN

- **Primary (headline + running body):** Czech (CS). Buyer decisions and
  legal signing happen in Czech; local-market listings on sreality/idnes
  are Czech-native.
- **Secondary (equal weight, smaller):** Russian (RU). Buyer pool for the
  seller's network is Russian-speaking.
- **Tertiary (caption only):** English (EN). For broader investor reach.
- **Per section:** the headline renders in CZ, a RU line below, and an EN
  caption in small muted type. Do NOT duplicate full paragraphs — only
  the spec labels + headline need all three languages.

## Palette (identical to sister repo — warm paper, leaf, gold)

| Token       | Hex       | Use |
|-------------|-----------|-----|
| `--bg`      | `#FAF8F4` | page background (warm off-white paper) |
| `--ink`     | `#1C1B18` | body text, numbers, dense info |
| `--accent`  | `#C9A961` | brushed gold — price, section rules, pins |
| `--secondary` | `#4A5D3F` | muted leaf-green — map, yield chips, STR chip |
| `--muted`   | `#8A8578` | warm grey — captions, sources, meta |
| `--line`    | `#E5DFD3` | hairline dividers |

**Rule:** gold is earned — used only on the asking-price figure, the
valuation-chart bar representing our ask, and the one-line horizontal
separator under each section title. Do not gild anything else.

## Typography

| Role      | Family             | Weight | Why |
|-----------|--------------------|--------|-----|
| Headings  | **Playfair Display** | 700 / 900 | Editorial serif, pairs with warm palette |
| Body      | **Inter**          | 400 / 500 | Neutral, reads well in CS/RU/EN |
| Numbers   | **JetBrains Mono** | 500 | Tabular alignment for prices and m² |
| Caption   | Inter              | 400, tracking +2% | Sources, meta, trilingual subtitles |

All three are free on Google Fonts; no licensing concerns.

**Size hierarchy (A4):**
- `H1` (cover): 64 pt Playfair
- `H2` (section): 24 pt Playfair
- `H3` (subsection): 14 pt Inter 600
- `body`: 10.5 pt Inter 400
- `caption`: 8 pt Inter 400
- `price`: 48 pt JetBrains Mono 500, `--accent` color

## Layout — two-page A4

### Page 1 — hero + headline valuation

1. **Top 45 %:** full-bleed hero image `source-photos/01-facade.jpg`
   (the ornate neoclassical street façade — the strongest anchor image
   for a Vinohrady address). Overlay typography:
   "Vinohrady #504" in 64 pt Playfair in off-white (`--bg` color),
   bottom-left, caption line `PRAHA 2 · KRÁLOVSKÉ VINOHRADY · KOMPAKTNÍ STUDIO`
   beneath in gold (`--accent`), letter-spaced all-caps.
2. **Middle 35 %:**
   - Left column (60 %): spec block from `brief/fact-sheet.md`, rendered
     as a two-column dense list with `--ink` values and `--muted` labels.
   - Right column (40 %): the asking price.
     - **`5 600 000 CZK`** in 48 pt JetBrains Mono, `--accent`.
     - Below in small muted type: `CZK/m² — upřesní se po potvrzení m²`
       *(CZK/m² placeholder — resolved once m² is confirmed)*.
     - Below that: `Hrubý výnos 4,24 % p.a.`.
     - A thin gold `--accent` rule separating price from the source tag.
3. **Bottom 20 %:** 3-sentence editorial lead from `brief/copy.cs.md`,
   with one Russian sentence and one English sentence immediately below
   (same point size, slightly lighter weight).

### Page 2 — evidence + map + STR proof

1. **Top 35 %:** 3-comp table from `research/02-comparables.md`
   (CS only, tabular mono numerals, gold highlight row for our listing).
   Valuation chart rendered once `02-comparables.md` is finalized.
2. **Middle 25 %:** the neighborhood map referencing
   `research/03-neighborhood-map.md` — pin list of metro / tram / walk
   times to Old Town, Wenceslas Sq., Riegrovy sady, Havlíčkovy sady,
   Manifesto Market. Caption in CS + one RU line + one EN line.
3. **Bottom 25 % — STR proof panel (NEW, not in sister repo):**
   a horizontal band presenting the Airbnb track record as hard data,
   not marketing copy. Layout:
   - Left third: large figure **`4,89 / 5`** in JetBrains Mono 36 pt,
     `--ink`. Below in muted caption: `180 recenzí`.
     Small `--secondary` leaf-green chip reading `Guest favourite`.
   - Middle third: three mini-stats in a row, JetBrains Mono 18 pt:
     `Check-in 5,0` · `Location 4,8` · `Value 4,8`.
   - Right third: 1-line caption, 10.5 pt Inter:
     *"Průkazná STR výkonnost — Airbnb #504"*.
     RU line below: *"Подтверждённые показатели STR — Airbnb #504"*.
     EN caption: *"Proven STR performance — Airbnb #504"*.
   No gold in this band. Leaf-green chip is the only accent.
4. **Bottom rule:** single-line `Sources:` footer listing the major
   source anchors (sreality, bezrealitky, Deloitte, Airbnb public
   listing snapshot) with link icons.

## Brand voice rules

- **No superlatives.** Say *"ověřená Airbnb výkonnost 4,89 / 5 napříč
  180 recenzemi"*. Don't say "luxurious" / "exclusive" / "unique".
- **No emojis, no all-caps shouting.**
- **Numbers rule.** Any claim that can have a number, has one. Any number
  has a source citation (`¹`, `²`, …).
- **Czech formatting:** space as thousands separator (`5 600 000 CZK`),
  comma as decimal (`4,24 %`), CZK trails the number.
- **Russian formatting:** same number rules, но падежи и язык — грамотный.
- **English formatting:** commas as thousands (`5,600,000 CZK`),
  "CZK" trails.

## Hard rule — size (m²)

Size (m²) is **TBD** until George confirms from cadastre / deed.
Use the verbal label **"kompaktní studio / компактная студия /
compact studio"** throughout copy and chrome until the m² is confirmed.
The valuation thesis in `research/01-valuation-thesis.md` presents
scenarios at 20 / 25 / 30 m² — the deck does not prefer one scenario;
it quotes the fixed **5 600 000 CZK** and leaves CZK/m² as a labelled
placeholder.

## Assets inventory

| Path | Purpose |
|------|---------|
| `source-photos/01-facade.jpg` | Street façade — neoclassical, bay windows, balconies · **HERO** |
| `source-photos/02-entrance-hall.jpg` | Grand entrance hall — colonnade, coffered ceiling, patterned tile |
| `source-photos/03-stairwell-lift.jpg` | Stairwell with original cast-iron balustrade + modern retrofit elevator |
| `source-photos/04-kitchen-living.jpg` | Open-plan kitchen/living — white kitchenette, induction hob, dining table |
| `source-photos/05-dining-nook.jpg` | Dining nook + framed line-art + oak chest + pendant light |
| `source-photos/06-bedroom.jpg` | Bedroom — double bed, tall windows, ornate neighbor-building views |
| `source-photos/07-bathroom.jpg` | Compact bathroom — quadrant shower, marble-tile, wall-hung WC, vanity |
| `research/01-valuation-thesis.md` | Evidence for the 5,6 M CZK price |
| `research/02-comparables.md` | 3-comp table + screenshots |
| `research/03-neighborhood-map.md` | Pin list + transit + amenities |
| `research/04-rental-yield.md` | LTR 4,24 % gross / 3,64 % net · STR alt-model |
| `research/assets/airbnb-reference-listing.png` | Full-page Airbnb snapshot (tone reference + review quotes) |
| `brief/fact-sheet.md` | Trilingual spec block (table-ready) |
| `brief/copy.cs.md` / `copy.ru.md` / `copy.en.md` | Trilingual copy |

## Other notes for Claude Design

- **`source-photos/` are the final deck assets.** No upscaling
  pipeline, no AI enhancement, no Nano Banana. Use the 7 phone JPEGs
  as-is. Do NOT apply aggressive filters, HDR, or "enhancement" — keep
  natural. If the layout calls for a crop, crop; do not restyle.
- **Hero image at top of page 1 must be `source-photos/01-facade.jpg`.**
  Do not pick a different image.
- If a fact doesn't have a source citation in the research files, don't
  include it in the deck.
- Prefer tables over prose for spec blocks. Prefer data over adjectives.
- The price **`5 600 000 CZK` is a single fixed figure**, not a range.
  Do not add a "from / to" spread.
- Review quotes — if used at all — must be verbatim from
  `research/assets/airbnb-reference-listing.png`. Do not paraphrase, do
  not invent.
