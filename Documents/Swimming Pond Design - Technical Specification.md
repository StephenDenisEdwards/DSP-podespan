# Natural Swimming Pond (Schwimmteich) - Technical Design Specification

**Date:** 2026-04-10
**Site:** Parcels 154/10 and 154/16, Jevany [533378]
**Owner:** Bc. Marketa Edwards
**Coordinate system:** S-JTSK (Krovak)
**Elevation datum:** Bpv (Baltic after adjustment)

---

## 1. Design Overview

A rectangular natural swimming pond (Schwimmteich) positioned adjacent to the existing terrace on the southeast side of the house. The pond uses biological filtration through aquatic plants and gravel substrate to maintain water quality without chemical treatment.

![Site Plan](dwg-files/schwimmteich_plan_v3.png)
*Figure 1: Site plan (left) and cross-section A-A' (right) showing pond position relative to building and terrace.*

![3D Isometric](dwg-files/schwimmteich_3d_isometric.png)
*Figure 2: 3D isometric cutaway view showing internal structure, depth zones, separation wall, gravel substrate, and circulation piping.*

---

## 2. Dimensions and Zone Areas

### Overall Pond

| Parameter | Value |
|-----------|-------|
| Overall dimensions | 10.0m x 7.5m |
| Total pond area | 75 m² |
| Swimming : Regeneration ratio | 1:1 (50:50) |
| Position | 0.1m gap from terrace edge (coping stone) |

The 1:1 ratio between swimming and regeneration zones follows the standard rule-of-thumb recommended in industry guidelines. UK/EU guidance suggests the swim area should not exceed 50-70% of total water surface, with a common target of equal area split (Ref: [Research Report 1], [Feasibility Guide §4]).

### Swimming Zone

| Parameter | Value |
|-----------|-------|
| Dimensions | 5.0m x 7.5m |
| Area | 38 m² |
| Depth | 2.0m (floor at 395.15m Bpv) |
| Water level | 397.05m Bpv (0.10m below terrace) |
| Terrace level | 397.15m Bpv |

The 2.0m depth provides thermocline stability, sufficient depth for comfortable swimming, and protection against freezing solid in winter at Jevany's ~400m ASL elevation (Ref: [Feasibility Guide §4], [Research Report 2 - Design Principles]).

### Regeneration Zone

| Parameter | Value |
|-----------|-------|
| Dimensions | 5.0m x 7.5m |
| Total area | 38 m² |
| Depth range | 0-100cm (three stepped zones) |

---

## 3. Regeneration Zone - Depth Zoning

The regeneration zone uses three stepped depth zones to support maximum plant diversity and optimise biological filtration. This follows the planting zone recommendations in the research literature, which identifies three distinct depth bands each suited to different plant communities (Ref: [Research Report 2 - Planting Palettes]).

### Zone Layout

The zones are arranged as concentric rings: a narrow marginal ring around the perimeter, a shallow ring inside that, and the deep gravel filter bed occupying the large centre.

| Zone | Depth | Width | Area | % of Regen | Purpose |
|------|-------|-------|------|------------|---------|
| **Zone 1: Marginal** | 0-30cm | 0.5m ring | ~12 m² | ~31% | Emergent edge plants |
| **Zone 2: Shallow** | 30-60cm | 0.5m ring | ~8 m² | ~22% | Mid-depth aquatics |
| **Zone 3: Deep gravel bed** | 60-100cm | Centre | ~18 m² | ~47% | Submerged oxygenators + biological filtration |

### Zone 1: Marginal (0-30cm)

The outermost ring, 0.5m wide around the full perimeter of the regeneration zone. This is the shallowest area, supporting emergent plants whose roots sit in saturated substrate but whose foliage grows above the waterline.

**Recommended plants:**
- Marsh Marigold (*Caltha palustris*)
- Soft Rush (*Juncus effusus*)
- Water Forget-me-not (*Myosotis scorpioides*)
- Flowering Rush (*Butomus umbellatus*)
- Creeping Jenny (*Lysimachia nummularia*)

### Zone 2: Shallow (30-60cm)

A 0.5m wide ring inside the marginal zone. Supports larger aquatic plants with deeper root systems that are partially or fully submerged.

**Recommended plants:**
- Yellow Flag Iris (*Iris pseudacorus*)
- Sweet Flag (*Acorus calamus*)
- Water Mint (*Mentha aquatica*)
- Pickerel Weed (*Pontederia cordata*)

### Zone 3: Deep Gravel Bed (60-100cm)

The largest zone, occupying the centre of the regeneration area. Contains the layered gravel substrate that provides the primary biological filtration surface. Supports fully submerged oxygenating plants and water lilies.

**Recommended plants:**
- Hardy Water Lily (*Nymphaea alba*)
- Hornwort (*Ceratophyllum demersum*)
- Water Crowfoot (*Ranunculus aquatilis*)
- Water Milfoil (*Myriophyllum spicatum*)

**Planting density:** 4-5 plants per m², aiming for 100% cover of shallow beds by summer (Ref: [Research Report 2 - Planting Palettes]).

---

## 4. Gravel Substrate

The deep gravel bed (Zone 3) contains a layered substrate that supports beneficial biofilm bacteria for nutrient removal and water purification. The total substrate depth is approximately 0.3-0.4m, sitting within the 0.6-1.0m deep zone.

German/US guidelines cite 0.6-1.0m of gravel depth under plants to house bacteria. Biotop uses 0.8-1.0m of gravel in their filters (Ref: [Research Report 1 - Sizing and Zoning]).

### Gravel Layer Specification

| Layer | Position | Grain size | Purpose |
|-------|----------|------------|---------|
| Coarse | Bottom | 16-32mm | Drainage, structural support, pipe protection |
| Medium | Middle | 8-16mm | Transition layer, additional biofilm surface |
| Fine | Top | 2-8mm | Planting substrate, maximum biofilm surface area |

All gravel must be washed, lime-free, and chemically inert to avoid nutrient leaching or pH changes (Ref: [Research Report 1 - Design Principles]).

---

## 5. Separation Wall

A reinforced concrete wall divides the swimming zone from the regeneration zone.

| Parameter | Value |
|-----------|-------|
| Material | Reinforced concrete or masonry |
| Thickness | 0.30m |
| Wall top | 0.40m below water surface (396.65m Bpv) |
| Wall base | Pond floor level (395.15m Bpv) |
| Water passages | 3 openings, each 0.5m wide |

The wall top sits below the waterline to allow surface-level water exchange between zones while preventing swimmers from entering the regeneration area. The three water passages at the base allow circulation flow from the regeneration zone back into the swimming zone after biological filtration.

Per BANSP/IOB guidelines, swimming and treatment zones must be strictly separated (Ref: [Research Report 1 - Sizing and Zoning]).

---

## 6. Circulation System

Water is continuously circulated through the biological filtration system. The flow path ensures all water passes through the gravel substrate and plant root zones before returning to the swimming area.

### Flow Path

```
Swimming Zone → Skimmer (surface) + Bottom Drain (deep) → Pump Chamber → 
Distribution Manifold → Perforated Pipes (under gravel) → 
Biological Filtration (through gravel layers) → 
Clean water flows through wall passages → Swimming Zone
```

### Components

| Component | Position | Function |
|-----------|----------|----------|
| **Skimmer (SK)** | Swimming zone, near terrace, surface level | Collects surface debris (leaves, pollen, floating matter) |
| **Bottom Drain (BD)** | Swimming zone floor, centre | Deep water circulation, removes settled sediment |
| **Pump Chamber** | Outside pond, adjacent to separation wall | Houses circulation pump, accessible for maintenance |
| **Distribution Manifold** | Under gravel, far end of regen zone | Distributes pumped water evenly across the gravel bed |
| **Perforated Branch Pipes** | Under gravel, perpendicular to manifold | Even distribution through substrate for uniform filtration |
| **Wall Passages** | 3 openings in separation wall | Return filtered water to swimming zone |

### Pump Sizing

Guidelines suggest recirculating the entire pond volume at least every 12-24 hours (Ref: [Research Report 2 - Hydraulics]).

| Parameter | Value |
|-----------|-------|
| Estimated pond volume | ~100 m³ |
| Target turnover | 12-24 hours |
| Required flow rate | ~4,200-8,300 L/h |

---

## 7. Entry and Access

### Steps

Three graduated steps descend from the terrace into the swimming zone:

| Step | Width | Depth below terrace |
|------|-------|---------------------|
| Step 1 | 3.0m | 0.30m |
| Step 2 | 2.4m | 0.60m |
| Step 3 | 1.8m | 0.90m |

Steps narrow progressively and are centred on the terrace edge. Non-slip surface finish required.

### Terrace / Deck

The existing 38 m² terrace serves as the pool deck. A coping stone edge (0.1m gap) separates the terrace from the pond water.

---

## 8. Elevations

| Feature | Elevation (m Bpv) |
|---------|-------------------|
| Terrace / deck level | 397.15 |
| Water level | 397.05 |
| Separation wall top | 396.65 |
| Zone 1 floor (marginal, 0-30cm) | ~396.90 |
| Zone 2 floor (shallow, 30-60cm) | ~396.60 |
| Zone 3 floor (deep gravel, 60-100cm) | ~396.05 |
| Swimming zone floor | 395.15 |

Natural terrain slopes approximately 2m toward the southeast. The pond is partially in-ground, taking advantage of the slope to reduce excavation on the downhill side (Ref: [Feasibility Guide §3]).

---

## 9. Construction Notes

### Liner / Sealing

The site soil is F5 ML (low-plasticity silt/clay) with permeability kv = 5.0 x 10⁻⁶ m/s. While relatively tight, this is not sufficient for a permanent pond without additional sealing. Options:

1. **Compacted clay liner** (min 300mm) from on-site clay to achieve kv < 10⁻⁸ m/s
2. **EPDM rubber liner** (≥1.0mm) with geotextile underlay — most reliable option
3. **Bentonite mat** as intermediate option

(Ref: [Feasibility Guide §3], [Research Report 1 - Construction Methods])

### Excavation

| Parameter | Estimate |
|-----------|----------|
| Excavation depth (max) | ~2.5m (swimming zone + liner base) |
| Estimated volume | ~110-130 m³ |
| Spoil material | F5 ML clay — reusable for compacted liner, landscaping berms, or slope grading |

Excavation will pass through fill material (0-1.80m) into natural deluvial clay below. The natural clay layer provides a more stable base (Ref: [Feasibility Guide §2]).

### Utilities

- Connect overflow to existing rainwater drainage system (D.1.4.1.4)
- Pump electrical supply from house (D.1.4.3)
- Maintain clearance from underground sewer route (D.1.4.1.2)
- All pipe penetrations through the liner must be welded or mechanically sealed

### Winter Considerations

Jevany is at ~400m ASL in central Bohemia with hard frosts expected. The 2.0m swimming zone depth prevents the pond from freezing solid. The circulation system must be winterisable — pump and exposed pipes drained or protected (Ref: [Feasibility Guide §3]).

---

## 10. Water Quality Targets

No chemical treatment (chlorine, biocides) is used. Water quality is maintained entirely through biological filtration.

| Parameter | Target | Standard |
|-----------|--------|----------|
| *E. coli* | ≤100 CFU/100 mL | FLL (German) guidelines |
| pH | 6.5-8.5 (target 7.0-7.5) | FLL guidelines |
| Water hardness | 8-12° dH | FLL guidelines |
| Phosphate | Minimised (no fertiliser runoff) | BANSP/IOB |

All surface runoff and fertiliser from surrounding land must be excluded from the pond. Even small amounts of lawn fertiliser can overload the system with phosphorus and trigger algal blooms (Ref: [Research Report 1 - Design Principles]).

---

## 11. Maintenance Summary

| Task | Frequency |
|------|-----------|
| Skim surface debris | Daily/as needed |
| Check pump and skimmer | Weekly |
| Test water quality (pH, nutrients) | Monthly |
| Trim and cut back dead plant growth | Autumn |
| Remove accumulated sediment | Annually |
| Deep clean and inspect liner | Annually (spring) |
| Lamp replacement (if UV fitted) | As needed |

(Ref: [Research Report 2 - Maintenance])

---

## 12. Drawing References

| Drawing | Description |
|---------|-------------|
| `schwimmteich_plan_v3.dxf` | Site plan with pond layout in S-JTSK coordinates |
| `schwimmteich_plan_v3.png` | Site plan visualisation with cross-section |
| `schwimmteich_3d_isometric.png` | 3D isometric cutaway showing internal structure |
| `combined_site_plan.dxf` | Combined site plan with building, garage, roads |
| `10225.dxf` | Original survey plan (base drawing) |

---

## 13. Research and Reference Documents

| Document | Location | Content |
|----------|----------|---------|
| Natural Swimming Pond - Feasibility & Design Guide | `Documents/Natural Swimming Pond - Feasibility & Design Guide.md` | Site-specific feasibility assessment for Jevany, soil conditions, sizing, excavation estimates |
| Natural Swimming Ponds Research Report | `Documents/reseach/natural-swimming-ponds-research-report.md` | Design principles, sizing/zoning ratios, construction methods, liner comparison, UK/EU case studies, FLL water quality standards |
| Natural Swimming Pond: Principles to Construction | `Documents/reseach/natural-swimming-ponds-research-report-2.md` | Planting palettes by depth zone, pump sizing calculations, filtration options comparison, construction sequence, maintenance schedules |
| Survey Plan Analysis | `Documents/Survey Plan Analysis - 10225.md` | Analysis of the 10225.dxf survey data, elevation points, coordinate system |
| Soil and Geotechnical Assessment | `Documents/Soil and Geotechnical Assessment - Swimming Pond.md` | Consolidated soil data, permeability analysis, data source traceability, outstanding investigations |

### Key Standards Referenced

- **FLL** (Forschungsgesellschaft Landschaftsentwicklung Landschaftsbau) — German guidelines for natural swimming pond water quality
- **BANSP/IOB** — British Association of Natural Swimming Pools / Institute of Builders — UK trade guidelines requiring sealed construction, zoned layout, no biocides
- **CSN 75 9010** — Czech standard for infiltration coefficient testing

---

## 14. Design Summary

| Parameter | Value |
|-----------|-------|
| **Total pond area** | 75 m² (10.0m x 7.5m) |
| **Swimming zone** | 38 m² at 2.0m deep |
| **Regeneration zone** | 38 m² in 3 depth zones |
| — Zone 1 (marginal) | ~12 m² at 0-30cm |
| — Zone 2 (shallow) | ~8 m² at 30-60cm |
| — Zone 3 (deep gravel) | ~18 m² at 60-100cm |
| **Swim:Regen ratio** | 1:1 |
| **Separation wall** | RC, 0.30m thick, 3 passages |
| **Gravel substrate** | 3 layers (coarse/medium/fine) |
| **Circulation** | Skimmer + bottom drain → pump → gravel bed → wall passages |
| **Water treatment** | Biological only (no chemicals) |
| **Planting density** | 4-5 plants/m² |
| **Pump turnover** | 12-24 hours full volume |
