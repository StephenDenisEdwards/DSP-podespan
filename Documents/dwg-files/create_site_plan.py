"""
Create a new DXF based on the survey plan (10225.dxf) with the building footprint added.

Position is determined by matching the PT (existing terrain) values at house corners
from C.3 to the survey elevation points in the DXF, and using the setback dimensions.
"""

import ezdxf
import math
import os
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(script_dir, "10225.dxf")
out_path = os.path.join(script_dir, "site_plan_with_building.dxf")
vis_path = os.path.join(script_dir, "site_plan_with_building.png")

doc = ezdxf.readfile(src_path)
msp = doc.modelspace()

# --- Site geometry ---
# The western boundary of the combined site runs NW to SE.
# In DXF coordinates, NW-to-SE direction (walking along boundary from NW corner):
# From (-717395.63, -1059595.57) to (-717386.90, -1059606.16):
#   dx = +8.73, dy = -10.59  =>  angle = atan2(-10.59, 8.73) = -50.5 degrees
AXIS_ANGLE = math.radians(-50.5)  # NW to SE along parcel

# Unit vectors
ax_x = math.cos(AXIS_ANGLE)   #  0.637  (along axis, NW->SE)
ax_y = math.sin(AXIS_ANGLE)   # -0.771

# Perpendicular pointing INWARD (from western boundary toward site interior = upper-right in plot)
# Rotate axis 90 degrees counter-clockwise to get inward perpendicular
perp_x = -ax_y   #  0.771
perp_y = ax_x    #  0.637

# Verify: from western boundary point (-717395.63, -1059595.57),
# moving in perp direction should go toward (-717386.62, -1059580.91) (NW cross-boundary end)
# Vector: (+9.01, +14.66) -- both positive = upper-right -- matches (perp_x>0, perp_y>0) ✓

# --- Building dimensions (from C.3 and D.1.1.3) ---
HOUSE_LENGTH = 17.220  # along parcel axis
HOUSE_WIDTH = 14.820   # perpendicular to axis
GARAGE_WIDTH = 3.660   # perpendicular
GARAGE_DEPTH = 4.920   # along axis (18.00 / 3.66)
TERRACE_DEPTH = 3.000  # perpendicular, approximate
TERRACE_LENGTH = 38.18 / TERRACE_DEPTH  # ~12.7m along house face

# Setbacks from C.3
SETBACK_WEST = 3.140  # from western boundary (parcel 154/11 side)

# --- Position the building using elevation matching ---
# C.3 shows PT (existing terrain) at 5 building corner positions:
#   PT=398.694, PT=397.425, PT=397.146, PT=397.235, PT=396.870
#
# The closest survey elevation points in the DXF are:
#   398.76 at (-717383.25, -1059584.80)  -- matches PT=398.694 (uphill/SW corner)
#   397.22 at (-717387.65, -1059588.48)  -- matches PT=397.235
#   397.15 at (-717378.64, -1059593.99)  -- matches PT=397.146
#   397.46 at (-717366.88, -1059597.37)  -- matches PT=397.425
#   396.89 at (-717379.06, -1059613.86)  -- matches PT=396.870 (downhill corner)
#
# The house sits where terrain is 397-399m.
# The western boundary near the house runs from (-717395.63,-1059595.57) SE.
# The setback is 3.14m from this boundary, perpendicular inward.

# Reference point: start from western boundary, offset inward by setback
# Use a point on the western boundary that aligns with the building area.
# The 398.76 elevation point (uphill corner) at (-717383.25, -1059584.80) is
# near the NW cross-boundary. The building's uphill (NW) end should be near here.
#
# Project the 398.76 point onto the western boundary to find the reference.
# Western boundary line: P0=(-717395.63, -1059595.57), direction=(ax_x, ax_y)
# The projection of the elevation point onto this line gives us the axial position.

P0 = np.array([-717395.63, -1059595.57])
axis_dir = np.array([ax_x, ax_y])
perp_dir = np.array([perp_x, perp_y])

# Project the high-elevation point onto the boundary
pt_high = np.array([-717383.25, -1059584.80])
v = pt_high - P0
t_along = np.dot(v, axis_dir)   # distance along axis from P0
t_perp = np.dot(v, perp_dir)    # distance perpendicular from boundary

print(f"High point projection: along={t_along:.2f}m, perp={t_perp:.2f}m from western boundary")

# The NW corner of the house (uphill end, boundary side) should be:
# - On the axis at roughly t_along (same axial position as the high elev point)
# - At SETBACK_WEST (3.14m) perpendicular from the boundary
house_nw_corner = P0 + t_along * axis_dir + SETBACK_WEST * perp_dir

# From the NW corner (boundary-side, uphill), compute all 4 corners:
# The house extends along the axis (toward SE) by HOUSE_LENGTH
# The house extends perpendicular (inward) by HOUSE_WIDTH
#
# Corner naming (relative to the parcel, not compass):
#   NW = uphill, boundary side
#   NE = uphill, interior side
#   SW = downhill, boundary side (toward SE along axis)
#   SE = downhill, interior side

c_nw = house_nw_corner  # boundary side, uphill end
c_ne = c_nw + HOUSE_WIDTH * perp_dir  # interior side, uphill end
c_sw = c_nw + HOUSE_LENGTH * axis_dir  # boundary side, downhill end
c_se = c_sw + HOUSE_WIDTH * perp_dir  # interior side, downhill end

print(f"\nHouse corners:")
print(f"  NW (boundary, uphill): ({c_nw[0]:.2f}, {c_nw[1]:.2f})")
print(f"  NE (interior, uphill): ({c_ne[0]:.2f}, {c_ne[1]:.2f})")
print(f"  SW (boundary, downhill): ({c_sw[0]:.2f}, {c_sw[1]:.2f})")
print(f"  SE (interior, downhill): ({c_se[0]:.2f}, {c_se[1]:.2f})")

# Check elevations at corners
elev_points = {}
for e in msp.query('TEXT'):
    t = e.dxf.text.strip()
    parts = t.split()
    if len(parts) == 2:
        try:
            val = float(parts[0]) + float(parts[1]) / 100
            if 392 < val < 400:
                pos = e.dxf.insert
                elev_points[t] = (pos.x, pos.y, val)
        except ValueError:
            pass

for name, corner in [("NW", c_nw), ("NE", c_ne), ("SW", c_sw), ("SE", c_se)]:
    best = min(elev_points.items(), key=lambda ep: math.sqrt((ep[1][0]-corner[0])**2 + (ep[1][1]-corner[1])**2))
    dist = math.sqrt((best[1][0]-corner[0])**2 + (best[1][1]-corner[1])**2)
    print(f"  {name}: nearest survey elev = {best[1][2]:.2f}m ('{best[0]}'), dist={dist:.1f}m")

# --- Verify position makes sense ---
# Check distance from western boundary at each corner
for name, corner in [("NW", c_nw), ("SW", c_sw)]:
    # Project onto boundary to find perpendicular distance
    v = corner - P0
    d_perp = np.dot(v, perp_dir)
    print(f"  {name} distance from western boundary: {d_perp:.2f}m (should be ~{SETBACK_WEST})")

for name, corner in [("NE", c_ne), ("SE", c_se)]:
    v = corner - P0
    d_perp = np.dot(v, perp_dir)
    print(f"  {name} distance from western boundary: {d_perp:.2f}m (should be ~{SETBACK_WEST + HOUSE_WIDTH})")

# --- Create layers ---
if "BUILDING" not in doc.layers:
    doc.layers.add("BUILDING", color=1)
if "GARAGE" not in doc.layers:
    doc.layers.add("GARAGE", color=3)
if "TERRACE" not in doc.layers:
    doc.layers.add("TERRACE", color=5)
if "BUILDING_LABEL" not in doc.layers:
    doc.layers.add("BUILDING_LABEL", color=1)

# --- Draw house footprint ---
house_corners = [tuple(c_nw), tuple(c_sw), tuple(c_se), tuple(c_ne)]
msp.add_lwpolyline(house_corners, close=True, dxfattribs={"layer": "BUILDING", "lineweight": 50})

# House label
center = (c_nw + c_sw + c_se + c_ne) / 4
rot_deg = math.degrees(AXIS_ANGLE)
msp.add_text("RD EDWARDS", dxfattribs={
    "layer": "BUILDING_LABEL", "height": 1.5, "rotation": rot_deg,
    "insert": (center[0] - 1 * perp_x, center[1] - 1 * perp_y),
})
msp.add_text("180.38 m2", dxfattribs={
    "layer": "BUILDING_LABEL", "height": 1.0, "rotation": rot_deg,
    "insert": (center[0] + 1 * perp_x, center[1] + 1 * perp_y),
})
msp.add_text("FFL +/-0.000 = 397.402 Bpv", dxfattribs={
    "layer": "BUILDING_LABEL", "height": 0.7, "rotation": rot_deg,
    "insert": (center[0] + 3 * perp_x, center[1] + 3 * perp_y),
})

# --- Garage ---
# From C.3: garage (SO-01b) is near the entrance (vjezd), FFL = 397.052 Bpv.
# It's 350mm lower than the house, so it's adjacent to the house, not far away.
# From the C.3 layout: "VJEZD GARÁŽ" is labeled near the access road side.
# The access is from Na Petřínku road which runs along the eastern boundary.
# Place the garage on the interior (eastern) side of the house at the SE (downhill) end,
# where the driveway arrives from the access road.
# The garage extends along the axis from the house SE corner.
garage_origin = c_sw + HOUSE_LENGTH * axis_dir + 1.0 * axis_dir  # 1m past house SE boundary-side corner
# But place it on the interior side, not the boundary side
garage_origin = c_se + 1.5 * axis_dir  # 1.5m gap from house, interior side
# Actually, the garage should be between the house and the access road,
# which comes from the SE direction. Place it adjacent to the downhill end of the house.
garage_origin = c_sw + 1.0 * perp_dir  # offset inward from house SW corner
g_corners = [
    tuple(garage_origin),
    tuple(garage_origin + GARAGE_DEPTH * axis_dir),
    tuple(garage_origin + GARAGE_DEPTH * axis_dir + GARAGE_WIDTH * perp_dir),
    tuple(garage_origin + GARAGE_WIDTH * perp_dir),
]
msp.add_lwpolyline(g_corners, close=True, dxfattribs={"layer": "GARAGE", "lineweight": 50})

g_center = np.mean([np.array(c) for c in g_corners], axis=0)
msp.add_text("GARAZ", dxfattribs={
    "layer": "BUILDING_LABEL", "height": 0.8, "rotation": rot_deg,
    "insert": (g_center[0], g_center[1]),
})
msp.add_text("18.00 m2", dxfattribs={
    "layer": "BUILDING_LABEL", "height": 0.6, "rotation": rot_deg,
    "insert": (g_center[0] + 1.2*perp_x, g_center[1] + 1.2*perp_y),
})

# --- Terrace ---
# Terrace is on the garden/interior side of the house (east side, away from western boundary).
# It extends along the house face, roughly centered.
# Place it along the interior (NE) face of the house, roughly centered on the house length.
terrace_offset = (HOUSE_LENGTH - TERRACE_LENGTH) / 2  # center the terrace
terrace_origin = c_ne + terrace_offset * axis_dir  # start along interior face, offset from NE corner
t_corners = [
    tuple(terrace_origin),
    tuple(terrace_origin + TERRACE_LENGTH * axis_dir),
    tuple(terrace_origin + TERRACE_LENGTH * axis_dir + TERRACE_DEPTH * perp_dir),
    tuple(terrace_origin + TERRACE_DEPTH * perp_dir),
]
msp.add_lwpolyline(t_corners, close=True, dxfattribs={"layer": "TERRACE", "lineweight": 30})

t_center = np.mean([np.array(c) for c in t_corners], axis=0)
msp.add_text("TERASA", dxfattribs={
    "layer": "BUILDING_LABEL", "height": 0.8, "rotation": rot_deg,
    "insert": (t_center[0], t_center[1]),
})

# --- Save DXF ---
doc.saveas(out_path)
print(f"\nSaved DXF: {out_path}")

# --- Visualize ---
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import LineCollection

fig, ax = plt.subplots(1, 1, figsize=(16, 20))

# Survey lines (background)
lines, line_colors = [], []
for e in msp.query("LINE"):
    layer = e.dxf.get("layer", "0")
    if layer in ("BUILDING", "GARAGE", "TERRACE", "BUILDING_LABEL"):
        continue
    s, end = e.dxf.start, e.dxf.end
    lines.append([(s.x, s.y), (end.x, end.y)])
    line_colors.append('#333333' if layer == '1' else '#AAAAAA')
if lines:
    ax.add_collection(LineCollection(lines, colors=line_colors, linewidths=0.4))

# Survey polylines, circles, arcs, points, inserts
for e in msp.query("LWPOLYLINE"):
    layer = e.dxf.get("layer", "0")
    pts = list(e.get_points(format="xy"))
    if e.closed:
        pts.append(pts[0])
    if len(pts) < 2:
        continue
    xs, ys = zip(*pts)
    if layer == "BUILDING":
        ax.fill(xs, ys, alpha=0.25, color='red')
        ax.plot(xs, ys, color='red', linewidth=2.5, label='House (RD Edwards)')
    elif layer == "GARAGE":
        ax.fill(xs, ys, alpha=0.25, color='green')
        ax.plot(xs, ys, color='green', linewidth=2.0, label='Garage')
    elif layer == "TERRACE":
        ax.fill(xs, ys, alpha=0.15, color='blue')
        ax.plot(xs, ys, color='blue', linewidth=1.5, linestyle='--', label='Terrace')
    else:
        ax.plot(xs, ys, color='#666666', linewidth=0.5)

for e in msp.query("CIRCLE"):
    c, r = e.dxf.center, e.dxf.radius
    ax.add_patch(plt.Circle((c.x, c.y), r, fill=False, edgecolor='#888', linewidth=0.3))

for e in msp.query("ARC"):
    c, r = e.dxf.center, e.dxf.radius
    ax.add_patch(mpatches.Arc((c.x, c.y), 2*r, 2*r, angle=0,
        theta1=e.dxf.start_angle, theta2=e.dxf.end_angle, edgecolor='#888', linewidth=0.3))

for e in msp.query("INSERT"):
    pos = e.dxf.insert
    ax.plot(pos.x, pos.y, '+', color='#BBB', markersize=2, markeredgewidth=0.3)

# Text labels
for e in msp.query("TEXT"):
    layer = e.dxf.get("layer", "0")
    pos = e.dxf.insert
    if layer == "BUILDING_LABEL":
        ax.text(pos.x, pos.y, e.dxf.text, fontsize=7, color='red',
                rotation=e.dxf.get("rotation", 0), ha='left', va='bottom', fontweight='bold')
    elif layer == "18":
        ax.text(pos.x, pos.y, e.dxf.text, fontsize=6, color='#E91E63',
                rotation=e.dxf.get("rotation", 0), ha='left', va='bottom', fontweight='bold')
    else:
        fontsize = max(3, min(e.dxf.height * 1.8, 5))
        ax.text(pos.x, pos.y, e.dxf.text, fontsize=fontsize, color='#888',
                rotation=e.dxf.get("rotation", 0), ha='left', va='bottom')

ax.set_aspect('equal')
ax.autoscale()
ax.set_xlabel('X (S-JTSK)')
ax.set_ylabel('Y (S-JTSK)')
ax.set_title('Site Plan with Building — RD Edwards, Jevany', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.15, linewidth=0.3)
ax.tick_params(labelsize=7)
ax.legend(loc='upper left', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig(vis_path, dpi=200, bbox_inches='tight')
print(f"Saved visualization: {vis_path}")
plt.close()
