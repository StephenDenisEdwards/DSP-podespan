# Soil and Geotechnical Assessment - Swimming Pond

**Date:** 2026-04-11
**Site:** Parcels 154/10 and 154/16, Jevany [533378]
**Owner:** Bc. Marketa Edwards
**Purpose:** Consolidate all available geotechnical data relevant to the proposed natural swimming pond (Schwimmteich) and identify gaps requiring further investigation.

---

## 1. Data Sources

All soil and geotechnical data currently available for this site originates from the **geological survey (geologicky pruzkum)** commissioned for the house construction, stored in the project under `E. Dokladova cast / GEOLOGICKY PRUZKUM`. The raw survey report is not included in this repository — the data below has been extracted from the following project documents that reference it:

| Document | What it contains |
|----------|-----------------|
| Natural Swimming Pond - Feasibility & Design Guide (2026-04-08) | Full borehole S1 profile, groundwater, permeability, radon, terrain, and feasibility factors |
| Swimming Pond Design - Technical Specification (2026-04-10) | Soil classification, permeability, excavation estimates, liner/sealing options |
| README.md | Site data summary table |
| Survey Plan Analysis - 10225.md | Elevation range and coordinate data from geodetic survey |
| Discussion Notes - DXF Workflow Setup.md | Foundation type, radon protection measures for the house |

**Important limitation:** All geotechnical data derives from **borehole S1**, which was drilled for the house foundation investigation. This borehole is not at the proposed pond location. The soil profile at the pond location has not been independently verified.

---

## 2. Soil Classification and Profile

**Classification:** F5 ML — low-plasticity silt/clay, stiff consistency throughout the full profile.

### Borehole S1 Profile

| Layer | Depth | Classification | Description |
|-------|-------|---------------|-------------|
| I | 0.00-0.10 m | F5 ML | Topsoil / humozni hlina (humic loam fill) |
| II | 0.10-1.80 m | F5 ML Y | Strongly sandy clay, stiff consistency. **Fill material (navazka)** with feldspar, quartz, mica from granite. |
| III | 1.80-2.00 m+ | F5 ML | Light brown/pinkish weakly sandy clay, stiff consistency. **Natural deluvial soil**, granite-derived. |

### Key Characteristics

- The entire profile is F5 ML (low-plasticity silt/clay), stiff consistency
- Mineral content (feldspar, quartz, mica) derives from the underlying Ricany-type granite
- **The upper 1.80 m is anthropogenic fill (navazka), not undisturbed ground**
- Natural deluvial clay only begins below 1.80 m
- The fill material (Layer II) may have variable properties across the site since it was placed, not naturally deposited

### Relevance to Pond Construction

The pond excavation will reach a maximum depth of ~2.5 m (swimming zone + liner base). This means:

- Excavation will pass entirely through the fill material (0-1.80 m) and into the natural deluvial clay below
- The natural clay layer (Layer III, below 1.80 m) provides a more stable, consistent base for the pond
- The fill layer should not be relied upon for structural or sealing purposes without testing
- Excavated spoil (F5 ML clay) is potentially reusable for compacted clay liner, landscaping berms, or slope grading

---

## 3. Soil Permeability

| Parameter | Value | Standard |
|-----------|-------|----------|
| Infiltration coefficient (kv) | 5.0 x 10⁻⁶ m/s | CSN 75 9010 |
| Classification | Boundary between low and medium permeability | |
| Existing soakaway performance | 16 m² active area, 67.8 hours drain-down for 9.76 m³ retention | |

### Interpretation for Pond Use

- A kv of 5.0 x 10⁻⁶ m/s is **not sufficient** for a permanent pond without additional sealing
- For a sealed pond, the liner or compacted clay must achieve kv < 10⁻⁸ m/s (two orders of magnitude tighter)
- The natural clay is described as "relatively tight" but not impermeable — water would slowly drain without a liner
- Whether the on-site clay can be compacted to achieve kv < 10⁻⁸ m/s is unknown and requires a Proctor compaction test

### Data Limitations

- The kv value comes from a **single borehole (S1)** at the house location
- Permeability may differ at the pond location, particularly within the variable fill layer
- The test was conducted per CSN 75 9010 but the specific depth and method (falling head, constant head, field, or lab) is not recorded in the project documents
- No permeability data exists for the natural clay layer (Layer III) separately from the fill

---

## 4. Geology and Bedrock

| Parameter | Value |
|-----------|-------|
| Bedrock type | Ricany-type granite |
| Soil origin | Granite-derived deluvial deposits |
| Characteristic minerals | Feldspar, quartz, mica |
| Chemical character | Neutral to slightly acidic (suitable for aquatic planting) |
| Groundwater regime | Fracture-controlled within granite bedrock |

The granite-derived soil is chemically suitable for a natural pond. The neutral-to-acidic character will not adversely affect pH or cause lime leaching (unlike concrete-based solutions).

---

## 5. Groundwater

| Parameter | Value |
|-----------|-------|
| Water table depth | ~7 m below ground surface |
| Aquifer type | Fracture-controlled, granite bedrock |
| Recharge | Direct infiltration of atmospheric precipitation |

### Implications for the Pond

- **No groundwater interference** at the proposed excavation depth (2.0-2.5 m)
- No risk of groundwater contamination from the pond
- No risk of buoyancy or flotation of an empty/drained pond (water table is far below pond base)
- The deep water table is a favourable condition — it simplifies both construction and ongoing management

---

## 6. Radon

| Parameter | Value |
|-----------|-------|
| Radon index | HIGH |
| Activity concentration (75th percentile) | 72.3 kBq/m³ |
| Gas permeability | Medium (stredni plynopropustnost) |

### Relevance to Pond

- **Open-air pond:** Radon dissipates freely in open water and air — **not a concern** for the swimming pond itself
- **Enclosed spaces:** Any underground pump chambers, plant rooms, or enclosed equipment housing would require radon protection measures (ventilation, sealed membranes)
- The house foundations already incorporate radon protection: perforated drainage pipes DN 60 under the foundation slab, vented through the foundation side

---

## 7. Terrain and Slope

| Parameter | Value |
|-----------|-------|
| Elevation range (site) | 392.72 m to 399.60 m ASL (Bpv) |
| Overall slope | ~7 m fall from south (street) to north, over ~100 m |
| Finished floor level (house) | +/-0,000 = 397.402 m Bpv |
| Finished ground level | 397.152 m Bpv |
| Terrain around building | 396.8-398.7 m Bpv |
| Local slope at pond | ~2 m fall toward the southeast |

### Implications for Pond Construction

- Excavation on a slope means **unequal cut depths** — the downhill (SE) side will have a significantly deeper cut than the uphill side
- The downhill side will have a substantial exposed wall requiring retaining solutions or naturalistic grading
- The slope is an advantage for circulation — water can flow by gravity from a higher regeneration zone to the swimming zone
- Excavated spoil can be reused to build up the downhill side and grade the surrounding terrain

---

## 8. Waterproofing Assessment

Based on the available soil data, four waterproofing options have been evaluated:

| Option | Suitability | Notes |
|--------|-------------|-------|
| **Compacted on-site clay** (min 300 mm) | Good — if Proctor test confirms kv < 10⁻⁸ m/s | Cheapest; most natural; uses excavated material. Viability unproven. |
| **Bentonite mat (GCL)** | Excellent | Self-healing; ~5-10 mm thick; reliable. Good backup for clay liner in critical areas. |
| **EPDM rubber liner** (1.0-1.5 mm) | Excellent | Standard for garden/swimming ponds; 20-30+ year life; most reliable option. Requires geotextile underlay. |
| **PVC-P (welded PVC sheets)** | Excellent | Common in Czech Republic (e.g. Alkorplan); often more cost-effective than EPDM; local installers familiar. |
| **Concrete with waterproof coating** | Overkill | Expensive; not typical for natural ponds; prone to freeze/thaw cracking in Jevany climate; lime leaching raises pH. |

**Current recommendation (from Feasibility Guide):** Test the on-site clay first. If it seals adequately after compaction, use compacted clay as the primary barrier with bentonite mat backup in critical areas. If clay does not achieve target permeability, use EPDM or PVC-P liner with geotextile underlay.

**Note on concrete:** Concrete lining is not considered necessary even at the 2.0 m swimming zone depth. The hydrostatic pressure at 2 m (~0.2 bar) is well within the capability of EPDM/PVC-P liners. Concrete introduces risks (freeze/thaw cracking, lime leaching affecting biological filtration pH) without corresponding benefits for a natural swimming pond.

---

## 9. Concrete vs. Liner-Only Construction — Decision Criteria

The question of whether concrete construction is necessary is a question of **ground stability and structural loads**, not waterproofing. A liner (EPDM, PVC-P, or compacted clay) handles waterproofing. Concrete is only justified when the ground itself cannot hold the shape of the pond.

### Factors That Would Require Concrete

| Factor | Threshold | This Site (Current Data) |
|--------|-----------|--------------------------|
| **Unstable soil** — loose, unconsolidated, or organic fill that won't hold a 1:3 slope at 2 m depth | Soft or variable fill revealed in pond-location borehole | F5 ML stiff clay at S1 — **favourable**, but unverified at pond location |
| **High groundwater** — water table close to pond depth; empty pond could float or collapse inward from hydrostatic pressure | Water table within 3 m of pond base | Water table at ~7 m — **not an issue** |
| **Near-vertical walls required** — formal pool shape or tight space constraints forcing steep sides | Slopes steeper than ~1:2 | Design uses 1:3 graded slopes — **not an issue** |
| **Integrated structural features** — built-in steps, seating ledges, overflow channels, or load-bearing edges (e.g. deck cantilevering over pond) | Structural loads on pond walls | Current design uses natural beach entries and planted shelves — **not an issue** |
| **Heavy adjacent loads** — driveway, building, or retaining wall at pond edge creating lateral earth pressure on pond walls | Surcharge loads within 1.5x pond depth of the edge | **Critical — see Building Proximity below** |
| **Proximity to building foundations** — deep excavation near existing foundations can undermine bearing capacity or cause settlement | Excavation within the influence zone of existing foundations (typically a 45-degree line from foundation base) | **Critical — see Building Proximity below** |

### Building Proximity — Critical Factor for This Site

The current design places the pond **0.1 m from the terrace edge**, directly adjacent to the house on the southeast side. This proximity introduces structural considerations that go beyond general pond construction:

**Key dimensions:**

| Parameter | Value |
|-----------|-------|
| Pond to terrace gap | 0.1 m (coping stone) |
| Terrace area | 38.18 m² |
| Pond swimming zone depth | 2.0 m (floor at 395.15 m Bpv) |
| Maximum excavation depth | ~2.5 m |
| House foundation type | Concrete strip foundations (základové pásy), C 16/20 - XC2 |
| Foundation deepest elevation | -1.050 m (relative to FFL 397.402 m Bpv = ~396.35 m Bpv) |
| Pond floor elevation | 395.15 m Bpv |

**The pond floor is approximately 1.2 m below the house foundation base.** This means the excavation extends well below the level at which the building foundations bear on the soil.

**Structural concerns:**

1. **Foundation influence zone** — A standard rule of thumb is that excavation should not encroach within a 45-degree line drawn from the base of an adjacent foundation. With the foundation base at approximately -1.05 m and the pond floor at approximately -2.5 m, the pond excavation is ~1.45 m deeper than the foundation. At a 45-degree angle, this means any excavation within ~1.45 m horizontally of the foundation edge could undermine bearing capacity. The current 0.1 m gap is **well within this zone**.

2. **Lateral earth pressure** — The terrace and house structure impose surcharge loads on the soil adjacent to the pond. A 2.0-2.5 m deep excavation immediately next to these loads removes the passive resistance that currently supports the soil beneath the terrace and building edge.

3. **Construction phase risk** — Even if the final pond is structurally sound, the temporary open excavation during construction poses the greatest risk. An unsupported 2.5 m deep cut 0.1 m from the terrace could cause settlement or slippage of the terrace and the house foundation edge.

4. **Water level fluctuation** — Cycles of filling and emptying the pond (e.g. for maintenance or a leak) change the lateral pressure on the terrace-side wall. When the pond is full, water pressure supports the wall. When empty, that support is removed.

**What this means for the concrete decision:**

On the **terrace/building side** of the pond, a liner-only solution over a graded earth slope is unlikely to be adequate. The options are:

| Option | Suitability |
|--------|-------------|
| **Reinforced concrete retaining wall** on the terrace side | Most robust. Acts as both a retaining structure protecting the foundations and the pond wall. Can be designed by a structural engineer to account for foundation loads. |
| **Sheet pile or secant pile wall** | Over-engineered for this scale, but technically viable. |
| **Increase the gap** between pond and terrace | Moving the pond further from the building (e.g. 2-3 m) could eliminate the foundation influence zone issue entirely, potentially allowing liner-only construction on all sides. |
| **Stepped excavation** on the building side | Excavate in benches rather than a single deep cut, keeping the deepest excavation further from the foundations. |

**The remaining three sides** of the pond (away from the building) are not subject to the same structural loads. If the soil is stiff and consistent (as S1 suggests), liner-only construction with graded 1:3 slopes should be sufficient on these sides.

**Recommendation:** The terrace-side wall will likely require a concrete retaining structure regardless of what the soil test reveals, because of the foundation proximity. This should be confirmed by a structural engineer who can assess the actual foundation loads and the interaction between the pond excavation and the existing strip foundations. The geotechnical investigation at the pond location should include an assessment of this interface.

### How the Soil Test Answers the Question (for the non-building sides)

The pond-location borehole and trial pit will provide the data needed to determine the construction method for the three sides away from the building:

1. **Is the fill layer consistent and stiff?** If yes — the excavated slopes will hold their shape and liner-only construction is sufficient on the non-building sides.
2. **Is there loose, wet, or variable fill?** If so — those areas may need **localised** concrete retaining walls or gabion baskets. This does not necessarily mean the entire pond requires concrete.
3. **Where is the fill/natural clay boundary?** If the natural clay (Layer III) starts at a different depth than the 1.80 m found at S1, it changes how much of the excavation sits in stable vs. potentially unstable material. The deepest part of the pond (2.0-2.5 m) should ideally be founded in the natural clay.

### Current Assessment

For the **three non-building sides**, indicators from borehole S1 point to liner-only construction being sufficient:

- F5 ML clay at stiff consistency holds excavated slopes well
- Groundwater at 7 m exerts no hydrostatic pressure on pond walls
- The deepest part of the pond (2.0-2.5 m) will sit in undisturbed natural clay below 1.80 m
- The 1:3 slope design is conservative for stiff clay

For the **terrace/building side**, the 0.1 m proximity to the house and the fact that the pond floor sits ~1.2 m below the foundation base means a concrete retaining wall or an increased setback distance is likely required. This is a structural engineering question that should be resolved before final design, independent of the soil test results.

Concrete would also become necessary on other sides if the pond-location investigation reveals materially different conditions — particularly soft or loose fill, or an unexpected water-bearing layer.

### Decision Flowchart

```
Pond-location borehole + trial pit
        |
        v
Soil stiff and consistent (matches S1)?
    |                   |
   YES                  NO
    |                   |
    v                   v
Liner-only          Where is the instability?
construction            |
(EPDM/PVC-P/       +-----------+-----------+
compacted clay)     |           |           |
                Localised    Widespread   Soft/wet
                soft fill    loose fill   throughout
                    |           |           |
                    v           v           v
                Localised   Partial      Full concrete
                retaining   concrete     shell or
                wall/gabion retaining    alternative
                            walls        site location
```

### Construction Method Summary

Based on all available data, the expected construction approach is a **hybrid design** — not fully concrete, not fully liner-only:

| Pond Side | Expected Construction Method | Reason |
|-----------|------------------------------|--------|
| **Terrace/house side (NW)** | **Reinforced concrete retaining wall** with liner over it | Pond floor is ~1.2 m below house foundation base; 0.1 m gap is within the 45-degree foundation influence zone. Concrete is needed here for structural reasons, regardless of soil quality. |
| **Other three sides (NE, SE, SW)** | **Liner-only** (EPDM, PVC-P, or compacted clay) on graded 1:3 earth slopes | No adjacent structural loads; stiff clay (per S1) can hold graded slopes. Subject to confirmation by pond-location soil test. |

**Alternative:** If the pond is moved 2-3 m away from the terrace (clearing the foundation influence zone), liner-only construction may be possible on **all four sides** — eliminating the need for any concrete. This would change the design relationship between the terrace and the pond but would simplify and reduce construction cost.

**Bottom line:** Concrete construction is likely required **only on the terrace/house side** due to the proximity of the house foundations. The other three sides can use liner-only construction, subject to the soil test confirming stiff, consistent clay at the pond location. A structural engineer should confirm the terrace-side approach, and the pond-location borehole and trial pit should be completed before final design.

---

## 10. Boundary Setback Constraints

### What is Known

The feasibility guide states that Czech building regulations typically require setbacks for water features and estimates **2-3 m from parcel boundaries** as a typical figure. However, this has **not been confirmed** for the Jevany site. The actual setback depends on several factors that can only be resolved by consulting the local authorities.

### What Needs to Be Confirmed

| Question | Where to get the answer |
|----------|------------------------|
| What is the minimum setback distance from parcel boundaries for a water feature (vodní dílo / jezírko)? | Územní plán obce Jevany (municipal zoning plan) and/or stavební úřad |
| Is the natural swimming pond classified as a stavba (structure)? | Stavební úřad Jevany — classification determines which setback rules apply |
| Does the permit type (ohlášení stavby vs. stavební povolení) affect setbacks? | Stavební úřad Jevany |
| Do setback requirements differ by boundary type (neighbour, road, public land)? | Územní plán and stavební úřad |
| Are there additional restrictions in the Jevany zoning plan on water features, maximum zastavěná plocha (built-up area), or minimum zelená plocha (green area)? | Územní plán obce Jevany |

### Why This Matters for Pond Positioning and Construction Method

The boundary setback interacts directly with the building proximity issue (§9) and constrains where the pond can be placed on the site:

- If the pond must maintain 2-3 m from the boundary **and** 2-3 m from the building (to clear the foundation influence zone), the available positioning envelope narrows significantly on a 1,091 m² plot
- Conversely, if the pond stays at 0.1 m from the terrace (current design), boundary setbacks on the opposite side determine the maximum pond width
- **The setback requirement may force the pond to be repositioned**, which in turn affects whether a concrete retaining wall is needed on the house side (see §9 — moving the pond 2-3 m from the terrace could eliminate the need for concrete entirely)

### Current Status

**Unconfirmed.** The 2-3 m estimate is a general Czech guideline, not a verified figure for Jevany. This must be confirmed with the stavební úřad before final pond positioning. Listed as a Priority 1 outstanding investigation (§12).

---

## 11. Excavation Estimates

| Parameter | Value |
|-----------|-------|
| Maximum excavation depth | ~2.5 m (swimming zone + liner base) |
| Estimated volume | 110-130 m³ |
| Spoil material | F5 ML clay |
| Spoil reuse | Compacted liner, landscaping berms, slope grading |

Excavation will pass through fill material (0-1.80 m) into natural deluvial clay below. The fill/natural clay boundary at ~1.80 m should be visually confirmed during excavation — the natural clay is described as light brown/pinkish and weakly sandy, distinct from the darker fill material above.

---

## 12. Gravel Substrate Specification

The regeneration zone requires a layered gravel substrate for biological filtration. All gravel must be washed, lime-free, and chemically inert to avoid nutrient leaching or pH changes.

| Layer | Position | Grain size | Purpose |
|-------|----------|------------|---------|
| Coarse | Bottom | 16-32 mm | Drainage, structural support, pipe protection |
| Medium | Middle | 8-16 mm | Transition layer, additional biofilm surface |
| Fine | Top | 2-8 mm | Planting substrate, maximum biofilm surface area |

Total substrate depth: approximately 0.3-0.4 m, sitting within the deep gravel zone (0.6-1.0 m depth).

**Sourcing note:** Gravel should be sourced locally to minimise cost and transport. Given the granite geology, locally quarried granite gravel would be chemically compatible with the site conditions. Limestone gravel must be avoided as it would raise pH and release calcium, disrupting the biological filtration system.

---

## 13. Outstanding Investigations

The following tests and investigations have been identified as necessary but **have not yet been completed**:

### Priority 1 — Required Before Final Design

| Investigation | Purpose | Notes |
|---------------|---------|-------|
| **Structural engineering assessment of building proximity** | Assess interaction between pond excavation and house strip foundations | **Critical.** Pond is 0.1 m from terrace; pond floor is ~1.2 m below foundation base. Must determine whether a concrete retaining wall is needed on the terrace side, or whether the pond should be moved further from the building (see §9). |
| **Geotechnical borehole at pond location** | Verify soil profile matches S1; test permeability at actual pond site | Borehole to 3+ m with in-situ permeability testing. **Also determines whether concrete construction is needed on the non-building sides** (see §9) — if soil is stiff and consistent, liner-only is sufficient; if loose or variable fill is found, localised or full concrete retaining may be required. |
| **Proctor compaction test** on site clay | Determine if excavated clay can be compacted to achieve kv < 10⁻⁸ m/s | Determines viability of compacted clay liner (cheapest option) |
| **Trial pit at pond location** | Visual confirmation of soil layers, fill depth, and natural clay interface | Can be combined with borehole investigation. Confirms fill/natural clay boundary depth and consistency. |
| **Boundary setback confirmation** | Verify minimum distances from parcel boundaries for a water feature | **Consult stavební úřad Jevany and check územní plán.** Setback requirements directly constrain pond positioning, which in turn determines whether a concrete retaining wall is needed on the house side (see §9, §10). Typical Czech estimate is 2-3 m, but unconfirmed for Jevany. |

### Priority 2 — Required Before Construction

| Investigation | Purpose | Notes |
|---------------|---------|-------|
| Utility route survey | Confirm exact positions of underground services at pond location | Cross-reference with C.3 coordination plan |

### Priority 3 — Recommended

| Investigation | Purpose | Notes |
|---------------|---------|-------|
| Water source quality test | Confirm mains water is suitable for initial fill (pH, hardness, chlorine) | May need dechlorination treatment before filling |
| Rainwater quality assessment | Evaluate roof runoff quality for pond top-up use | Check for contaminants from roofing material |

---

## 14. Summary of Key Soil Parameters

| Parameter | Value | Source | Confidence |
|-----------|-------|--------|------------|
| Soil classification | F5 ML (low-plasticity silt/clay) | Borehole S1 (geological survey) | High — consistent through full profile |
| Consistency | Stiff | Borehole S1 | High |
| Fill depth | 0-1.80 m (navazka) | Borehole S1 | Medium — may vary across site |
| Natural clay depth | 1.80 m+ | Borehole S1 | Medium — may vary across site |
| Permeability (kv) | 5.0 x 10⁻⁶ m/s | Borehole S1, per CSN 75 9010 | Medium — single test, single location |
| Groundwater depth | ~7 m | Geological survey | High |
| Bedrock | Ricany-type granite | Geological survey | High |
| Radon index | HIGH (72.3 kBq/m³) | Radon report | High |
| Gas permeability | Medium | Radon report | High |

**Overall assessment:** The site soil conditions are **favourable** for a natural swimming pond. The deep water table, stiff clay, and granite-derived chemistry are all positive factors. The main uncertainty is whether the on-site clay can be compacted to a sufficient seal — this requires the outstanding Proctor compaction test. If not, EPDM or PVC-P liner provides a proven alternative.

---

## References

| Document | Location |
|----------|----------|
| Natural Swimming Pond - Feasibility & Design Guide | `Documents/Natural Swimming Pond - Feasibility & Design Guide.md` |
| Swimming Pond Design - Technical Specification | `Documents/Swimming Pond Design - Technical Specification.md` |
| Geological Survey (original) | `E. Dokladova cast/GEOLOGICKY PRUZKUM/` (not in repository) |
| Radon Report | `E. Dokladova cast/` (referenced, not in repository) |
| Survey Plan Analysis | `Documents/Survey Plan Analysis - 10225.md` |
| CSN 75 9010 | Czech standard for infiltration coefficient testing |
