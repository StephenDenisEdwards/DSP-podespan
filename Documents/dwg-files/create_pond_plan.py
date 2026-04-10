"""Design natural swimming pond and generate site plan with pond overlay."""
import ezdxf
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.path import Path
import matplotlib.patches as mpatches

# === Transform parameters (64-point fit) ===
a_p = 0.000999628440
b_p = 0.000000223925
tx_p = -717879.783827
ty_p = -1059415.885979

def transform(x, y):
    return (a_p*x - b_p*y + tx_p, b_p*x + a_p*y + ty_p)

# === Building geometry from C.3 ===
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

# === Design the pond ===
# The pond extends from the terrace SE edge toward the garage
# Building axis angle: -140.3 deg
# Perpendicular (toward SE from terrace): -140.3 + 90 = -50.3 deg

axis_angle = math.radians(-140.3)
perp_angle = axis_angle + math.pi/2  # toward SE
along_angle = axis_angle  # along building long axis

# Local coordinate system centered on terrace SE edge midpoint
# u-axis: along building (parallel to terrace edge)
# v-axis: perpendicular, pointing away from building (toward SE)
terrace_mid = (
    (terrace_sj[1][0] + terrace_sj[2][0] + terrace_sj[3][0] + terrace_sj[4][0]) / 4,
    (terrace_sj[1][1] + terrace_sj[2][1] + terrace_sj[3][1] + terrace_sj[4][1]) / 4,
)

cos_a = math.cos(along_angle)
sin_a = math.sin(along_angle)
cos_p = math.cos(perp_angle)
sin_p = math.sin(perp_angle)

def local_to_sjtsk(u, v):
    """Convert from building-local coords (u=along, v=away from building) to S-JTSK."""
    x = terrace_mid[0] + u * cos_a + v * cos_p
    y = terrace_mid[1] + u * sin_a + v * sin_p
    return (x, y)

# Design an organic kidney/bean-shaped pond
# The pond starts 1m from the terrace edge (v=1) and extends to v=11 (11m away)
# It widens from the terrace, then narrows toward the far end
# It curves to avoid the garage and access road

# Create the pond outline using parametric curve
# Split into: swimming zone (deeper, near terrace) and regeneration zone (shallow, planted)
t = np.linspace(0, 2*np.pi, 120)

# Main pond outline - organic bean shape
# In local coords: u = along building axis, v = perpendicular (away from building)
def pond_outline(t):
    """Create organic pond outline in local coords."""
    # Base ellipse stretched toward SE
    u_center = 1.0   # slightly offset along building axis
    v_center = 6.0   # center 6m from terrace edge

    # Asymmetric radii - wider near terrace, narrower toward garage
    r_u_base = 5.5   # half-width along building axis
    r_v_base = 5.0   # half-length perpendicular to building

    # Add organic deformation
    u = u_center + r_u_base * np.cos(t) * (1 + 0.15*np.sin(2*t) + 0.08*np.cos(3*t))
    v = v_center + r_v_base * np.sin(t) * (1 + 0.12*np.cos(2*t) - 0.1*np.sin(t))

    # Flatten the terrace-side edge (v near 1)
    # Pull points closer to terrace where v < 2
    mask = v < 1.5
    v[mask] = 1.5

    # Prevent extending too close to garage (v > 10.5)
    mask2 = v > 10.5
    v[mask2] = 10.5

    return u, v

u_pond, v_pond = pond_outline(t)
pond_sj = [local_to_sjtsk(u, v) for u, v in zip(u_pond, v_pond)]

# Swimming zone - inner area (deeper, near terrace)
def swim_zone(t):
    u_center = 0.5
    v_center = 4.5
    r_u = 3.5
    r_v = 3.0
    u = u_center + r_u * np.cos(t) * (1 + 0.1*np.sin(2*t))
    v = v_center + r_v * np.sin(t) * (1 + 0.08*np.cos(2*t))
    v = np.clip(v, 2.0, 7.5)
    return u, v

u_swim, v_swim = swim_zone(t)
swim_sj = [local_to_sjtsk(u, v) for u, v in zip(u_swim, v_swim)]

# Wooden deck extending from terrace into pond
deck_local = [(-3.0, 0.5), (3.0, 0.5), (3.0, 3.0), (2.0, 3.5), (-2.0, 3.5), (-3.0, 3.0)]
deck_sj = [local_to_sjtsk(u, v) for u, v in deck_local]

# Stepping stones path (from garage side to pond)
stones = [(4.5, 9.5), (4.0, 8.5), (3.3, 7.5), (3.0, 6.5), (3.5, 5.5)]
stones_sj = [local_to_sjtsk(u, v) for u, v in stones]

# Compute pond area
def polygon_area(pts):
    n = len(pts)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += pts[i][0] * pts[j][1]
        area -= pts[j][0] * pts[i][1]
    return abs(area) / 2

pond_area = polygon_area(pond_sj)
swim_area = polygon_area(swim_sj)
print(f"Total pond area: {pond_area:.0f} m2")
print(f"Swimming zone: {swim_area:.0f} m2")
print(f"Regeneration zone: {pond_area - swim_area:.0f} m2")

# === Write DXF ===
doc_sv = ezdxf.readfile('10225.dxf')
msp_sv = doc_sv.modelspace()

doc_sv.layers.add('BUILDING_FOOTPRINT', color=1)
doc_sv.layers.add('BUILDING_TERRACE', color=5)
doc_sv.layers.add('BUILDING_GARAGE', color=3)
doc_sv.layers.add('BUILDING_ACCESS', color=8)
doc_sv.layers.add('BUILDING_LABELS', color=7)
doc_sv.layers.add('POND_OUTLINE', color=4)
doc_sv.layers.add('POND_SWIM_ZONE', color=4)
doc_sv.layers.add('POND_DECK', color=30)
doc_sv.layers.add('POND_STONES', color=42)
doc_sv.layers.add('POND_REGEN_ZONE', color=94)

msp_sv.add_lwpolyline(building_sj, dxfattribs={'layer': 'BUILDING_FOOTPRINT'}, close=True)
msp_sv.add_lwpolyline(terrace_sj, dxfattribs={'layer': 'BUILDING_TERRACE'}, close=True)
msp_sv.add_lwpolyline(garage_sj, dxfattribs={'layer': 'BUILDING_GARAGE'}, close=True)
msp_sv.add_lwpolyline(road1_sj, dxfattribs={'layer': 'BUILDING_ACCESS'}, close=True)
msp_sv.add_lwpolyline(road2_sj, dxfattribs={'layer': 'BUILDING_ACCESS'}, close=True)
msp_sv.add_lwpolyline(pond_sj, dxfattribs={'layer': 'POND_OUTLINE'}, close=True)
msp_sv.add_lwpolyline(swim_sj, dxfattribs={'layer': 'POND_SWIM_ZONE'}, close=True)
msp_sv.add_lwpolyline(deck_sj, dxfattribs={'layer': 'POND_DECK'}, close=True)
for s in stones_sj:
    msp_sv.add_circle(s, radius=0.3, dxfattribs={'layer': 'POND_STONES'})

label_house = transform(494471, -178491)
label_garage = transform(505783, -200993)
msp_sv.add_text('RD EDWARDS', dxfattribs={'layer': 'BUILDING_LABELS', 'height': 1.2, 'insert': label_house})
msp_sv.add_text('GARAZ', dxfattribs={'layer': 'BUILDING_LABELS', 'height': 1.0, 'insert': label_garage})

pond_label = local_to_sjtsk(0.5, 6.0)
msp_sv.add_text('SWIMMING POND', dxfattribs={'layer': 'BUILDING_LABELS', 'height': 0.8, 'insert': pond_label})

doc_sv.saveas('site_plan_with_pond.dxf')
print('Saved site_plan_with_pond.dxf')

# === Generate visualization ===
fig, ax = plt.subplots(1, 1, figsize=(18, 22))

# Survey plan base layers
doc_draw = ezdxf.readfile('10225.dxf')
msp_draw = doc_draw.modelspace()

for e in msp_draw:
    if e.dxftype() == 'LINE' and e.dxf.layer == '1':
        s, en = e.dxf.start, e.dxf.end
        ax.plot([s[0], en[0]], [s[1], en[1]], color='#cccccc', linewidth=0.2)
    elif e.dxftype() == 'LINE' and e.dxf.layer == '4':
        s, en = e.dxf.start, e.dxf.end
        ax.plot([s[0], en[0]], [s[1], en[1]], color='#888888', linewidth=0.6)

for e in msp_draw:
    if e.dxf.layer == '25' and e.dxftype() == 'INSERT':
        p = e.dxf.insert
        ax.plot(p[0], p[1], 'b^', markersize=4, alpha=0.5)
    elif e.dxftype() == 'TEXT' and e.dxf.layer == '18':
        p = e.dxf.insert
        ax.annotate(e.dxf.text, (p[0], p[1]), fontsize=6, color='darkblue',
                   fontweight='bold', ha='center', alpha=0.6)
    elif e.dxftype() == 'TEXT' and e.dxf.layer == '19':
        p = e.dxf.insert
        ax.annotate(e.dxf.text, (p[0], p[1]), fontsize=5, color='purple',
                   fontweight='bold', ha='center', alpha=0.6)
    elif e.dxftype() == 'TEXT' and e.dxf.layer == '23':
        p = e.dxf.insert
        ax.annotate(e.dxf.text.strip(), (p[0], p[1]), fontsize=3, color='#bbbbbb')

def plot_poly(pts, color, lw, label=None, fill=False, alpha=0.25, ls='-', zorder=2):
    xs = [p[0] for p in pts] + [pts[0][0]]
    ys = [p[1] for p in pts] + [pts[0][1]]
    if fill:
        ax.fill(xs, ys, alpha=alpha, color=color, zorder=zorder)
    ax.plot(xs, ys, color=color, linewidth=lw, linestyle=ls, label=label, zorder=zorder+1)

# Building (red)
plot_poly(building_sj, '#cc3333', 2.0, 'Building (180.4 m\u00b2)', fill=True, alpha=0.3, zorder=5)

# Terrace (warm gray)
plot_poly(terrace_sj, '#8B7355', 1.5, 'Terrace (38.2 m\u00b2)', fill=True, alpha=0.35, zorder=4)

# Garage (dark gray)
plot_poly(garage_sj, '#555555', 1.5, 'Garage (18.0 m\u00b2)', fill=True, alpha=0.35, zorder=5)

# Access road (light gray dashed)
plot_poly(road1_sj, '#aaaaaa', 0.6, 'Access road', ls='--', zorder=2)
plot_poly(road2_sj, '#aaaaaa', 0.6, None, ls='--', zorder=2)

# === POND ===
# Regeneration zone (outer pond - green/teal)
pond_xs = [p[0] for p in pond_sj] + [pond_sj[0][0]]
pond_ys = [p[1] for p in pond_sj] + [pond_sj[0][1]]
ax.fill(pond_xs, pond_ys, alpha=0.25, color='#2E8B57', zorder=6)  # sea green
ax.plot(pond_xs, pond_ys, color='#1B5E20', linewidth=1.5, zorder=7,
        label=f'Regeneration zone ({pond_area - swim_area:.0f} m\u00b2)')

# Swimming zone (inner - blue/teal)
swim_xs = [p[0] for p in swim_sj] + [swim_sj[0][0]]
swim_ys = [p[1] for p in swim_sj] + [swim_sj[0][1]]
ax.fill(swim_xs, swim_ys, alpha=0.35, color='#00838F', zorder=8)
ax.plot(swim_xs, swim_ys, color='#004D40', linewidth=1.2, zorder=9,
        label=f'Swimming zone ({swim_area:.0f} m\u00b2)')

# Wooden deck (brown)
deck_xs = [p[0] for p in deck_sj] + [deck_sj[0][0]]
deck_ys = [p[1] for p in deck_sj] + [deck_sj[0][1]]
ax.fill(deck_xs, deck_ys, alpha=0.5, color='#8B6914', zorder=10)
ax.plot(deck_xs, deck_ys, color='#5D4037', linewidth=1.0, zorder=11, label='Wooden deck')

# Stepping stones
for s in stones_sj:
    circle = plt.Circle(s, 0.3, color='#9E9E9E', alpha=0.7, zorder=10)
    ax.add_patch(circle)
ax.plot([], [], 'o', color='#9E9E9E', markersize=5, label='Stepping stones')

# Plant markers around regeneration zone (small green dots)
regen_plants = []
for i in range(0, len(pond_sj), 4):
    # Place plants at outer edge
    px, py = pond_sj[i]
    # Slight inward offset
    cx_pond = sum(p[0] for p in pond_sj) / len(pond_sj)
    cy_pond = sum(p[1] for p in pond_sj) / len(pond_sj)
    dx = cx_pond - px
    dy = cy_pond - py
    d = math.sqrt(dx*dx + dy*dy)
    if d > 0:
        px2 = px + dx/d * 0.8
        py2 = py + dy/d * 0.8
        ax.plot(px2, py2, '*', color='#2E7D32', markersize=4, alpha=0.6, zorder=10)

# Labels
ax.annotate('RD EDWARDS\n180.38 m\u00b2', label_house, fontsize=9, color='darkred',
            fontweight='bold', ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9, edgecolor='#cc3333'))
ax.annotate('GAR\u00c1\u017d\n18 m\u00b2', label_garage, fontsize=7, color='#333333',
            fontweight='bold', ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.9, edgecolor='#555555'))
ax.annotate('TERASA', transform(501000, -183500), fontsize=6, color='#5D4037',
            fontweight='bold', ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8, edgecolor='#8B7355'))

# Pond labels
ax.annotate(f'SWIMMING\nPOND\n{pond_area:.0f} m\u00b2', pond_label, fontsize=8,
            color='#004D40', fontweight='bold', ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E0F2F1', alpha=0.9, edgecolor='#00695C'))

swim_label = local_to_sjtsk(0.0, 4.0)
ax.annotate(f'swim\n{swim_area:.0f} m\u00b2', swim_label, fontsize=6,
            color='#00695C', ha='center', va='center', zorder=20)

deck_label = local_to_sjtsk(0.0, 2.0)
ax.annotate('deck', deck_label, fontsize=5, color='#5D4037',
            ha='center', va='center', zorder=20)

# Dimension annotations
# Pond length
p1 = local_to_sjtsk(6.0, 1.5)
p2 = local_to_sjtsk(6.0, 10.5)
ax.annotate('', xy=p2, xytext=p1,
            arrowprops=dict(arrowstyle='<->', color='#00695C', lw=1.0), zorder=15)
mid_dim = local_to_sjtsk(7.0, 6.0)
ax.annotate('~9m', mid_dim, fontsize=7, color='#00695C', ha='center', zorder=15)

# Pond width
p3 = local_to_sjtsk(-5.0, 5.0)
p4 = local_to_sjtsk(6.5, 5.0)
ax.annotate('', xy=p4, xytext=p3,
            arrowprops=dict(arrowstyle='<->', color='#00695C', lw=1.0), zorder=15)
mid_dim2 = local_to_sjtsk(0.5, 4.2)
ax.annotate('~11m', mid_dim2, fontsize=7, color='#00695C', ha='center', zorder=15)

# Clearance to garage
gc_label = local_to_sjtsk(2.0, 11.5)
ax.annotate('~3m to garage', gc_label, fontsize=5, color='gray', ha='center', zorder=15)

# North arrow
arrow_x = -717325
arrow_y = -1059590
ax.annotate('N', xy=(arrow_x, arrow_y + 5), fontsize=10, fontweight='bold',
            ha='center', va='bottom', color='black', zorder=20)
ax.annotate('', xy=(arrow_x, arrow_y + 5), xytext=(arrow_x, arrow_y),
            arrowprops=dict(arrowstyle='->', color='black', lw=2), zorder=20)

# Terrain elevation note
note_pos = (-717325, -1059620)
ax.annotate(
    'Terrain: 397.2m (terrace)\n'
    'to 395.0m (garage area)\n'
    'Natural 2m slope \u2192 SE\n'
    'Pond partially in-ground',
    note_pos, fontsize=6, color='#666666', ha='center', va='top', zorder=20,
    bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFFDE7', alpha=0.9, edgecolor='#999999'))

ax.set_aspect('equal')
ax.legend(loc='upper right', fontsize=7, framealpha=0.9, ncol=1)
ax.set_title(
    'Site Plan with Natural Swimming Pond Design\n'
    f'Total pond: {pond_area:.0f} m\u00b2 | Swimming: {swim_area:.0f} m\u00b2 | '
    f'Regeneration: {pond_area - swim_area:.0f} m\u00b2',
    fontsize=12, fontweight='bold'
)
ax.set_xlabel('S-JTSK Y (m)')
ax.set_ylabel('S-JTSK X (m)')

# Zoom to area of interest
ax.set_xlim(-717405, -717315)
ax.set_ylim(-1059630, -1059570)
ax.grid(True, alpha=0.1)

plt.tight_layout()
plt.savefig('site_plan_with_pond.png', dpi=200, bbox_inches='tight')
print('Saved site_plan_with_pond.png')
