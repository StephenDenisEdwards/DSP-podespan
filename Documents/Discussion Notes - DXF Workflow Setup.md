# Discussion Notes - DXF Workflow Setup

**Date:** 2026-04-08

## Project Overview

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

## Repository Contents

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

## Documents Examined

### D.1.1.2. Pudorys zakladu (Foundation Plan)

- **Foundation type:** Concrete strip foundations (zakladove pasy) in C 16/20 - XC2 concrete with reinforced concrete slab (ZB deska)
- **Key elevations:** -0,150 / -0,330 / -0,580 / -1,050 m
- **Overall dimensions:** ~16.9 m x 14.5 m (outer edge of foundation slab)
- **Radon protection:** Perforated drainage pipes DN 60 under slab, vented through foundation side
- **Drainage:** Perforated drainage pipes around perimeter with collection pipes
- **Penetrations:** Sewer, water + electrical, fresh air supply for fireplace

### D.1.1.3. Pudorys 1. NP (1st Floor Plan)

Single-story house with total usable area of **142.07 m2** plus a **38.19 m2 terrace**.

| Room | Area | Floor |
|---|---|---|
| 1.01 Zadveri (Entrance) | 8.90 m2 | Ceramic tile |
| 1.02 Technicka mistnost (Utility) | 4.14 m2 | Ceramic tile |
| 1.03 Koupelna + WC (Bathroom 1) | 3.78 m2 | Ceramic tile |
| 1.04 Obyvaci pokoj + KK (Living + kitchen) | 49.11 m2 | Wood |
| 1.05 Spiz (Pantry) | 4.16 m2 | Wood |
| 1.06 Pokoj 1 (Bedroom 1) | 11.28 m2 | Wood |
| 1.07 Koupelna + WC (Bathroom 2) | 11.22 m2 | Ceramic tile |
| 1.08 Pokoj 2 (Bedroom 2) | 17.11 m2 | Wood |
| 1.09 Loznice (Master bedroom) | 19.26 m2 | Wood |
| 1.10 Satna (Walk-in closet) | 6.38 m2 | Wood |
| 1.11 Chodba (Hallway) | 6.72 m2 | Wood |

**Wall types:**
- **W6 (Exterior):** Silicone facade + EPS 160mm + KVH 60/120 studs + mineral insulation + vapor barrier + battens 40/60 + Rigistabil. Total ~357 mm.
- **W1 (Interior load-bearing):** Rigistabil + KVH 60/120 + insulation + Rigistabil. Total 145 mm.
- **W2 (Interior non-load-bearing):** Rigistabil + KVH 60/80 + insulation + Rigistabil. Total 105 mm.

**Key features:** Chimney DN 270, hidden blind cassettes on most windows, heat pump in utility room, skylight 900x1200 in living room.

## Current Limitations

- All project files are **PDFs only** - we can extract text data but **cannot see the graphical content** (drawings, layouts, symbols, hatching)
- To work with the actual drawings, the **original DWG or DXF files** are needed from the architect

## DXF Workflow Setup

### What is DXF?
DXF (Drawing Exchange Format) is Autodesk's open, text-based CAD exchange format. It is fully interchangeable with DWG:
- **DWG -> DXF:** Save As DXF in AutoCAD (or any CAD program)
- **DXF -> DWG:** Open DXF in AutoCAD and Save As DWG

### Tool Installed
- **ezdxf 1.4.3** (Python library) - installed and verified on 2026-04-08
- Enables programmatic reading, editing, and creation of DXF files

### Capabilities
With DXF files, we can:
- Read all layers, entities, blocks, and dimensions
- Modify geometry (move/add/delete walls, openings, annotations)
- Update text, dimensions, and room labels
- Create new drawings from scratch
- Save back to DXF for reopening in AutoCAD

### Next Steps
1. Obtain original DWG files from LUCERN DREVOSTAVBY
2. Export them as DXF (Save As in AutoCAD)
3. Place DXF files in this project directory
4. Use ezdxf to read, analyze, and edit the drawings programmatically
