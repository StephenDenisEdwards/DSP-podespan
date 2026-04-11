# CAD Workflow and File Status

**Date:** 2026-04-08 (updated 2026-04-10)
**Purpose:** Track CAD file acquisition from LUCERN, document analysis results, and enable site design work (landscaping, swimming pond).

---

## 1. Project Overview

This repository contains the complete building permit documentation (DSP + DPS) for a new family house in Jevany, Czech Republic.

- **Project:** Novostavba rodinneho domu (New family house)
- **Location:** Jevany [533378], parcels 154/10 and 154/16
- **Investor:** Bc. Marketa Edwards, K dalnici 167, Pitkovice, 104 00 Praha 10
- **Design firm:** LUCERN DREVOSTAVBY s.r.o., Udolni 280/15, Praha 4 - Branik
- **Construction type:** Timber-frame (drevostavba), LUCERN EKO PLUS system
- **Lead designer:** Ing. Josef Frydryn
- **Drafter:** Ing. Vaclav Kepelak, DiS.
- **Authorization:** Ing. Milos Slavik (digitally signed 2026-03-09)
- **Stage:** DSP + DPS
- **Elevation reference:** +/-0,000 = 397.402 m above sea level (Bpv)

The repository contains ~45 PDF files organized into standard Czech building documentation sections:

| Section | Description |
|---|---|
| A. Pruvodni list | Cover/introductory report |
| B. Souhrnna technicka zprava | Summary technical report |
| C. Situacni vykresy (C.1-C.4) | Site plans |
| D.1.1. Architektonicko stavebni cast (13 drawings) | Architecture - plans, sections, elevations |
| D.1.2. Stavebne konstrukcni cast | Structural engineering |
| D.1.3. Pozarni bezpecnost staveb | Fire safety |
| D.1.4.1. Zdravotne technicke instalace (5 docs) | Plumbing |
| D.1.4.2. Vytapeni (2 docs) | Heating |
| D.1.4.3. Elektroinstalace (3 docs) | Electrical |
| D.1.4.4. Nucene vetrani (2 docs) | Mechanical ventilation |
| E. Dokladova cast | Supporting documents (geology, radon, PENB) |
| _TITULKY | Title/cover pages |

---

## 2. File Status

| File | Status | Notes |
|------|--------|-------|
| 10225.dxf | **Available** | Survey plan (polohopisny a vyskopisny plan) — in S-JTSK absolute coordinates, fully analyzed |
| 10225.dwg | **Available** | Same survey plan in DWG format |
| All PDFs | **Available** | Complete set of ~45 PDFs — text/dimensions extractable, but graphical content (shapes, layouts) not accessible |
| C.3. Koordinacni situace.dwg/.dxf | **Received 2026-04-10** | Coordination site plan. Paper space coordinates (mm), NOT S-JTSK. |
| C.2. Celkovy situacni vykres.dwg/.dxf | **Received 2026-04-10** | Overall site plan. Paper space coordinates (mm), NOT S-JTSK. |
| D.1.1.3. Pudorys 1. NP.dwg/.dxf | **Received 2026-04-10** | Ground floor plan. Local coordinates (mm), near origin. |

---

## 3. Outstanding File Requests

Request the **original DWG files** for all remaining drawings. Every PDF in the documentation package was created from a DWG — the architect has them.

### Priority 2 — Important for site design

| Drawing | PDF name | Why we need it |
|---------|----------|----------------|
| **D.1.1.2 Pudorys zakladu** | D.1.1.2. Pudorys zakladu.pdf | Foundation plan — exact footprint at ground level, drainage pipes, radon protection. Relevant for understanding what's underground near the building. |
| **D.1.1.8 Pudorys zakladu garaze** | D.1.1.8. Pudorys zakladu garaze.pdf | Garage foundation plan — exact garage footprint. |
| **D.1.1.9 Pudorys 1. NP garaze** | D.1.1.9. Pudorys 1. NP garaze.pdf | Garage floor plan — exact garage shape. |
| **C.1 Situace sirsich vztahu** | C.1. Situace sirsich vztahu.pdf | Wider context plan — surroundings, access, neighbouring features. |
| **C.4 Situace podpisova** | C.4. Situace podpisova.pdf | Signed site plan — may have additional annotations or corrections. |

### Priority 3 — Useful for detailed design

| Drawing | PDF name | Why we need it |
|---------|----------|----------------|
| **D.1.1.5 Rez A-A** | D.1.1.5. Rez A-A.pdf | Cross-section — finished ground levels, floor levels, terrain relationship. |
| **D.1.1.6 Pohled severni/jizni** | D.1.1.6. Pohled severni_jizni.pdf | Elevations — finished ground line around the house. |
| **D.1.1.7 Pohled vychodni/zapadni** | D.1.1.7. Pohled vychodni_zapadni.pdf | Elevations — other directions. |
| **D.1.4.1.2 Schema lezate kanalizace** | D.1.4.1.2. Schema lezate kanalizace.pdf | Underground drainage layout — pipe routes to avoid when excavating. |
| **D.1.4.1.4 Schema destove kanalizace** | D.1.4.1.4. Schema destova kanalizace.pdf | Rainwater drainage — potential integration with swimming pond. |
| **D.1.4.3.3 Schema hromosvodu** | D.1.4.3.3. Schema hromosvodu.pdf | Lightning protection — earthing routes that may cross the garden. |

### How to Request

> *"Dobrý den, mohli byste nám prosím poskytnout originální DWG soubory k projektové dokumentaci RD Edwards, Jevany? Potřebujeme je pro návrh zahradních úprav a koupacího jezírka. Především potřebujeme koordinační situaci (C.3), celkovou situaci (C.2) a půdorys 1. NP (D.1.1.3). Ideálně všechny výkresy, pokud je to možné."*

Translation:
> *"Hello, could you please provide us with the original DWG files for the RD Edwards project documentation, Jevany? We need them for designing the garden landscaping and a swimming pond. We primarily need the coordination site plan (C.3), overall site plan (C.2), and the ground floor plan (D.1.1.3). Ideally all drawings, if possible."*

### Format Notes

- **DWG is preferred** — native AutoCAD format, preserves everything (layers, blocks, dimensions, hatching, paper space layouts)
- **DXF is also acceptable** — fully interchangeable with DWG, though some formatting may be simplified
- Files should be in **S-JTSK / EPSG:5514** — ask whether site plans were drawn in absolute S-JTSK coordinates or a local coordinate system

---

## 4. DXF Analysis Results (2026-04-10)

### Tool Setup

- **ezdxf 1.4.3** (Python library) — installed and verified 2026-04-08
- Enables programmatic reading, editing, and creation of DXF files

### C.3. Koordinacni situace (Coordination site plan)

- **DXF version:** AC1027 (AutoCAD 2013)
- **Units:** mm
- **Layers:** 12 (including BT_mapove_znacky, BT_hranice_parcel, BT_hranice_budov, BT_vnitrni_kresby, BT_text_parcel, BT_prvky_mapy, Situace - koordinační)
- **Entities:** 801 (453 LWPOLYLINE, 164 MTEXT, 53 CIRCLE, 39 DIMENSION, 33 HATCH, 30 INSERT, 29 ARC)
- **Extents:** Min (405930, -271768) to Max (619733, -128588) — paper space layout, ~214m x 143m sheet
- **Coordinate system:** Paper space (mm), NOT S-JTSK

### C.2. Celkovy situacni vykres (Overall site plan)

- **DXF version:** AC1027
- **Units:** mm
- **Layers:** 10 (similar BT_ survey layers as C.3)
- **Entities:** 287 (146 LWPOLYLINE, 40 MTEXT, 33 CIRCLE, 31 DIMENSION, 30 INSERT, 7 HATCH)
- **Extents:** Min (155930, -269476) to Max (369733, -128588) — paper space layout
- **Coordinate system:** Paper space (mm), NOT S-JTSK

### D.1.1.3. Pudorys 1. NP (Ground floor plan)

- **DXF version:** AC1027
- **Units:** mm
- **Layers:** 24 (Konstrukce - svislé nosné, Otvory – Okna, Otvory – Dveře, Interiér - nábytek, Kóty - SP, etc.)
- **Entities:** 420 (142 DIMENSION, 100 LWPOLYLINE, 95 INSERT, 58 MTEXT, 18 CIRCLE, 7 HATCH)
- **Extents:** Min (-2870, -19566) to Max (17163, 9870) — ~20m x 29m, local coordinates near origin
- **Coordinate system:** Local model coordinates (mm)

### Survey plan reference (10225.dxf)

- **Extents:** Min (-717399, -1059683) to Max (-717317, -1059575) — ~82m x 108m
- **Coordinate system:** S-JTSK absolute (EPSG:5514)

---

## 5. Coordinate System Issue

The LUCERN drawings are in paper/layout coordinates (mm), not S-JTSK. Direct overlay on the survey plan is not possible without transformation.

**Approaches:**
1. **Ask LUCERN for S-JTSK versions** — request the model-space drawings in absolute S-JTSK coordinates, or ask for the xref/block of the survey underlay they used.
2. **Manual alignment** — extract the building footprint from C.3 and place it on the survey plan using known reference points and setback dimensions. Work on this is underway.

---

## 6. Documents Examined from PDFs

### D.1.1.2. Pudorys zakladu (Foundation Plan)

- **Foundation type:** Concrete strip foundations (zakladove pasy) in C 16/20 - XC2 concrete with reinforced concrete slab (ZB deska)
- **Key elevations:** -0,150 / -0,330 / -0,580 / -1,050 m
- **Overall dimensions:** ~16.9 m x 14.5 m (outer edge of foundation slab)
- **Radon protection:** Perforated drainage pipes DN 60 under slab, vented through foundation side
- **Drainage:** Perforated drainage pipes around perimeter with collection pipes
- **Penetrations:** Sewer, water + electrical, fresh air supply for fireplace

### D.1.1.3. Pudorys 1. NP (1st Floor Plan)

Single-story house with total usable area of **142.07 m²** plus a **38.19 m² terrace**.

| Room | Area | Floor |
|---|---|---|
| 1.01 Zadveri (Entrance) | 8.90 m² | Ceramic tile |
| 1.02 Technicka mistnost (Utility) | 4.14 m² | Ceramic tile |
| 1.03 Koupelna + WC (Bathroom 1) | 3.78 m² | Ceramic tile |
| 1.04 Obyvaci pokoj + KK (Living + kitchen) | 49.11 m² | Wood |
| 1.05 Spiz (Pantry) | 4.16 m² | Wood |
| 1.06 Pokoj 1 (Bedroom 1) | 11.28 m² | Wood |
| 1.07 Koupelna + WC (Bathroom 2) | 11.22 m² | Ceramic tile |
| 1.08 Pokoj 2 (Bedroom 2) | 17.11 m² | Wood |
| 1.09 Loznice (Master bedroom) | 19.26 m² | Wood |
| 1.10 Satna (Walk-in closet) | 6.38 m² | Wood |
| 1.11 Chodba (Hallway) | 6.72 m² | Wood |

**Wall types:**
- **W6 (Exterior):** Silicone facade + EPS 160mm + KVH 60/120 studs + mineral insulation + vapor barrier + battens 40/60 + Rigistabil. Total ~357 mm.
- **W1 (Interior load-bearing):** Rigistabil + KVH 60/120 + insulation + Rigistabil. Total 145 mm.
- **W2 (Interior non-load-bearing):** Rigistabil + KVH 60/80 + insulation + Rigistabil. Total 105 mm.

**Key features:** Chimney DN 270, hidden blind cassettes on most windows, heat pump in utility room, skylight 900x1200 in living room.

---

## 7. What We Can Do With the DWGs

1. Extract the exact building footprint from C.3 and overlay it on the survey plan
2. Create an accurate combined site plan (survey + building + utilities) as base for landscaping design
3. Design the swimming pond with precise positioning relative to the house, boundaries, and utilities
4. Calculate exact excavation volumes using the terrain elevation data
5. Plan utility integration (rainwater diversion to pond, electrical for circulation pump)

---

## 8. Next Steps

1. ~~Obtain Priority 1 DWG files from LUCERN~~ **Done (2026-04-10)**
2. ~~Export as DXF~~ **Done (2026-04-10)**
3. ~~Analyze DXF files with ezdxf~~ **Done (2026-04-10)**
4. Request S-JTSK coordinate versions from LUCERN
5. Extract building footprint from C.3 and manually align to survey plan
6. Create combined site plan (survey + building + utilities) as base for landscaping design
7. Request remaining Priority 2-3 DWG files
