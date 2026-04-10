"""
Rectangular natural swimming pond (Schwimmteich) design.
- Terrace serves as the wooden deck
- Proper swimming zone + regeneration/filtration zone
- Separation wall, circulation system, depth zoning
"""
import ezdxf
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import matplotlib.patheffects as pe

# === Transform parameters ===
a_p = 0.000999628440
b_p = 0.000000223925
tx_p = -717879.783827
ty_p = -1059415.885979

def transform(x, y):
    return (a_p*x - b_p*y + tx_p, b_p*x + a_p*y + ty_p)

# === Building geometry ===
building_c3 = [
    (487302.099, -178539.936), (492749.529, -185090.959),
    (493380.027, -184566.676), (499362.064, -179592.380),
    (504924.580, -186281.805), (507538.839, -184107.947),
    (509707.135, -182304.925), (498697.189, -169064.477),
]
terrace_c3 = [
    (499413.877, -179029.071), (493130.206, -184254.187),
    (495298.136, -186873.375), (500511.274, -182538.448),
    (504155.681, -186921.174), (507538.839, -184107.947),
    (507027.343, -183492.827), (504720.646, -185410.936),
]
garage_c3 = [
    (503145.036, -197931.664), (505310.915, -195855.859),
    (509462.525, -200187.618), (507296.646, -202263.423),
]
access_road_c3 = [
    (498131.446, -166819.679), (498362.116, -166627.868),
    (507829.733, -178013.528), (507599.063, -178205.339),
]
access_road2_c3 = [
    (507829.733, -178013.528), (507599.063, -178205.339),
    (513353.390, -185125.434), (513584.060, -184933.623),
]

building_sj = [transform(*p) for p in building_c3]
terrace_sj = [transform(*p) for p in terrace_c3]
garage_sj = [transform(*p) for p in garage_c3]
road1_sj = [transform(*p) for p in access_road_c3]
road2_sj = [transform(*p) for p in access_road2_c3]

# === Local coordinate system ===
# Origin: terrace vertex 0
# u-axis: perpendicular to building axis (negative = toward SE/garden)
# v-axis: along building long axis
axis_angle = math.radians(129.7)  # building axis angle
origin_sj = terrace_sj[0]

cos_a = math.cos(axis_angle)
sin_a = math.sin(axis_angle)

def local_to_sjtsk(u, v):
    """Convert building-local (u, v) to S-JTSK."""
    ca = math.cos(axis_angle)
    sa = math.sin(axis_angle)
    dx = u * ca - v * sa
    dy = u * sa + v * ca
    return (origin_sj[0] + dx, origin_sj[1] + dy)

def sjtsk_to_local(sx, sy):
    ca = math.cos(axis_angle)
    sa = math.sin(axis_angle)
    dx = sx - origin_sj[0]
    dy = sy - origin_sj[1]
    u = dx * ca + dy * sa
    v = -dx * sa + dy * ca
    return u, v

# Verify terrace vertices in local coords
for i, (sx, sy) in enumerate(terrace_sj):
    u, v = sjtsk_to_local(sx, sy)

# ============================================================
# POND DESIGN - Rectangular Schwimmteich
# ============================================================

# The terrace outer edge at u=-3.40 (from v=1.40 to v=8.18) is the main deck edge.
# The terrace also extends to u=-9.10 at v=1.40, providing additional deck along the near side.

# Pond rectangle (in local coords):
POND_U_START = -3.50    # just off the terrace edge (0.1m gap for coping stone)
POND_U_END = -13.50     # ~3m from garage (garage at u ~ -16.7)
POND_V_START = 1.50     # starts at terrace step (v=1.40), avoids right arm overlap
POND_V_END = 9.00       # extend slightly past terrace left edge

POND_DEPTH = abs(POND_U_END - POND_U_START)  # 10.0m
POND_WIDTH = POND_V_END - POND_V_START       # 7.5m
POND_AREA = POND_DEPTH * POND_WIDTH

# Separation wall position (divides swimming from regeneration)
WALL_U = -8.50  # 5.0m from terrace edge

SWIM_DEPTH = abs(WALL_U - POND_U_START)  # 5.0m
REGEN_DEPTH = abs(POND_U_END - WALL_U)   # 5.0m
SWIM_AREA = SWIM_DEPTH * POND_WIDTH
REGEN_AREA = REGEN_DEPTH * POND_WIDTH

print(f"=== POND DIMENSIONS ===")
print(f"Overall: {POND_DEPTH:.1f}m x {POND_WIDTH:.1f}m = {POND_AREA:.0f} m2")
print(f"Swimming zone: {SWIM_DEPTH:.1f}m x {POND_WIDTH:.1f}m = {SWIM_AREA:.0f} m2")
print(f"Regeneration zone: {REGEN_DEPTH:.1f}m x {POND_WIDTH:.1f}m = {REGEN_AREA:.0f} m2")
print(f"Ratio swim:regen = {SWIM_AREA/POND_AREA*100:.0f}:{REGEN_AREA/POND_AREA*100:.0f}")

# === Pond elements in local coords ===

# Pond outer rectangle
pond_rect = [
    (POND_U_START, POND_V_START),
    (POND_U_START, POND_V_END),
    (POND_U_END, POND_V_END),
    (POND_U_END, POND_V_START),
]

# Separation wall (with 3 water passages)
wall_line = [(WALL_U, POND_V_START), (WALL_U, POND_V_END)]
# Water passages (0.5m wide openings in the wall)
passage_width = 0.5
passages = [
    ((WALL_U, POND_V_START + 1.5), (WALL_U, POND_V_START + 2.0)),
    ((WALL_U, (POND_V_START + POND_V_END)/2 - 0.25), (WALL_U, (POND_V_START + POND_V_END)/2 + 0.25)),
    ((WALL_U, POND_V_END - 2.0), (WALL_U, POND_V_END - 1.5)),
]

# Swimming zone
swim_rect = [
    (POND_U_START, POND_V_START),
    (POND_U_START, POND_V_END),
    (WALL_U, POND_V_END),
    (WALL_U, POND_V_START),
]

# Regeneration zone
regen_rect = [
    (WALL_U, POND_V_START),
    (WALL_U, POND_V_END),
    (POND_U_END, POND_V_END),
    (POND_U_END, POND_V_START),
]

# Shallow planting shelves in regeneration zone (stepped depths)
# Shelf 1: 0.1-0.3m deep (marginal plants) - 1m wide border
shelf1 = [
    (WALL_U - 0.1, POND_V_START + 0.1),
    (WALL_U - 0.1, POND_V_END - 0.1),
    (POND_U_END + 0.1, POND_V_END - 0.1),
    (POND_U_END + 0.1, POND_V_START + 0.1),
    # Inner boundary
]
shelf1_inner = [
    (WALL_U - 1.0, POND_V_START + 1.0),
    (WALL_U - 1.0, POND_V_END - 1.0),
    (POND_U_END + 1.0, POND_V_END - 1.0),
    (POND_U_END + 1.0, POND_V_START + 1.0),
]

# Gravel filter bed (center of regen zone, 0.5-0.8m deep)
gravel_bed = [
    (WALL_U - 1.5, POND_V_START + 1.5),
    (WALL_U - 1.5, POND_V_END - 1.5),
    (POND_U_END + 1.5, POND_V_END - 1.5),
    (POND_U_END + 1.5, POND_V_START + 1.5),
]

# Entry steps (in swimming zone, near terrace, v centered)
steps_v_center = (POND_V_START + POND_V_END) / 2
steps = [
    (POND_U_START, steps_v_center - 1.5, POND_U_START - 0.4, steps_v_center + 1.5, -0.3),
    (POND_U_START - 0.4, steps_v_center - 1.2, POND_U_START - 0.8, steps_v_center + 1.2, -0.6),
    (POND_U_START - 0.8, steps_v_center - 0.9, POND_U_START - 1.2, steps_v_center + 0.9, -0.9),
]

# Circulation system
skimmer_pos = (POND_U_START - 0.3, POND_V_END - 1.0)  # near terrace, left end
bottom_drain_pos = (POND_U_START - 2.5, steps_v_center)  # center of swim zone
pump_chamber_pos = (WALL_U - 0.5, POND_V_END + 0.8)  # outside pond near wall
inlet_pos = (POND_U_END + 0.5, POND_V_START + 2.0)  # return into regen far end

# Pipe route: skimmer -> pump -> regen zone inlet
# Also: bottom drain -> pump

# === Convert to S-JTSK and create DXF ===
def rect_to_sj(rect):
    return [local_to_sjtsk(u, v) for u, v in rect]

pond_sj = rect_to_sj(pond_rect)
swim_sj = rect_to_sj(swim_rect)
regen_sj = rect_to_sj(regen_rect)
shelf1_inner_sj = rect_to_sj(shelf1_inner)
gravel_sj = rect_to_sj(gravel_bed)

wall_sj = [local_to_sjtsk(*p) for p in wall_line]

# DXF output
doc = ezdxf.readfile('10225.dxf')
msp = doc.modelspace()

doc.layers.add('BUILDING_FOOTPRINT', color=1)
doc.layers.add('BUILDING_TERRACE', color=14)
doc.layers.add('BUILDING_GARAGE', color=8)
doc.layers.add('BUILDING_ACCESS', color=8)
doc.layers.add('BUILDING_LABELS', color=7)
doc.layers.add('POND_OUTLINE', color=4)
doc.layers.add('POND_SWIM_ZONE', color=140)
doc.layers.add('POND_REGEN_ZONE', color=80)
doc.layers.add('POND_SEPARATION_WALL', color=252)
doc.layers.add('POND_GRAVEL_BED', color=42)
doc.layers.add('POND_SHELF', color=70)
doc.layers.add('POND_CIRCULATION', color=6)
doc.layers.add('POND_STEPS', color=14)
doc.layers.add('POND_DIMENSIONS', color=7)

msp.add_lwpolyline(building_sj, dxfattribs={'layer': 'BUILDING_FOOTPRINT'}, close=True)
msp.add_lwpolyline(terrace_sj, dxfattribs={'layer': 'BUILDING_TERRACE'}, close=True)
msp.add_lwpolyline(garage_sj, dxfattribs={'layer': 'BUILDING_GARAGE'}, close=True)
msp.add_lwpolyline(road1_sj, dxfattribs={'layer': 'BUILDING_ACCESS'}, close=True)
msp.add_lwpolyline(road2_sj, dxfattribs={'layer': 'BUILDING_ACCESS'}, close=True)

# Pond
msp.add_lwpolyline(pond_sj, dxfattribs={'layer': 'POND_OUTLINE', 'lineweight': 50}, close=True)
msp.add_lwpolyline(swim_sj, dxfattribs={'layer': 'POND_SWIM_ZONE'}, close=True)
msp.add_lwpolyline(regen_sj, dxfattribs={'layer': 'POND_REGEN_ZONE'}, close=True)
msp.add_lwpolyline(shelf1_inner_sj, dxfattribs={'layer': 'POND_SHELF'}, close=True)
msp.add_lwpolyline(gravel_sj, dxfattribs={'layer': 'POND_GRAVEL_BED'}, close=True)

# Separation wall (solid segments with gaps for passages)
wall_segments_v = [POND_V_START]
for (_, v1), (_, v2) in passages:
    wall_segments_v.extend([v1, v2])
wall_segments_v.append(POND_V_END)

for i in range(0, len(wall_segments_v), 2):
    p1 = local_to_sjtsk(WALL_U, wall_segments_v[i])
    p2 = local_to_sjtsk(WALL_U, wall_segments_v[i+1])
    msp.add_line(p1, p2, dxfattribs={'layer': 'POND_SEPARATION_WALL', 'lineweight': 35})

# Entry steps
for u1, v1, u2, v2, depth in steps:
    step_pts = [
        local_to_sjtsk(u1, v1), local_to_sjtsk(u1, v2),
        local_to_sjtsk(u2, v2), local_to_sjtsk(u2, v1),
    ]
    msp.add_lwpolyline(step_pts, dxfattribs={'layer': 'POND_STEPS'}, close=True)

# Circulation elements
sk = local_to_sjtsk(*skimmer_pos)
bd = local_to_sjtsk(*bottom_drain_pos)
pc = local_to_sjtsk(*pump_chamber_pos)
inlet = local_to_sjtsk(*inlet_pos)

msp.add_circle(sk, radius=0.3, dxfattribs={'layer': 'POND_CIRCULATION'})
msp.add_circle(bd, radius=0.25, dxfattribs={'layer': 'POND_CIRCULATION'})
msp.add_circle(inlet, radius=0.3, dxfattribs={'layer': 'POND_CIRCULATION'})
# Pump chamber rectangle
pc_rect = [
    local_to_sjtsk(pump_chamber_pos[0]-0.4, pump_chamber_pos[1]-0.4),
    local_to_sjtsk(pump_chamber_pos[0]+0.4, pump_chamber_pos[1]-0.4),
    local_to_sjtsk(pump_chamber_pos[0]+0.4, pump_chamber_pos[1]+0.4),
    local_to_sjtsk(pump_chamber_pos[0]-0.4, pump_chamber_pos[1]+0.4),
]
msp.add_lwpolyline(pc_rect, dxfattribs={'layer': 'POND_CIRCULATION'}, close=True)

# Pipe routes (dashed lines)
msp.add_line(sk, pc, dxfattribs={'layer': 'POND_CIRCULATION', 'linetype': 'DASHED'})
msp.add_line(bd, pc, dxfattribs={'layer': 'POND_CIRCULATION', 'linetype': 'DASHED'})
msp.add_line(pc, inlet, dxfattribs={'layer': 'POND_CIRCULATION', 'linetype': 'DASHED'})

# Labels
msp.add_text('RD EDWARDS', dxfattribs={'layer': 'BUILDING_LABELS', 'height': 1.2,
             'insert': transform(494471, -178491)})
msp.add_text('GARAZ', dxfattribs={'layer': 'BUILDING_LABELS', 'height': 1.0,
             'insert': transform(505783, -200993)})

doc.saveas('schwimmteich_plan_v3.dxf')
print('Saved schwimmteich_plan.dxf')

# ============================================================
# VISUALIZATION
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(24, 16), gridspec_kw={'width_ratios': [3, 2]})

# --- LEFT: Site plan view ---
ax = axes[0]

# Survey base
doc_draw = ezdxf.readfile('10225.dxf')
msp_draw = doc_draw.modelspace()
for e in msp_draw:
    if e.dxftype() == 'LINE' and e.dxf.layer == '1':
        s, en = e.dxf.start, e.dxf.end
        ax.plot([s[0], en[0]], [s[1], en[1]], color='#dddddd', linewidth=0.2)
    elif e.dxftype() == 'LINE' and e.dxf.layer == '4':
        s, en = e.dxf.start, e.dxf.end
        ax.plot([s[0], en[0]], [s[1], en[1]], color='#aaaaaa', linewidth=0.5)
for e in msp_draw:
    if e.dxftype() == 'TEXT' and e.dxf.layer == '18':
        p = e.dxf.insert
        ax.annotate(e.dxf.text, (p[0], p[1]), fontsize=5, color='darkblue',
                   fontweight='bold', ha='center', alpha=0.5)

def plot_poly(ax, pts, color, lw, label=None, fill=False, alpha=0.25, ls='-', zo=2):
    xs = [p[0] for p in pts] + [pts[0][0]]
    ys = [p[1] for p in pts] + [pts[0][1]]
    if fill:
        ax.fill(xs, ys, alpha=alpha, color=color, zorder=zo)
    ax.plot(xs, ys, color=color, linewidth=lw, linestyle=ls, label=label, zorder=zo+1)

# Building
plot_poly(ax, building_sj, '#cc3333', 2.0, 'Building (180 m\u00b2)', fill=True, alpha=0.2, zo=5)
plot_poly(ax, terrace_sj, '#A0522D', 1.5, 'Terrace = deck', fill=True, alpha=0.4, zo=6)
plot_poly(ax, garage_sj, '#666666', 1.5, 'Garage', fill=True, alpha=0.3, zo=5)
plot_poly(ax, road1_sj, '#bbbbbb', 0.5, 'Access road', ls='--', zo=2)
plot_poly(ax, road2_sj, '#bbbbbb', 0.5, None, ls='--', zo=2)

# Pond - regeneration zone (green)
plot_poly(ax, regen_sj, '#2E7D32', 1.5, f'Regeneration zone ({REGEN_AREA:.0f} m\u00b2)',
          fill=True, alpha=0.25, zo=7)

# Pond - swimming zone (blue)
plot_poly(ax, swim_sj, '#0277BD', 2.0, f'Swimming zone ({SWIM_AREA:.0f} m\u00b2)',
          fill=True, alpha=0.3, zo=8)

# Gravel bed
plot_poly(ax, gravel_sj, '#8D6E63', 0.8, 'Gravel filter bed', fill=True, alpha=0.2, zo=8)

# Planting shelf
plot_poly(ax, shelf1_inner_sj, '#4CAF50', 0.6, 'Planting shelf (0.1-0.3m)', ls=':', zo=8)

# Separation wall
for i in range(0, len(wall_segments_v), 2):
    p1 = local_to_sjtsk(WALL_U, wall_segments_v[i])
    p2 = local_to_sjtsk(WALL_U, wall_segments_v[i+1])
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='#424242', linewidth=3.0, solid_capstyle='round',
            zorder=10, label='Separation wall' if i == 0 else None)

# Water passages
for (_, v1), (_, v2) in passages:
    p1 = local_to_sjtsk(WALL_U, v1)
    p2 = local_to_sjtsk(WALL_U, v2)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='#29B6F6', linewidth=4.0, solid_capstyle='round',
            zorder=11)
# Label one passage
pw = local_to_sjtsk(WALL_U, (POND_V_START+POND_V_END)/2)
ax.annotate('water\npassage', pw, fontsize=4, color='#0277BD', ha='center', va='center', zorder=12)

# Entry steps
for u1, v1, u2, v2, depth in steps:
    step_pts = [
        local_to_sjtsk(u1, v1), local_to_sjtsk(u1, v2),
        local_to_sjtsk(u2, v2), local_to_sjtsk(u2, v1),
    ]
    plot_poly(ax, step_pts, '#BDBDBD', 0.5, None, fill=True, alpha=0.3, zo=9)

step_label = local_to_sjtsk(POND_U_START - 0.6, steps_v_center)
ax.annotate('entry\nsteps', step_label, fontsize=4, color='#757575', ha='center', va='center', zorder=12)

# Circulation system
ax.plot(*local_to_sjtsk(*skimmer_pos), 'o', color='#E65100', markersize=6, zorder=12)
ax.annotate('SK', local_to_sjtsk(*skimmer_pos), fontsize=4, color='#E65100',
            ha='center', va='bottom', fontweight='bold', xytext=(0,4), textcoords='offset points', zorder=12)

ax.plot(*local_to_sjtsk(*bottom_drain_pos), 's', color='#E65100', markersize=5, zorder=12)
ax.annotate('BD', local_to_sjtsk(*bottom_drain_pos), fontsize=4, color='#E65100',
            ha='center', va='bottom', fontweight='bold', xytext=(0,4), textcoords='offset points', zorder=12)

pc_sj = local_to_sjtsk(*pump_chamber_pos)
ax.plot(*pc_sj, 'D', color='#E65100', markersize=7, zorder=12)
ax.annotate('PUMP', pc_sj, fontsize=4, color='#E65100',
            ha='center', va='bottom', fontweight='bold', xytext=(0,5), textcoords='offset points', zorder=12)

ax.plot(*local_to_sjtsk(*inlet_pos), 'v', color='#2E7D32', markersize=6, zorder=12)
ax.annotate('IN', local_to_sjtsk(*inlet_pos), fontsize=4, color='#2E7D32',
            ha='center', va='bottom', fontweight='bold', xytext=(0,4), textcoords='offset points', zorder=12)

# Pipe routes
for p1, p2, c in [(local_to_sjtsk(*skimmer_pos), pc_sj, '#E65100'),
                   (local_to_sjtsk(*bottom_drain_pos), pc_sj, '#E65100'),
                   (pc_sj, local_to_sjtsk(*inlet_pos), '#2E7D32')]:
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=c, linewidth=0.8, linestyle='--', alpha=0.6, zorder=9)

# Flow arrows in regen zone
for v_pos in [2.0, 5.0, 7.5]:
    a1 = local_to_sjtsk(POND_U_END + 0.8, v_pos)
    a2 = local_to_sjtsk(WALL_U - 0.5, v_pos)
    ax.annotate('', xy=a2, xytext=a1,
                arrowprops=dict(arrowstyle='->', color='#66BB6A', lw=0.8, alpha=0.5), zorder=9)

# Dimension annotations
# Pond width
dw1 = local_to_sjtsk(POND_U_END - 0.5, POND_V_START)
dw2 = local_to_sjtsk(POND_U_END - 0.5, POND_V_END)
ax.annotate('', xy=dw2, xytext=dw1,
            arrowprops=dict(arrowstyle='<->', color='#333333', lw=0.8), zorder=15)
dw_mid = local_to_sjtsk(POND_U_END - 1.2, (POND_V_START+POND_V_END)/2)
ax.annotate(f'{POND_WIDTH:.1f}m', dw_mid, fontsize=6, color='#333333', ha='center', zorder=15,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=1))

# Pond depth
dd1 = local_to_sjtsk(POND_U_START, POND_V_END + 0.5)
dd2 = local_to_sjtsk(POND_U_END, POND_V_END + 0.5)
ax.annotate('', xy=dd2, xytext=dd1,
            arrowprops=dict(arrowstyle='<->', color='#333333', lw=0.8), zorder=15)
dd_mid = local_to_sjtsk((POND_U_START+POND_U_END)/2, POND_V_END + 1.2)
ax.annotate(f'{POND_DEPTH:.1f}m', dd_mid, fontsize=6, color='#333333', ha='center', zorder=15,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=1))

# Labels
ax.annotate('RD EDWARDS', transform(494471, -178491), fontsize=8, color='darkred',
            fontweight='bold', ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9, edgecolor='#cc3333'))
ax.annotate('TERRACE\n(= deck)', local_to_sjtsk(-1.5, 4.5), fontsize=6, color='#5D4037',
            fontweight='bold', ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#EFEBE9', alpha=0.9, edgecolor='#A0522D'))

swim_label = local_to_sjtsk((POND_U_START+WALL_U)/2, (POND_V_START+POND_V_END)/2)
ax.annotate(f'SWIMMING\n2.0m deep\n{SWIM_AREA:.0f} m\u00b2', swim_label, fontsize=7,
            color='#01579B', fontweight='bold', ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E1F5FE', alpha=0.9, edgecolor='#0277BD'))

regen_label = local_to_sjtsk((WALL_U+POND_U_END)/2, (POND_V_START+POND_V_END)/2)
ax.annotate(f'REGENERATION\n& FILTRATION\n0.1-0.8m deep\n{REGEN_AREA:.0f} m\u00b2', regen_label, fontsize=6,
            color='#1B5E20', fontweight='bold', ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', alpha=0.9, edgecolor='#2E7D32'))

ax.set_aspect('equal')
ax.legend(loc='upper right', fontsize=6, framealpha=0.9)
ax.set_title('Natural Swimming Pond (Schwimmteich) \u2014 Site Plan', fontsize=12, fontweight='bold')
ax.set_xlabel('S-JTSK Y (m)')
ax.set_ylabel('S-JTSK X (m)')
ax.set_xlim(-717402, -717320)
ax.set_ylim(-1059625, -1059572)
ax.grid(True, alpha=0.1)

# --- RIGHT: Cross-section and details ---
ax2 = axes[1]

# Cross-section through the pond (along u-axis at v = center)
section_u = np.array([-2.0, POND_U_START, POND_U_START, POND_U_START-1.2,
                       POND_U_START-1.2, WALL_U+0.15, WALL_U+0.15, WALL_U,
                       WALL_U, WALL_U-0.15, WALL_U-0.15, WALL_U-1.0,
                       WALL_U-1.0, POND_U_END+1.0, POND_U_END+1.0,
                       POND_U_END, POND_U_END, -15.0])
section_z = np.array([397.15, 397.15, 397.05, 396.75,
                       395.15, 395.15, 395.15, 395.15,
                       396.65, 396.65, 396.35, 396.35,
                       396.55, 396.55, 396.85,
                       397.05, 397.05, 396.50])

# Water level
water_level = 397.05
water_u = np.array([POND_U_START, POND_U_END])
water_z = np.array([water_level, water_level])

# Draw section
ax2.fill_between(section_u, section_z, 394.5, color='#8D6E63', alpha=0.3, label='Ground/structure')
ax2.plot(section_u, section_z, color='#5D4037', linewidth=2.0)

# Water
swim_u = [POND_U_START, WALL_U+0.15]
regen_u = [WALL_U-0.15, POND_U_END]
ax2.fill_between([POND_U_START, WALL_U+0.15], water_level, [395.15, 395.15],
                  color='#0288D1', alpha=0.3, label='Swimming water (2.0m)')
ax2.fill_between([WALL_U-0.15, WALL_U-1.0, POND_U_END+1.0, POND_U_END],
                  water_level, [396.35, 396.35, 396.55, 397.05],
                  color='#66BB6A', alpha=0.3, label='Regen zone (0.1-0.8m)')
ax2.axhline(y=water_level, color='#0288D1', linewidth=1.0, linestyle='--', alpha=0.5)

# Gravel fill in regen zone
gravel_u = np.linspace(WALL_U-1.5, POND_U_END+1.5, 20)
for gu in gravel_u:
    ax2.plot(gu, 396.55, '.', color='#A1887F', markersize=2)

# Separation wall
ax2.fill_between([WALL_U+0.15, WALL_U-0.15], 396.65, 395.15,
                  color='#616161', alpha=0.6, label='Separation wall')
# Wall top below water
ax2.plot([WALL_U+0.15, WALL_U-0.15], [396.65, 396.65], color='#424242', linewidth=2)

# Entry steps
for i, (u1, v1, u2, v2, depth) in enumerate(steps):
    step_z = 397.15 + depth  # depth is negative
    ax2.fill_between([u1, u2], 397.15 if i == 0 else 397.15 + steps[i-1][4], step_z,
                      color='#BDBDBD', alpha=0.5)

# Labels
ax2.annotate('TERRACE\n(deck)', (-1.0, 397.35), fontsize=8, ha='center', fontweight='bold',
            color='#5D4037')
ax2.annotate('SWIMMING ZONE\n2.0m deep', ((POND_U_START+WALL_U)/2, 396.0), fontsize=8,
            ha='center', color='#01579B', fontweight='bold')
ax2.annotate('REGENERATION\n& FILTRATION', ((WALL_U+POND_U_END)/2, 396.85), fontsize=7,
            ha='center', color='#1B5E20', fontweight='bold')

ax2.annotate('separation\nwall', (WALL_U, 396.85), fontsize=6, ha='center', color='#424242')
ax2.annotate('steps', (POND_U_START-0.6, 396.6), fontsize=6, ha='center', color='#757575')
ax2.annotate('gravel\nsubstrate', ((WALL_U+POND_U_END)/2, 396.3), fontsize=5,
            ha='center', color='#8D6E63', style='italic')

# Plant symbols in regen zone
plant_positions = [WALL_U-1.5, WALL_U-2.5, WALL_U-3.5, POND_U_END+1.5, POND_U_END+2.0]
for pu in plant_positions:
    ax2.plot(pu, water_level + 0.15, color='#2E7D32', marker=6, markersize=8)
    ax2.plot([pu, pu], [396.55, water_level + 0.05], color='#4CAF50', linewidth=0.8)

# Water flow arrows
ax2.annotate('', xy=(WALL_U+0.3, 395.5), xytext=(WALL_U-0.3, 395.5),
            arrowprops=dict(arrowstyle='->', color='#0288D1', lw=1.5))
ax2.annotate('water flow\nthrough wall', (WALL_U, 395.2), fontsize=5, ha='center', color='#0288D1')

# Elevation labels
ax2.annotate(f'WL {water_level:.2f}m', (POND_U_END+0.2, water_level), fontsize=5,
            color='#0288D1', va='bottom')
ax2.annotate(f'{397.15:.2f}m\n(terrace level)', (-2.0, 397.15), fontsize=5,
            color='#5D4037', va='bottom', ha='right')

# Dimensions
ax2.annotate('', xy=(WALL_U, 394.8), xytext=(POND_U_START, 394.8),
            arrowprops=dict(arrowstyle='<->', color='#333', lw=0.8))
ax2.annotate(f'{SWIM_DEPTH:.1f}m', ((POND_U_START+WALL_U)/2, 394.65), fontsize=6,
            ha='center', color='#333')

ax2.annotate('', xy=(POND_U_END, 394.8), xytext=(WALL_U, 394.8),
            arrowprops=dict(arrowstyle='<->', color='#333', lw=0.8))
ax2.annotate(f'{REGEN_DEPTH:.1f}m', ((WALL_U+POND_U_END)/2, 394.65), fontsize=6,
            ha='center', color='#333')

ax2.set_xlim(-3.0, -15.0)  # reversed so terrace is on left
ax2.set_ylim(394.4, 397.7)
ax2.set_xlabel('Distance from building (m)')
ax2.set_ylabel('Elevation (m Bpv)')
ax2.set_title('Cross-Section A-A\u2032 (through pond center)', fontsize=11, fontweight='bold')
ax2.legend(loc='lower left', fontsize=6, framealpha=0.9)
ax2.grid(True, alpha=0.15)
ax2.invert_xaxis()

plt.tight_layout()
plt.savefig('schwimmteich_plan_v3.png', dpi=200, bbox_inches='tight')
print('Saved schwimmteich_plan.png')

# Print summary
print(f"""
=== SCHWIMMTEICH DESIGN SUMMARY ===

DIMENSIONS
  Overall: {POND_DEPTH:.1f}m x {POND_WIDTH:.1f}m = {POND_AREA:.0f} m2
  Swimming zone: {SWIM_DEPTH:.1f}m x {POND_WIDTH:.1f}m = {SWIM_AREA:.0f} m2 (depth: 1.8-2.0m)
  Regeneration zone: {REGEN_DEPTH:.1f}m x {POND_WIDTH:.1f}m = {REGEN_AREA:.0f} m2
  Ratio swim:regen = {SWIM_AREA/POND_AREA*100:.0f}:{REGEN_AREA/POND_AREA*100:.0f}

SEPARATION WALL
  Reinforced concrete or masonry, top at -0.4m below water surface
  3 water passages (0.5m wide) for circulation

DEPTH ZONES (Regeneration)
  Marginal shelf: 0.1-0.3m (1.0m wide border) - Iris, Caltha, Typha minima
  Mid zone: 0.3-0.5m - Nymphaea, Potamogeton
  Gravel filter bed: 0.5-0.8m center - substrate filtration

CIRCULATION SYSTEM
  Skimmer (SK): surface debris collection, near terrace
  Bottom drain (BD): deep water circulation
  Pump chamber: outside pond, near separation wall
  Inlet (IN): return flow into regeneration zone far end
  Flow: Swim zone -> SK/BD -> Pump -> Regen zone -> through wall -> Swim zone

ENTRY
  3 graduated steps from terrace into swimming zone (0.3m, 0.6m, 0.9m)

TERRACE / DECK
  Existing 38 m2 terrace serves as the pool deck
  Coping stone edge between terrace and pond (0.1m gap)

TERRAIN
  Terrace level: 397.15m Bpv
  Water level: ~397.05m Bpv (0.1m below terrace)
  Swim zone floor: ~395.15m Bpv (1.9m deep)
  Natural terrain slopes ~2m toward SE - pond is partially in-ground

UTILITIES
  Connect overflow to rainwater drainage (D.1.4.1.4)
  Pump power from house electrical (D.1.4.3)
  Keep clear of underground sewer route (D.1.4.1.2)
""")
