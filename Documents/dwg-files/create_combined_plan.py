"""Create combined site plan with correct building footprint overlay."""
import ezdxf
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Transform parameters (64-point fit, 1:1000 scale)
a_p = 0.000999628440
b_p = 0.000000223925
tx_p = -717879.783827
ty_p = -1059415.885979

def transform(x, y):
    return (a_p*x - b_p*y + tx_p, b_p*x + a_p*y + ty_p)

# === Building geometry from C.3 ===

# BUILDING FOOTPRINT (180.38 m2) - the actual house
building_c3 = [
    (487302.099, -178539.936),
    (492749.529, -185090.959),
    (493380.027, -184566.676),
    (499362.064, -179592.380),
    (504924.580, -186281.805),
    (507538.839, -184107.947),
    (509707.135, -182304.925),
    (498697.189, -169064.477),
]

# TERRACE (38.18 m2)
terrace_c3 = [
    (499413.877, -179029.071),
    (493130.206, -184254.187),
    (495298.136, -186873.375),
    (500511.274, -182538.448),
    (504155.681, -186921.174),
    (507538.839, -184107.947),
    (507027.343, -183492.827),
    (504720.646, -185410.936),
]

# GARAGE (18 m2)
garage_c3 = [
    (503145.036, -197931.664),
    (505310.915, -195855.859),
    (509462.525, -200187.618),
    (507296.646, -202263.423),
]

# DJ structure
dj_c3 = [
    (515189.705, -190782.573),
    (513698.269, -192115.096),
    (512032.615, -190250.800),
    (513524.052, -188918.277),
]

# Access road
access_road_c3 = [
    (498131.446, -166819.679),
    (498362.116, -166627.868),
    (507829.733, -178013.528),
    (507599.063, -178205.339),
]
access_road2_c3 = [
    (507829.733, -178013.528),
    (507599.063, -178205.339),
    (513353.390, -185125.434),
    (513584.060, -184933.623),
]

# Transform all to S-JTSK
building_sj = [transform(*p) for p in building_c3]
terrace_sj = [transform(*p) for p in terrace_c3]
garage_sj = [transform(*p) for p in garage_c3]
dj_sj = [transform(*p) for p in dj_c3]
road1_sj = [transform(*p) for p in access_road_c3]
road2_sj = [transform(*p) for p in access_road2_c3]

# Compute building dimensions along principal axis
edge_angle = math.atan2(
    building_c3[0][1] - building_c3[7][1],
    building_c3[0][0] - building_c3[7][0]
)
cos_a = math.cos(edge_angle)
sin_a = math.sin(edge_angle)

proj_along = [x*cos_a + y*sin_a for x, y in building_c3]
proj_perp = [-x*sin_a + y*cos_a for x, y in building_c3]
dim_along = (max(proj_along) - min(proj_along)) / 1000
dim_perp = (max(proj_perp) - min(proj_perp)) / 1000
print(f"Building axis angle: {math.degrees(edge_angle):.1f} deg")
print(f"Building dimensions along axis: {dim_along:.1f}m x {dim_perp:.1f}m")

# === Write combined DXF ===
doc_sv = ezdxf.readfile('10225.dxf')
msp_sv = doc_sv.modelspace()

doc_sv.layers.add('BUILDING_FOOTPRINT', color=1)
doc_sv.layers.add('BUILDING_TERRACE', color=5)
doc_sv.layers.add('BUILDING_GARAGE', color=3)
doc_sv.layers.add('BUILDING_DJ', color=4)
doc_sv.layers.add('BUILDING_ACCESS', color=8)
doc_sv.layers.add('BUILDING_LABELS', color=7)

msp_sv.add_lwpolyline(building_sj, dxfattribs={'layer': 'BUILDING_FOOTPRINT'}, close=True)
msp_sv.add_lwpolyline(terrace_sj, dxfattribs={'layer': 'BUILDING_TERRACE'}, close=True)
msp_sv.add_lwpolyline(garage_sj, dxfattribs={'layer': 'BUILDING_GARAGE'}, close=True)
msp_sv.add_lwpolyline(dj_sj, dxfattribs={'layer': 'BUILDING_DJ'}, close=True)
msp_sv.add_lwpolyline(road1_sj, dxfattribs={'layer': 'BUILDING_ACCESS'}, close=True)
msp_sv.add_lwpolyline(road2_sj, dxfattribs={'layer': 'BUILDING_ACCESS'}, close=True)

label_house = transform(494471, -178491)
label_garage = transform(505783, -200993)
msp_sv.add_text('RD EDWARDS', dxfattribs={'layer': 'BUILDING_LABELS', 'height': 1.2, 'insert': label_house})
msp_sv.add_text('GARAZ', dxfattribs={'layer': 'BUILDING_LABELS', 'height': 1.0, 'insert': label_garage})

doc_sv.saveas('combined_site_plan.dxf')
print('Saved combined_site_plan.dxf')

# === Generate visualization ===
fig, ax = plt.subplots(1, 1, figsize=(16, 20))

# Read fresh copy for drawing
doc_draw = ezdxf.readfile('10225.dxf')
msp_draw = doc_draw.modelspace()

# Survey plan layers
for e in msp_draw:
    if e.dxftype() == 'LINE' and e.dxf.layer == '1':
        s, en = e.dxf.start, e.dxf.end
        ax.plot([s[0], en[0]], [s[1], en[1]], color='#999999', linewidth=0.3)
    elif e.dxftype() == 'LINE' and e.dxf.layer == '4':
        s, en = e.dxf.start, e.dxf.end
        ax.plot([s[0], en[0]], [s[1], en[1]], color='#555555', linewidth=0.8)

# Boundary markers
for e in msp_draw:
    if e.dxf.layer == '25' and e.dxftype() == 'INSERT':
        p = e.dxf.insert
        ax.plot(p[0], p[1], 'b^', markersize=5)

# Parcel labels
for e in msp_draw:
    if e.dxftype() == 'TEXT':
        p = e.dxf.insert
        if e.dxf.layer == '18':
            ax.annotate(e.dxf.text, (p[0], p[1]), fontsize=7, color='darkblue',
                       fontweight='bold', ha='center')
        elif e.dxf.layer == '19':
            ax.annotate(e.dxf.text, (p[0], p[1]), fontsize=6, color='purple',
                       fontweight='bold', ha='center')
        elif e.dxf.layer == '23':
            ax.annotate(e.dxf.text.strip(), (p[0], p[1]), fontsize=3.5, color='#aaaaaa')

# Survey point markers
for e in msp_draw:
    if e.dxf.layer == '23' and e.dxftype() == 'INSERT':
        p = e.dxf.insert
        ax.plot(p[0], p[1], '.', color='#777777', markersize=1.5)

def plot_poly(pts, color, lw, label, fill=False, alpha=0.25, ls='-'):
    xs = [p[0] for p in pts] + [pts[0][0]]
    ys = [p[1] for p in pts] + [pts[0][1]]
    if fill:
        ax.fill(xs, ys, alpha=alpha, color=color)
    ax.plot(xs, ys, color=color, linewidth=lw, linestyle=ls, label=label)

# Building footprint (red)
plot_poly(building_sj, 'red', 2.5, f'Building footprint (180.4 m\u00b2)', fill=True, alpha=0.25)

# Terrace (blue)
plot_poly(terrace_sj, 'dodgerblue', 1.5, f'Terrace (38.2 m\u00b2)', fill=True, alpha=0.2)

# Garage (green)
plot_poly(garage_sj, 'green', 2.0, f'Garage (18.0 m\u00b2)', fill=True, alpha=0.25)

# DJ structure
plot_poly(dj_sj, 'cyan', 1.5, 'DJ (drainage)')

# Access road
plot_poly(road1_sj, 'gray', 0.8, 'Access road', ls='--')
plot_poly(road2_sj, 'gray', 0.8, None, ls='--')

# Labels
ax.annotate(f'RD EDWARDS\n180.38 m\u00b2', label_house, fontsize=9, color='darkred',
            fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.85, edgecolor='red'))
ax.annotate(f'GAR\u00c1\u017d\n18.00 m\u00b2', label_garage, fontsize=7, color='darkgreen',
            fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.85, edgecolor='green'))
ax.annotate(f'TERASA\n38.19 m\u00b2', transform(501000, -183500), fontsize=6, color='blue',
            fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8, edgecolor='dodgerblue'))

ax.set_aspect('equal')
ax.legend(loc='upper right', fontsize=8, framealpha=0.9)
ax.set_title(
    f'Combined Site Plan: Survey + Building (C.3 Koordina\u010dn\u00ed situace)\n'
    f'Transform: 64-point fit, 1:1000 scale, ~2cm accuracy | '
    f'Building: {dim_along:.1f}m x {dim_perp:.1f}m',
    fontsize=11
)
ax.set_xlabel('S-JTSK Y (m)')
ax.set_ylabel('S-JTSK X (m)')
ax.grid(True, alpha=0.15)

plt.tight_layout()
plt.savefig('combined_site_plan.png', dpi=200, bbox_inches='tight')
print('Saved combined_site_plan.png')
