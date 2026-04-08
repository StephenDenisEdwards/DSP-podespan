# DWG Files Request — LUCERN DREVOSTAVBY

**Date:** 2026-04-08
**Purpose:** To enable site design work (landscaping, swimming pond) and accurate digital overlay of the building on the geodetic survey plan.

---

## What to ask for

Request the **original DWG files** for all drawings in the project documentation. These are the source CAD files from which the PDFs were generated. Every PDF in the documentation package was created from a DWG — the architect has them.

### Priority 1 — Essential (need these first)

| Drawing | PDF name | Why we need it |
|---------|----------|----------------|
| **C.3 Situace koordinacni** | C.3. Situace koordinacni.pdf | Contains the building footprint positioned on the parcels with exact coordinates. This is the single most important file — it lets us place the house precisely on the survey plan. |
| **C.2 Situace celkova** | C.2. Situace celkova.pdf | Overall site plan with terrace, garage, paved areas, and all setback dimensions. |
| **D.1.1.3 Pudorys 1. NP** | D.1.1.3. Pudorys 1. NP.pdf | Ground floor plan — the exact house shape (it is not a simple rectangle). Needed to draw the accurate building outline. |

### Priority 2 — Important for site design

| Drawing | PDF name | Why we need it |
|---------|----------|----------------|
| **D.1.1.2 Pudorys zakladu** | D.1.1.2. Pudorys zakladu.pdf | Foundation plan — shows the exact footprint at ground level, drainage pipes around the house, and radon protection details. Relevant for understanding what's underground near the building. |
| **D.1.1.8 Pudorys zakladu garaze** | D.1.1.8. Pudorys zakladu garaze.pdf | Garage foundation plan — exact garage footprint. |
| **D.1.1.9 Pudorys 1. NP garaze** | D.1.1.9. Pudorys 1. NP garaze.pdf | Garage floor plan — exact garage shape. |
| **C.1 Situace sirsich vztahu** | C.1. Situace sirsich vztahu.pdf | Wider context plan — useful for understanding surroundings, access, and neighbouring features. |
| **C.4 Situace podpisova** | C.4. Situace podpisova.pdf | Signed site plan — may have additional annotations or corrections. |

### Priority 3 — Useful for detailed design

| Drawing | PDF name | Why we need it |
|---------|----------|----------------|
| **D.1.1.5 Rez A-A** | D.1.1.5. Rez A-A.pdf | Cross-section — shows finished ground levels, floor levels, and how the house sits in the terrain. Useful for understanding cut/fill near the house. |
| **D.1.1.6 Pohled severni/jizni** | D.1.1.6. Pohled severni_jizni.pdf | Elevations — show finished ground line around the house. |
| **D.1.1.7 Pohled vychodni/zapadni** | D.1.1.7. Pohled vychodni_zapadni.pdf | Elevations — same, other directions. |
| **D.1.4.1.2 Schema lezate kanalizace** | D.1.4.1.2. Schema lezate kanalizace.pdf | Underground drainage layout — pipe routes to avoid when excavating for a pond. |
| **D.1.4.1.4 Schema destove kanalizace** | D.1.4.1.4. Schema destova kanalizace.pdf | Rainwater drainage — potential integration with a swimming pond. |
| **D.1.4.3.3 Schema hromosvodu** | D.1.4.3.3. Schema hromosvodu.pdf | Lightning protection layout — earthing routes that may cross the garden. |

---

## How to ask

Something like:

> *"Dobrý den, mohli byste nám prosím poskytnout originální DWG soubory k projektové dokumentaci RD Edwards, Jevany? Potřebujeme je pro návrh zahradních úprav a koupacího jezírka. Především potřebujeme koordinační situaci (C.3), celkovou situaci (C.2) a půdorys 1. NP (D.1.1.3). Ideálně všechny výkresy, pokud je to možné."*

Translation:
> *"Hello, could you please provide us with the original DWG files for the RD Edwards project documentation, Jevany? We need them for designing the garden landscaping and a swimming pond. We primarily need the coordination site plan (C.3), overall site plan (C.2), and the ground floor plan (D.1.1.3). Ideally all drawings, if possible."*

---

## Format notes

- **DWG is preferred** — it's the native AutoCAD format and preserves everything (layers, blocks, dimensions, hatching, paper space layouts with title blocks and legends)
- **DXF is also acceptable** — we can work with it, though some formatting may be simplified
- The files should be in the **same coordinate system as the survey plan** (S-JTSK / EPSG:5514) — the site plans (C.2, C.3) should already be, since they're drawn on top of the survey data
- Ask whether the site plans were drawn in **absolute S-JTSK coordinates** or in a local coordinate system — this determines whether we can overlay them directly on the survey plan or need to align them

---

## What we already have

| File | Status |
|------|--------|
| 10225.dxf | Survey plan (polohopisny a vyskopisny plan) — already in the repo, fully analyzed |
| 10225.dwg | Same survey plan in DWG format — in the repo but not readable without AutoCAD/ODA converter |
| All PDFs | Complete set of ~45 PDFs — text/dimensions extractable, but graphical content (shapes, layouts) not accessible |

## What we can do once we have the DWGs

1. Extract the exact building footprint from C.3 and overlay it on the survey plan
2. Create an accurate combined site plan (survey + building + utilities) as the base for landscaping design
3. Design the swimming pond with precise positioning relative to the house, boundaries, and utilities
4. Calculate exact excavation volumes using the terrain elevation data
5. Plan utility integration (rainwater diversion to pond, electrical for circulation pump)
