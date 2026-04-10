# Image Generation Prompt — LUCERN House with Natural Swimming Pond (Schwimmteich)

## Context

- Single-story modern timber-frame house (LUCERN EKO PLUS system), Jevany, Czech Republic
- Flat roof, white silicone render exterior with horizontal timber cladding (larch/thermowood)
- Large floor-to-ceiling glazing, covered terrace with outdoor dining
- Rectangular natural swimming pond (Schwimmteich) extending from the terrace toward the garden
- The existing stone/concrete terrace serves as the pool deck — no separate wooden deck
- Pond is divided into a clear swimming zone (near the terrace) and a planted regeneration/filtration zone (far side), separated by a submerged wall
- Viewpoint: standing at the back of the house, looking southeast across the terrace and pond
- Terrain slopes gently downhill (~2m over 15m) from terrace toward the garden — pond is partially in-ground
- Surrounded by mature deciduous and conifer trees (Central European forest edge)
- Late afternoon golden-hour light, summer

## Reference images

- `images/lucern-house-jevany.jpeg` — the house style (architecture, materials, terrace)
- `images/natural-swimming-pond-jevany.jpeg` — the pond style (water clarity, planting, natural stone, atmosphere)

---

## Midjourney Prompt

Upload both reference images to Midjourney first, then use their image URLs in the prompt:

```
[upload lucern-house-jevany.jpeg] [upload natural-swimming-pond-jevany.jpeg] Combine these two references: the modern single-story house architecture from the first image with a natural swimming pond inspired by the second image, but rectangular. Photorealistic architectural visualization, eye-level view from the covered terrace looking southeast across the garden. The house exactly as shown in image 1 — flat roof, white render with horizontal timber cladding, floor-to-ceiling glass doors, covered terrace with dark dining furniture. The stone terrace serves as the pool deck, with three wide entry steps descending directly from the terrace into a rectangular natural swimming pond (10m x 7.5m). The near half of the pond is a clear swimming zone with crystal turquoise water and a visible gravel bottom, 2 meters deep. A low submerged concrete wall divides the pond at the midpoint. The far half is a shallow regeneration and filtration zone filled with aquatic plants — water lilies, native reeds, rushes, iris, and submerged oxygenating plants growing from a gravel substrate. Natural stone coping borders the pond edges. The terrain slopes gently downhill from the terrace. A matching flat-roofed garage is partially visible 15 meters away beyond the pond. Mature spruce trees, birches, and oaks frame the background, Czech countryside forest edge. Lush green lawn around the pond. Late afternoon golden sunlight, long shadows, warm summer atmosphere. 35mm lens, architectural photography --ar 16:9 --v 6.1 --style raw --sw 200
```

> **Note:** `--sw 200` (style weight) increases the influence of the reference images. Adjust between 100-500. You can also use `--cref` and `--sref` flags for character/style references in newer Midjourney versions.

### Alternative: using /describe + /blend

1. `/describe` each image to get Midjourney's interpretation
2. `/blend` both images together as a starting point
3. Then refine with `/imagine` using the text prompt above

---

## DALL-E / ChatGPT Prompt

In ChatGPT with DALL-E, upload both images to the conversation first, then send:

```
I've uploaded two reference images:
1. A modern single-story house — this is the exact house style I want (flat roof, white render + horizontal timber cladding, floor-to-ceiling glass, covered terrace with dark furniture)
2. A natural swimming pond — this is the water/planting style I want (clear water, natural stone borders, aquatic plants, natural atmosphere)

Create a photorealistic architectural visualization that combines both, but with a RECTANGULAR pond design (a Schwimmteich / natural swimming pool):

Viewpoint: standing on the covered terrace of the house from image 1, looking out southeast across the garden.

The scene should show:
- The house terrace (as in image 1) in the immediate foreground — the covered section with timber ceiling, the concrete/stone paved terrace area
- The terrace IS the pool deck — no separate wooden deck. Three wide stone entry steps descend directly from the terrace edge into the swimming zone
- A rectangular natural swimming pond, 10m long x 7.5m wide, aligned with the building axis
- The NEAR HALF (closest to the terrace) is a clear swimming zone — crystal turquoise water, 2m deep, visible gravel bottom, clean and inviting
- A low submerged separation wall (visible as a subtle line just below the water surface) divides the pond at the midpoint
- The FAR HALF is a regeneration and biological filtration zone — shallower (0.3-0.8m), filled with aquatic plants growing from a gravel substrate: water lilies (Nymphaea), native reeds (Phragmites), rushes, yellow iris (Iris pseudacorus), marsh marigold (Caltha), and submerged oxygenating plants
- Natural stone coping (cut stone or large flat rocks) borders all four edges of the rectangular pond
- The terrain slopes gently downhill from the terrace toward the far edge — the pond is partially set into the ground, with the terrace at the high side
- Lush green lawn around the pond, with some ornamental grasses
- Mature spruce trees, birches, and oaks in the background (Central European forest edge, similar atmosphere to image 2)
- A separate flat-roofed garage building (matching the house style — white render, flat roof) partially visible to the right, about 15 meters from the terrace, beyond the pond
- No fencing or pool barriers

Lighting: late afternoon golden hour, warm summer sunlight casting long shadows. Clear sky. Czech countryside, Jevany (east of Prague).

Style: photorealistic architectural photography, 35mm lens perspective, professional real-estate / architectural magazine quality. The image should feel warm, aspirational, and serene.
```

---

## Stable Diffusion Prompt (with IP-Adapter for image references)

Use IP-Adapter or ControlNet to feed both reference images, then apply this prompt:

```
(masterpiece, best quality, photorealistic:1.3), architectural exterior photography,
modern single-story house with flat roof, white render and horizontal timber cladding,
floor-to-ceiling glass doors, stone terrace as pool deck with entry steps into water,
rectangular natural swimming pool Schwimmteich with crystal clear turquoise water,
near half clear deep swimming zone visible gravel bottom,
far half shallow regeneration zone with aquatic plants water lilies reeds iris growing from gravel substrate,
low submerged separation wall dividing swimming and regeneration zones,
natural stone coping bordering rectangular pond,
view from covered terrace looking southeast across pond,
(lush green garden:1.1), mature spruce trees birch trees oak trees in background,
Czech countryside forest edge setting,
gentle slope downhill from terrace, pond partially set into ground,
flat-roofed garage building visible in distance,
golden hour late afternoon sunlight, warm summer atmosphere, long shadows,
35mm lens, shallow depth of field, architectural photography
Negative prompt: cartoon, illustration, painting, sketch, ugly, deformed, blurry, low quality, watermark, text, kidney shape, organic shape, round pool, wooden deck
```

> **Setup:** Use IP-Adapter with `lucern-house-jevany.jpeg` at weight 0.6 for architectural style, and `natural-swimming-pond-jevany.jpeg` at weight 0.5 for the water/planting style. Use a depth ControlNet if you have a 3D mockup.

---

## Key Design Details for Reference

| Element | Dimension | Notes |
|---------|-----------|-------|
| Total pond area | 75 m2 | Rectangular, aligned with building axis |
| Swimming zone | 38 m2 (5.0m x 7.5m) | 1.9m deep, clear water, gravel bottom |
| Regeneration zone | 38 m2 (5.0m x 7.5m) | 0.1-0.8m deep, planted with native aquatics on gravel substrate |
| Separation wall | 7.5m long | Reinforced concrete, top 0.4m below water surface, 3 water passages |
| Pond overall | 10.0m x 7.5m | Long axis perpendicular to building |
| Deck / terrace | 38 m2 (existing) | Stone/concrete, serves as pool deck |
| Entry steps | 3 steps | 0.3m, 0.6m, 0.9m graduated from terrace into swim zone |
| Pond to garage | ~3m clearance | |
| Terrain drop | ~2m | From terrace (397.2m Bpv) to far edge (395.2m Bpv) |
| Water level | 397.05m Bpv | 0.1m below terrace surface |
| Building orientation | ~40 deg from N | Long axis runs NW-SE |
| Circulation | Skimmer + bottom drain → pump → return to regen zone | Low-energy, chemical-free |
