# Survey Plan Analysis - 10225.dxf / 10225.dwg

**Date:** 2026-04-08

## File Summary

| Property | Value |
|---|---|
| Filename | 10225.dxf (282 KB) / 10225.dwg (56 KB) |
| AutoCAD version | AC1027 (AutoCAD 2013) |
| Code page | ANSI_1252 (Central European Windows) |
| Last saved by | steph |
| Drawing type | 2D (all Z = 0.0) |
| Coordinate system | S-JTSK (Czech national geodetic system) |

## What This Drawing Is

This is a **polohopisny a vyskopisny plan** (planimetric and altimetric survey plan) — a standard Czech geodetic survey deliverable. It documents the site at parcel 154/11 and surroundings in Jevany, produced by a licensed surveyor (geodet) as part of the building permit documentation.

The drawing shows:

1. **Cadastral parcel boundaries** with parcel numbers from the Czech land registry
2. **Terrain elevations** at ~93 measured points (392-400 m ASL), indicating a gently sloping site (~7 m drop over ~100 m)
3. **Existing infrastructure** — roads, sidewalks, driveways, vegetation
4. **Survey control network** — benchmarks, reference points, situational points
5. **Coordinate grid** in S-JTSK with labeled tick marks

## Spatial Extent

- **X range:** -717,399 to -717,317 (~82 m)
- **Y range:** -1,059,683 to -1,059,575 (~108 m)
- **Viewport center:** -717,368.7, -1,059,608.0
- **Elevation range:** 392.72 m to 399.60 m ASL (Bpv)

## Layers

All 14 layers use AutoCAD color index 7 (white/black). The numeric names follow the Czech geodetic feature coding standard:

| Layer | Entity Count | Meaning |
|-------|-------------|---------|
| 1 | 432 | Cadastral boundaries (hranice parcel) |
| 23 | 189 | Survey/height points (vyskove body) |
| 41 | 97 | Height value text annotations |
| 22 | 96 | Elevation labels (vyskove koty) |
| 25 | 25 | Geodetic control points (geodeticke body) |
| 4 | 19 | Buildings / structures (budovy) |
| 0 | 15 | Default layer |
| 61 | 12 | Coordinate grid (souradnicova sit) |
| 18 | 9 | Parcel number labels (cisla parcel) |
| 26 | 7 | Trees (stromy) |
| 19 | 3 | Additional parcel labels |
| 16 | 1 | Misc |

Two additional named layers exist but carry no entities: `CONSTRUCTION_CLASS`, `PATTERN_CLASS`.

## Entities (874 total in model space)

| Type | Count | Role |
|------|-------|------|
| LINE | 488 | Parcel boundaries, building edges, grid lines |
| TEXT | 220 | Labels — parcel numbers, elevations, surface types |
| INSERT | 136 | Survey symbol block references |
| ARC | 12 | Curved boundaries, building details |
| CIRCLE | 10 | Part of blocks, manholes |
| LWPOLYLINE | 6 | Complex boundaries (fences, walls) |
| POINT | 1 | Single reference point |
| SOLID | 1 | Filled triangle (arrowhead in RNZICE block) |

## Block Definitions (Survey Symbols)

12 blocks defined, representing standard Czech geodetic symbols:

| Block | Inserts | Description |
|-------|---------|-------------|
| 1$09 | 98 | Small circle (r=0.15) — spot elevation marker |
| SIT | 9 | Crosshair (+) shape — situational point |
| 3$04 | 8 | Circle + horizontal line — tree/vegetation symbol |
| 3$13 | 7 | Nested arcs — boundary detail point |
| 4$02 | 4 | Tiny circle (r=0.175) — survey control point |
| 2$18 | 3 | Two opposing arcs — utility/pipe symbol |
| RNZICE | 1 | Large circle + crosshair + directional lines — benchmark/reference point |
| 3$14 | 1 | V-shape polyline + 2 circles — gate/entrance symbol |
| 6$20 | 1 | Unit circle — manhole/well symbol |
| 1$07 | 1 | Arc-based — boundary marker |
| 1$051 | 2 | Nested block with scaled insert — composite boundary marker |
| 1$052 | 1 | Nested block with scaled insert — composite boundary marker |

## Text Content

### Parcel Numbers (layer 18/19)
154/4, 154/5, 154/6, 154/8, 154/10, 154/11, 154/15, 154/16, 157/19, 288/165, 562/6, 699, 113, 129

### Spot Elevations (layers 22/41)
~93 values ranging from 392.72 m to 399.60 m ASL. The site slopes generally from NW (~399 m) to SE (~393 m).

### Survey Point IDs (layer 23)
Sequential numbers 1 through 93, plus supplementary points 4001-4004.

### Surface / Land-Use Labels
- `chodnik` — sidewalk/path
- `asfaltova komunikace` — asphalt road
- `vjezd` — driveway/entrance
- `zelen` — greenery
- `RIS` — utility marker

### Grid Coordinates (layer 61)
X labels: 717330, 717390
Y labels: 1059600, 1059630, 1059660

## Linetypes Defined
ByBlock, ByLayer, Continuous, Dot, Hidden, Dashed, DashDot, Divide, Center

## Text Styles Defined
ITALICT, MONOTXT, STANDARD

## Relationship to Project

- The project's elevation reference is +/-0,000 = 397.402 m ASL (Bpv), which falls within the surveyed elevation range
- The target parcels for the building permit are **154/10** and **154/16**, both visible in this survey
- The survey covers the surrounding context parcels needed for the site plans (C.1-C.4)

## Note on the DWG File

The `10225.dwg` file (56 KB) is the original binary AutoCAD drawing. It likely contains a paper space layout with a title block, legend, surveyor's stamp, and certification — but we cannot read it directly with ezdxf (which only handles DXF). To access the paper space content, the DWG would need to be:
1. Opened in AutoCAD and exported as DXF, or
2. Converted using the ODA File Converter (free tool from Open Design Alliance)

## Visualization

A visualization script (`dwg-files/visualize_dxf.py`) and rendered PNG (`dwg-files/10225_visualization.png`) are available. The script is generic and works with any DXF file:

```
python visualize_dxf.py [file.dxf]
```
