# MASTER BRIEF — Vinohrady #504 listing package

This is the single source of truth for every agent working in this repo.
Read this first. All deliverables must stay consistent with the facts here.

---

## Subject property

- **Unit:** "Friendly apartments in Prague (old town) #504" — studio / 1+kk
- **Neighborhood:** Praha 2 — Královské Vinohrady (Royal Vinohrady)
- **Building:** Late-19th-century / early-20th-century neoclassical
  apartment house, fully renovated. Decorative façade, historic entrance
  hall with colonnade and patterned floor tile, modern elevator
  retrofitted into the original iron-balustrade stairwell.
- **Unit layout:** 1 bedroom (open-plan living/kitchen + single room with
  double bed), 1 bathroom with walk-in shower and washing machine.
- **Typical size band for this kind of Vinohrady renovated studio:** 20 – 30 m².
  Exact m² is **TBD** — the valuation agent should produce scenarios for
  20 / 25 / 30 m² and flag this as the single open data point.
- **Furnishing:** turnkey, furnished (double bed, dining nook, sofa,
  TV, kitchenette with induction + built-in microwave/oven + fridge,
  washing machine, dedicated workspace, wardrobe rail).

## Headline numbers (FIXED — do not change)

- **Asking price: 5 600 000 CZK** (~ €225 000 / $240 000 at April 2026 FX).
- **Current long-term rent: 19 800 CZK/month — all-in**, of which
  **2 800 CZK/month are service charges / utilities** (fees paid by
  landlord out of the gross rent).
- **Net rent to landlord: 17 000 CZK/month** (= 19 800 − 2 800).
- **Implied gross yield on asking price: 4.24 % p.a.**
  (19 800 × 12 / 5 600 000 = 237 600 / 5 600 000 = 4.243 %).
- **Net yield on 17 000 CZK/mo (before tax/CapEx): 3.64 % p.a.**
  (17 000 × 12 / 5 600 000 = 204 000 / 5 600 000 = 3.643 %).

## STR (Airbnb) track record — the upside angle

Unit #504 has been on Airbnb under Artem's "Friendly apartments in
Prague" managed program. Public listing data (April 2026 snapshot):

- **4.89 / 5** average rating across **180 reviews**.
- **"Guest favourite"** badge ("one of the most loved homes on Airbnb").
- Sub-ratings: Check-in **5.0**, Communication **4.9**, Accuracy **4.9**,
  Cleanliness **4.8**, Location **4.8**, Value **4.8**.
- Host: **Artem** · "Business" account · 7 years hosting · 6 857 total
  reviews across all units · co-hosts Elena + Property (managed).
- Listing positioning: *"prestigious area of Prague Royal Vinohrady.
  Historical city center within walking distance, central public
  transport stop 5-min walk, many restaurants, bars, pubs and a market
  in the immediate vicinity."*
- House rules: check-in 15:00, checkout 10:00, 2 guests max.
- Self check-in via lockbox.
- 28 listed amenities including: Kitchen, WiFi, Dedicated workspace,
  TV, Lift, Washing machine, Hairdryer, Fridge, Long-term stays allowed,
  Carbon monoxide alarm.
- Reference URL (benchmark for tone + research depth):
  <https://www.airbnb.co.uk/rooms/1097826905142301323>

**Review themes (positive):** walkable to Old Town, close to metro/tram,
quiet street, responsive host, clean, well-equipped kitchen, good value.

**Review themes (minor critiques):** curtains don't fully block morning
light; can get warm in summer (no A/C — a fan would help).

## Photo inventory (in `source-photos/`)

| # | File | Subject |
|---|------|---------|
| 1 | `01-facade.jpg` | Street façade of the building — ornate neoclassical, bay windows, balconies |
| 2 | `02-entrance-hall.jpg` | Grand entrance hall — colonnade, coffered ceiling, patterned tile floor, original wooden double door |
| 3 | `03-stairwell-lift.jpg` | Stairwell with original cast-iron balustrade + modern retrofit stainless-steel elevator |
| 4 | `04-kitchen-living.jpg` | Open-plan kitchen/living — white IKEA-style kitchenette, induction hob, small dining table |
| 5 | `05-dining-nook.jpg` | Dining nook + framed line-art print + oak chest of drawers + pendant light |
| 6 | `06-bedroom.jpg` | Bedroom — double bed, tall windows, views to similar ornate neighboring building, folded towels (Airbnb turnover) |
| 7 | `07-bathroom.jpg` | Compact bathroom — quadrant shower, beige marble-tile, wall-hung toilet, vanity |

## Deliverable — the deck

Two-page A4 portrait PDF produced by **Claude Design**, in the same
editorial voice and palette as the sister repo `altajska-4-listing`:

- Trilingual: **Czech primary**, **Russian secondary**, **English captions**.
- Palette: `#FAF8F4` bg, `#1C1B18` ink, `#C9A961` gold accent,
  `#4A5D3F` leaf-green secondary, `#8A8578` muted, `#E5DFD3` hairline.
- Typography: Playfair Display (headings), Inter (body),
  JetBrains Mono (numbers).
- Gold is earned — only on the asking price line, the "our listing" bar
  in the valuation chart, and the section-title hairline.
- Every number in the deck must be cited from a `research/*.md` file.

## Target audience

Sale of an income-producing, STR-proven studio in prime Vinohrady to a:
1. **Czech / Russian-speaking private investor** looking for a turnkey
   asset with a documented rental track record, OR
2. **EU buyer** looking for a pied-à-terre in Prague that pays for
   itself as STR when not in use.

The deck must defend the 5.6 M CZK price AND make the STR upside
legible without overselling (no "luxurious", no "exclusive", no hype).

## Agent task matrix

| Agent | Writes into | Deliverable |
|-------|-------------|-------------|
| 1 — Valuation & Comparables | `research/01-valuation-thesis.md`, `research/02-comparables.md`, `research/assets/*.png` | Price thesis for 5.6 M CZK + 3 sale comps from Vinohrady studios (sreality + bezrealitky), Playwright screenshots |
| 2 — Neighborhood & Location | `research/03-neighborhood-map.md` | Royal Vinohrady narrative — transport, amenities, walk times to Old Town / Wenceslas Sq, parks (Riegrovy sady, Havlíčkovy sady), Manifesto Market, café culture. Pin list ready for the map render. |
| 3 — STR / Airbnb Yield | `research/04-rental-yield.md` | Long-term yield math (4.24 % gross / 3.64 % net-rent) + STR alternative modelled on AirDNA-style Prague 2 studio benchmarks + Prague STR regulatory environment (2024 platform-registry rules, any night caps). Compare LTR vs STR scenarios. |
| 4 — Copy + Fact Sheet + Design System | `brief/design-system.md`, `brief/fact-sheet.md`, `brief/copy.cs.md`, `brief/copy.ru.md`, `brief/copy.en.md`, `brief/claude-design-form.md` | Mirror Altajská's brief/ structure, adapted for this subject. Voice: tone of the Airbnb listing's host blurb translated into a sale-deck register — calm, Vinohrady-prestige, proof-not-hype. |
| 5 — Image Pipeline | `engine/prompts.json`, `engine/prompts.renders.json`, plus README block | Nano-Banana prompts tailored to the 7 actual photos. `fotos-4k/` and `renders/` stay empty pending billing (project 443316313587). |

## Non-negotiables

- **Price 5 600 000 CZK is fixed.** It is not a range to widen.
- **Rent 19 800 CZK incl. 2 800 CZK fees is fixed.** Do not model
  higher "asking rent"; the rent is already agreed with the tenant.
- **Do not fabricate review quotes.** Real guest quotes from the
  Airbnb page snapshot are in `research/assets/airbnb-reference-listing.png`
  (full-page screenshot). Only quote from that snapshot.
- **Do not claim amenities not on the Airbnb listing.** No A/C, no
  parking — those are NOT present.
- **Do not invent an m² number.** Size is TBD until George confirms;
  deck copy should say "compact studio / studio kompaktní / квартира-студия"
  and the valuation thesis should present scenarios.
- **Sister repo** `gtrush03/altajska-4-listing` is the style template.
  Read `brief/design-system.md` and `brief/claude-design-form.md`
  from `/Users/gtrush/Downloads/MAMA-HOUSE-DELIVERABLES/brief/` as your
  palette / typography / layout reference — do NOT diverge from it.
