# Vinohrady #504 — Listing package for Claude Design

Two-page A4 presentation deck for a turnkey studio in **Praha 2 —
Královské Vinohrady**, operating as a 4.89★ Guest-favourite Airbnb
("Friendly apartments in Prague #504" under Artem's managed program).

**Asking price: 5 600 000 CZK.**
**Current long-term rent: 19 800 CZK/month all-in** (incl. 2 800 CZK
service charges → 17 000 CZK net) ⇒ **4.24 % gross yield / 3.64 % on net rent.**
**STR upside:** 180 reviews at 4.89★, "Guest favourite" badge, 5.0 check-in.

---

## Read order for Claude Design

0. **`MASTER-BRIEF.md`** — single source of truth, facts + constraints.
1. **`brief/claude-design-form.md`** — pre-filled Claude Design setup form.
2. **`brief/design-system.md`** — palette, typography, layout, voice.
3. **`brief/fact-sheet.md`** — spec card, table-ready.
4. **`brief/copy.cs.md` / `copy.ru.md` / `copy.en.md`** — trilingual copy.
5. **`source-photos/`** — 7 originals (phone JPEGs, turnkey condition). **These are the final deck assets** — no upscaling pipeline in this repo.
6. **`research/`** — sourced evidence for every number in the deck.

## Repository map

```
.
├── README.md                        you are here
├── MASTER-BRIEF.md                  subject, facts, agent matrix
├── brief/
│   ├── claude-design-form.md
│   ├── design-system.md             palette + typography + layout
│   ├── fact-sheet.md
│   ├── copy.cs.md                   (Czech primary)
│   ├── copy.ru.md                   (Russian secondary)
│   └── copy.en.md                   (English captions)
├── source-photos/                   7 originals (final deck assets)
│   ├── 01-facade.jpg
│   ├── 02-entrance-hall.jpg
│   ├── 03-stairwell-lift.jpg
│   ├── 04-kitchen-living.jpg
│   ├── 05-dining-nook.jpg
│   ├── 06-bedroom.jpg
│   └── 07-bathroom.jpg
├── research/
│   ├── 01-valuation-thesis.md       sourced 5.6 M CZK defense
│   ├── 02-comparables.md            3 comps from Vinohrady studios
│   ├── 03-neighborhood-map.md       transport + amenities + pin list
│   ├── 04-rental-yield.md           LTR vs STR yield scenarios
│   └── assets/                      comp screenshots + airbnb snapshot
└── .gitignore
```

## Design constraints

- Two-page A4 portrait, 300 DPI.
- Trilingual: Czech primary, Russian secondary, English captions.
- Palette: `#FAF8F4` / `#1C1B18` / `#C9A961` gold / `#4A5D3F` /
  `#8A8578` / `#E5DFD3` — identical to sister repo
  [`altajska-4-listing`](https://github.com/gtrush03/altajska-4-listing).
- Fonts: Playfair Display (headings), Inter (body),
  JetBrains Mono (numbers) — all on Google Fonts.
- Every number has a source citation in `/research`.
