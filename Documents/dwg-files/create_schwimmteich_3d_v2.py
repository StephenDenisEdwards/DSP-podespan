"""
3D Isometric cutaway view of the Schwimmteich (natural swimming pond).
Version 2 -- Banded Zones (parallel depth bands instead of concentric rings).

Shows:
- Swimming zone (2.0m deep) and regeneration zone with 3 parallel depth bands
- Separation wall with water passages
- Gravel substrate layers in Zone 3 (deepest band, next to wall)
- Pump, piping, skimmer, and bottom drain under the gravel
- Entry steps from terrace
- Planting in regeneration zone
- Water level and flow direction

Zone layout (from wall outward):
  Zone 3 (deepest, gravel bed, 60-100cm) -- y = WALL_Y to WALL_Y + 2.35m
  Zone 2 (shallow, 30-60cm)             -- y = WALL_Y + 2.35 to WALL_Y + 3.45m
  Zone 1 (marginal, 0-30cm, shallowest) -- y = WALL_Y + 3.45 to POND_L (= WALL_Y + 5.0)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patches as mpatches

# =============================================================
# POND DIMENSIONS (from schwimmteich_plan_v3)
# =============================================================

POND_W = 7.5
POND_L = 10.0
SWIM_L = 5.0
REGEN_L = 5.0
WALL_Y = 5.0

TERRACE_Z = 0.0
WATER_Z = -0.10
SWIM_FLOOR_Z = -2.00
WALL_TOP_Z = -0.40
WALL_BASE_Z = -2.00
REGEN_FLOOR_Z = -1.00
GRAVEL_TOP_Z = -0.60
GRAVEL_BOT_Z = -1.00
SHELF_Z = -0.40
PIPE_Z = -1.10
WALL_T = 0.30
STEP_W = 3.0
STEP_D = 0.4
STEP_DEPTHS = [-0.30, -0.60, -0.90]

Z_SCALE = 1.5

def iso_project(x, y, z, angle=35, rotation=45):
    # Rotate model 90° so deck is at back-right, regen at front-left
    x, y = 10.0 - y, 7.5 - x
    rot = np.radians(rotation)
    ang = np.radians(angle)
    z_scaled = z * Z_SCALE
    x2d = x * np.cos(rot) - y * np.sin(rot)
    y2d = (x * np.sin(rot) + y * np.cos(rot)) * np.sin(ang) + z_scaled * np.cos(ang)
    return x2d, y2d

def draw_face(ax, vertices, color, alpha=0.7, edgecolor='#333', lw=0.5, zorder=2):
    pts_2d = [iso_project(*v) for v in vertices]
    xs = [p[0] for p in pts_2d]
    ys = [p[1] for p in pts_2d]
    ax.fill(xs, ys, color=color, alpha=alpha, edgecolor=edgecolor, linewidth=lw, zorder=zorder)

def draw_box(ax, x0, y0, z0, dx, dy, dz, top_color, side_color, front_color,
             alpha=0.7, lw=0.5, draw_top=True, draw_front=True, draw_right=True, zorder=2):
    if draw_top:
        top = [(x0, y0, z0+dz), (x0+dx, y0, z0+dz),
               (x0+dx, y0+dy, z0+dz), (x0, y0+dy, z0+dz)]
        draw_face(ax, top, top_color, alpha, zorder=zorder+1)
    if draw_front:
        front = [(x0, y0+dy, z0), (x0+dx, y0+dy, z0),
                 (x0+dx, y0+dy, z0+dz), (x0, y0+dy, z0+dz)]
        draw_face(ax, front, front_color, alpha, zorder=zorder)
    if draw_right:
        right = [(x0+dx, y0, z0), (x0+dx, y0+dy, z0),
                 (x0+dx, y0+dy, z0+dz), (x0+dx, y0, z0+dz)]
        draw_face(ax, right, side_color, alpha, zorder=zorder)

def draw_line_3d(ax, p1, p2, color='#333', lw=1.0, ls='-', zorder=5, alpha=1.0):
    x1, y1 = iso_project(*p1)
    x2, y2 = iso_project(*p2)
    ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw, linestyle=ls, zorder=zorder, alpha=alpha)

# =============================================================
# MAIN FIGURE
# =============================================================
fig, ax = plt.subplots(1, 1, figsize=(20, 14))
ax.set_aspect('equal')
ax.axis('off')

# 1. GROUND
ground_margin = 1.5
draw_box(ax, -ground_margin, -ground_margin, -2.5,
         POND_W + 2*ground_margin, POND_L + 2*ground_margin, 0.4,
         '#8B7355', '#6B5335', '#7B6345', alpha=0.3, zorder=0,
         draw_front=True, draw_right=True)

# 2. POND SHELL
SHELL_T = 0.15
draw_face(ax,
    [(0, 0, SWIM_FLOOR_Z), (POND_W, 0, SWIM_FLOOR_Z),
     (POND_W, WALL_Y, SWIM_FLOOR_Z), (0, WALL_Y, SWIM_FLOOR_Z)],
    '#B0BEC5', alpha=0.5, zorder=1)

# BANDED DEPTH PROFILE (V2)
Z1_Z = -0.15
Z2_Z = -0.45
Z3_LENGTH = 2.35
Z2_LENGTH = 1.10
Z1_LENGTH = 1.55

z1_color = '#43A047'
z2_color = '#FDD835'
z3_color = '#E65100'

z3_y0 = WALL_Y
z3_y1 = WALL_Y + Z3_LENGTH
z2_y0 = z3_y1
z2_y1 = z3_y1 + Z2_LENGTH
z1_y0 = z2_y1
z1_y1 = POND_L

# Zone 3: Deep gravel bed
draw_face(ax,
    [(0, z3_y0, GRAVEL_BOT_Z), (POND_W, z3_y0, GRAVEL_BOT_Z),
     (POND_W, z3_y1, GRAVEL_BOT_Z), (0, z3_y1, GRAVEL_BOT_Z)],
    z3_color, alpha=0.5, edgecolor='#8D3200', lw=1.5, zorder=5)

# Zone 2: Shallow
draw_face(ax,
    [(0, z2_y0, Z2_Z), (POND_W, z2_y0, Z2_Z),
     (POND_W, z2_y1, Z2_Z), (0, z2_y1, Z2_Z)],
    z2_color, alpha=0.65, edgecolor='#F9A825', lw=1.5, zorder=4.5)

# Zone 1: Marginal
draw_face(ax,
    [(0, z1_y0, Z1_Z), (POND_W, z1_y0, Z1_Z),
     (POND_W, z1_y1, Z1_Z), (0, z1_y1, Z1_Z)],
    z1_color, alpha=0.65, edgecolor='#2E7D32', lw=1.5, zorder=4)

# Step Z3->Z2 front face
draw_face(ax,
    [(0, z3_y1, GRAVEL_BOT_Z), (POND_W, z3_y1, GRAVEL_BOT_Z),
     (POND_W, z3_y1, Z2_Z), (0, z3_y1, Z2_Z)],
    '#BF360C', alpha=0.75, edgecolor='#8D3200', lw=2.0, zorder=5)

# Step Z2->Z1 front face
draw_face(ax,
    [(0, z2_y1, Z2_Z), (POND_W, z2_y1, Z2_Z),
     (POND_W, z2_y1, Z1_Z), (0, z2_y1, Z1_Z)],
    '#33691E', alpha=0.75, edgecolor='#1B5E20', lw=2.0, zorder=4.5)

# Right-side step-down faces
draw_face(ax,
    [(POND_W, z3_y0, GRAVEL_BOT_Z), (POND_W, z3_y1, GRAVEL_BOT_Z),
     (POND_W, z3_y1, Z2_Z), (POND_W, z3_y0, Z2_Z)],
    '#BF360C', alpha=0.55, edgecolor='#8D3200', lw=1.0, zorder=5)
draw_face(ax,
    [(POND_W, z2_y0, Z2_Z), (POND_W, z2_y1, Z2_Z),
     (POND_W, z2_y1, Z1_Z), (POND_W, z2_y0, Z1_Z)],
    '#33691E', alpha=0.55, edgecolor='#1B5E20', lw=1.0, zorder=4.5)

# Gravel fill variables
s2_inner_x0 = 0
s2_inner_x1 = POND_W
s2_inner_y0 = z3_y0
s2_inner_y1 = z3_y1

# Pond walls
draw_face(ax,
    [(POND_W, 0, SWIM_FLOOR_Z), (POND_W, WALL_Y, SWIM_FLOOR_Z),
     (POND_W, WALL_Y, TERRACE_Z), (POND_W, 0, TERRACE_Z)],
    '#90A4AE', alpha=0.5, zorder=3)
draw_face(ax,
    [(POND_W, WALL_Y, Z1_Z), (POND_W, POND_L, Z1_Z),
     (POND_W, POND_L, TERRACE_Z), (POND_W, WALL_Y, TERRACE_Z)],
    '#90A4AE', alpha=0.5, zorder=3)
draw_face(ax,
    [(0, POND_L, Z1_Z), (POND_W, POND_L, Z1_Z),
     (POND_W, POND_L, TERRACE_Z), (0, POND_L, TERRACE_Z)],
    '#78909C', alpha=0.5, zorder=3)

# Left wall cross-section
draw_face(ax,
    [(0, 0, SWIM_FLOOR_Z), (0, WALL_Y, SWIM_FLOOR_Z),
     (0, WALL_Y, TERRACE_Z), (0, 0, TERRACE_Z)],
    '#78909C', alpha=0.4, lw=0.8, zorder=3)
draw_face(ax,
    [(0, WALL_Y, Z1_Z), (0, POND_L, Z1_Z),
     (0, POND_L, TERRACE_Z), (0, WALL_Y, TERRACE_Z)],
    '#78909C', alpha=0.4, lw=0.8, zorder=3)
draw_face(ax,
    [(0, z3_y0, GRAVEL_BOT_Z), (0, z3_y1, GRAVEL_BOT_Z),
     (0, z3_y1, Z2_Z), (0, z3_y0, Z2_Z)],
    '#BF360C', alpha=0.6, lw=1.5, zorder=4.5)
draw_face(ax,
    [(0, z2_y0, Z2_Z), (0, z2_y1, Z2_Z),
     (0, z2_y1, Z1_Z), (0, z2_y0, Z1_Z)],
    '#F9A825', alpha=0.6, lw=1.5, zorder=4)

# Back wall
draw_face(ax,
    [(0, 0, SWIM_FLOOR_Z), (POND_W, 0, SWIM_FLOOR_Z),
     (POND_W, 0, TERRACE_Z), (0, 0, TERRACE_Z)],
    '#B0BEC5', alpha=0.3, zorder=1)

# Zone areas
z3_area = Z3_LENGTH * POND_W
z2_area = Z2_LENGTH * POND_W
z1_area = Z1_LENGTH * POND_W
regen_total = REGEN_L * POND_W

# Depth labels
z3_anchor = iso_project(POND_W - 0.5, (z3_y0 + z3_y1)/2, GRAVEL_BOT_Z + 0.2)
z3_label = iso_project(POND_W + 2.5, WALL_Y + 0.5, GRAVEL_BOT_Z)
ax.annotate('ZONE 3: DEEP GRAVEL BED\n60-100cm deep  |  %.1f m2 (%d%%)\nNymphaea, hornwort, oxygenators\n3 gravel layers, 4-5 plants/m2' % (z3_area, z3_area/regen_total*100),
            xy=z3_anchor, xytext=z3_label, fontsize=7, fontweight='bold',
            color='#BF360C', ha='left', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FBE9E7', edgecolor='#E65100', alpha=0.95, linewidth=2),
            arrowprops=dict(arrowstyle='->', color='#E65100', lw=1.5))

z2_anchor = iso_project(POND_W - 0.3, (z2_y0 + z2_y1)/2, Z2_Z)
z2_label = iso_project(POND_W + 2.5, WALL_Y + 2.5, Z2_Z + 0.1)
ax.annotate('ZONE 2: SHALLOW\n30-60cm deep  |  %.1f m2 (%d%%)\nIris, Acorus, Mentha aquatica' % (z2_area, z2_area/regen_total*100),
            xy=z2_anchor, xytext=z2_label, fontsize=7, fontweight='bold',
            color='#F57F17', ha='left', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF9C4', edgecolor='#F9A825', alpha=0.95, linewidth=2),
            arrowprops=dict(arrowstyle='->', color='#F9A825', lw=1.5))

z1_anchor = iso_project(POND_W - 0.3, (z1_y0 + z1_y1)/2, Z1_Z)
z1_label = iso_project(POND_W + 2.5, WALL_Y + 4.5, Z1_Z + 0.3)
ax.annotate('ZONE 1: MARGINAL\n0-30cm deep  |  %.1f m2 (%d%%)\nCaltha, Juncus, Myosotis' % (z1_area, z1_area/regen_total*100),
            xy=z1_anchor, xytext=z1_label, fontsize=7, fontweight='bold',
            color='#1B5E20', ha='left', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#C8E6C9', edgecolor='#2E7D32', alpha=0.95, linewidth=2),
            arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=1.5))

# Vertical depth dimensions
dd_top = iso_project(-0.6, POND_L, TERRACE_Z)
dd_z1 = iso_project(-0.6, POND_L, Z1_Z)
dd_z2 = iso_project(-0.6, POND_L, Z2_Z)
dd_z3 = iso_project(-0.6, POND_L, GRAVEL_BOT_Z)
ax.annotate('', xy=dd_z1, xytext=dd_top, arrowprops=dict(arrowstyle='<->', color='#2E7D32', lw=1.2), zorder=20)
dm1 = iso_project(-1.3, POND_L, (TERRACE_Z + Z1_Z)/2)
ax.annotate('0.15m', dm1, fontsize=6, fontweight='bold', color='#2E7D32', ha='right', va='center', zorder=20,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))
ax.annotate('', xy=dd_z2, xytext=dd_z1, arrowprops=dict(arrowstyle='<->', color='#F9A825', lw=1.2), zorder=20)
dm2 = iso_project(-1.3, POND_L, (Z1_Z + Z2_Z)/2)
ax.annotate('0.30m', dm2, fontsize=6, fontweight='bold', color='#F57F17', ha='right', va='center', zorder=20,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))
ax.annotate('', xy=dd_z3, xytext=dd_z2, arrowprops=dict(arrowstyle='<->', color='#BF360C', lw=1.2), zorder=20)
dm3 = iso_project(-1.3, POND_L, (Z2_Z + GRAVEL_BOT_Z)/2)
ax.annotate('0.55m', dm3, fontsize=6, fontweight='bold', color='#BF360C', ha='right', va='center', zorder=20,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

# 3. SEPARATION WALL
wall_color_top = '#616161'
wall_color_front = '#757575'
wall_color_side = '#555555'
passage_positions = [(1.5, 2.0), (3.5, 4.0), (5.5, 6.0)]
wall_segments_x = [0]
for p_start, p_end in passage_positions:
    wall_segments_x.extend([p_start, p_end])
wall_segments_x.append(POND_W)

for i in range(0, len(wall_segments_x), 2):
    x_start = wall_segments_x[i]
    x_end = wall_segments_x[i+1]
    seg_w = x_end - x_start
    if seg_w > 0.01:
        draw_box(ax, x_start, WALL_Y - WALL_T/2, WALL_BASE_Z,
                 seg_w, WALL_T, WALL_TOP_Z - WALL_BASE_Z,
                 wall_color_top, wall_color_side, wall_color_front, alpha=0.85, zorder=8)

for p_start, p_end in passage_positions:
    draw_face(ax,
        [(p_start, WALL_Y - WALL_T/2, WALL_BASE_Z), (p_end, WALL_Y - WALL_T/2, WALL_BASE_Z),
         (p_end, WALL_Y - WALL_T/2, WALL_TOP_Z), (p_start, WALL_Y - WALL_T/2, WALL_TOP_Z)],
        '#29B6F6', alpha=0.4, edgecolor='#0288D1', lw=1.0, zorder=9)
    mid_x = (p_start + p_end) / 2
    mid_z = (WALL_BASE_Z + WALL_TOP_Z) / 2
    p1 = iso_project(mid_x, WALL_Y + 0.5, mid_z)
    p2 = iso_project(mid_x, WALL_Y - 0.5, mid_z)
    ax.annotate('', xy=p2, xytext=p1, arrowprops=dict(arrowstyle='->', color='#0288D1', lw=1.5), zorder=15)

# 4. GRAVEL FILL in Zone 3 band
gravel_fill_z0 = GRAVEL_BOT_Z
gravel_fill_z1 = GRAVEL_BOT_Z + 0.10
gravel_fill_z2 = GRAVEL_BOT_Z + 0.20
gravel_fill_z3 = GRAVEL_TOP_Z

draw_face(ax,
    [(s2_inner_x0, s2_inner_y0, gravel_fill_z1), (s2_inner_x1, s2_inner_y0, gravel_fill_z1),
     (s2_inner_x1, s2_inner_y1, gravel_fill_z1), (s2_inner_x0, s2_inner_y1, gravel_fill_z1)],
    '#6D4C41', alpha=0.45, edgecolor='#5D4037', lw=0.5, zorder=5.1)
draw_face(ax,
    [(s2_inner_x0, s2_inner_y0, gravel_fill_z2), (s2_inner_x1, s2_inner_y0, gravel_fill_z2),
     (s2_inner_x1, s2_inner_y1, gravel_fill_z2), (s2_inner_x0, s2_inner_y1, gravel_fill_z2)],
    '#8D6E63', alpha=0.45, edgecolor='#6D4C41', lw=0.5, zorder=5.2)
draw_face(ax,
    [(s2_inner_x0, s2_inner_y0, gravel_fill_z3), (s2_inner_x1, s2_inner_y0, gravel_fill_z3),
     (s2_inner_x1, s2_inner_y1, gravel_fill_z3), (s2_inner_x0, s2_inner_y1, gravel_fill_z3)],
    '#BCAAA4', alpha=0.55, edgecolor='#A1887F', lw=0.5, zorder=5.3)

# Gravel front face cross-section
draw_face(ax,
    [(s2_inner_x0, s2_inner_y1, gravel_fill_z0), (s2_inner_x1, s2_inner_y1, gravel_fill_z0),
     (s2_inner_x1, s2_inner_y1, gravel_fill_z1), (s2_inner_x0, s2_inner_y1, gravel_fill_z1)],
    '#5D4037', alpha=0.65, edgecolor='#4E342E', lw=0.5, zorder=5.5)
draw_face(ax,
    [(s2_inner_x0, s2_inner_y1, gravel_fill_z1), (s2_inner_x1, s2_inner_y1, gravel_fill_z1),
     (s2_inner_x1, s2_inner_y1, gravel_fill_z2), (s2_inner_x0, s2_inner_y1, gravel_fill_z2)],
    '#795548', alpha=0.6, edgecolor='#5D4037', lw=0.5, zorder=5.5)
draw_face(ax,
    [(s2_inner_x0, s2_inner_y1, gravel_fill_z2), (s2_inner_x1, s2_inner_y1, gravel_fill_z2),
     (s2_inner_x1, s2_inner_y1, gravel_fill_z3), (s2_inner_x0, s2_inner_y1, gravel_fill_z3)],
    '#A1887F', alpha=0.55, edgecolor='#8D6E63', lw=0.5, zorder=5.5)

# Gravel right face
draw_face(ax,
    [(s2_inner_x1, s2_inner_y0, gravel_fill_z0), (s2_inner_x1, s2_inner_y1, gravel_fill_z0),
     (s2_inner_x1, s2_inner_y1, gravel_fill_z3), (s2_inner_x1, s2_inner_y0, gravel_fill_z3)],
    '#795548', alpha=0.5, edgecolor='#5D4037', lw=0.5, zorder=5.5)

# Gravel texture dots
np.random.seed(42)
for _ in range(60):
    gx = np.random.uniform(s2_inner_x0 + 0.2, s2_inner_x1 - 0.2)
    gy = np.random.uniform(s2_inner_y0 + 0.2, s2_inner_y1 - 0.2)
    gpx, gpy = iso_project(gx, gy, gravel_fill_z3 + 0.01)
    ax.plot(gpx, gpy, '.', color='#6D4C41', markersize=np.random.uniform(1.5, 3.5), zorder=6, alpha=0.6)

for label, z_mid, col in [
    ('coarse\n16-32mm', (gravel_fill_z0 + gravel_fill_z1)/2, '#5D4037'),
    ('medium\n8-16mm', (gravel_fill_z1 + gravel_fill_z2)/2, '#795548'),
    ('fine\n2-8mm', (gravel_fill_z2 + gravel_fill_z3)/2, '#A1887F'),
]:
    lx, ly = iso_project(s2_inner_x1 + 0.3, (s2_inner_y0 + s2_inner_y1)/2, z_mid)
    ax.annotate(label, (lx, ly), fontsize=5, color=col, ha='left', va='center', zorder=20,
                fontweight='bold', fontstyle='italic')

# 6. PIPING UNDER GRAVEL
pipe_color = '#E65100'
manifold_y = (z3_y0 + z3_y1) / 2
draw_line_3d(ax, (0.8, manifold_y, PIPE_Z), (POND_W - 0.8, manifold_y, PIPE_Z), color=pipe_color, lw=2.5, zorder=7)

for bx in np.linspace(1.2, POND_W - 1.2, 5):
    draw_line_3d(ax, (bx, manifold_y, PIPE_Z), (bx, WALL_Y + 0.5, PIPE_Z), color=pipe_color, lw=1.5, ls='--', zorder=7, alpha=0.7)
    bpx, bpy = iso_project(bx, WALL_Y + 0.5, PIPE_Z)
    ax.plot(bpx, bpy, 'o', color=pipe_color, markersize=3, zorder=7)

pump_x = POND_W + 0.8
pump_y = WALL_Y
pump_z = -0.5
draw_line_3d(ax, (pump_x, pump_y, pump_z), (POND_W - 0.3, pump_y, pump_z), color=pipe_color, lw=2.5, zorder=7)
draw_line_3d(ax, (POND_W - 0.3, pump_y, pump_z), (POND_W - 0.3, pump_y, PIPE_Z), color=pipe_color, lw=2.5, zorder=7)
draw_line_3d(ax, (POND_W - 0.3, pump_y, PIPE_Z), (POND_W - 0.3, manifold_y, PIPE_Z), color=pipe_color, lw=2.5, zorder=7)
draw_line_3d(ax, (POND_W - 0.3, manifold_y, PIPE_Z), (POND_W - 0.8, manifold_y, PIPE_Z), color=pipe_color, lw=2.5, zorder=7)

skimmer_x = POND_W - 1.0
skimmer_y = 0.5
draw_line_3d(ax, (skimmer_x, skimmer_y, WATER_Z - 0.05), (skimmer_x, skimmer_y, PIPE_Z), color='#BF360C', lw=2.0, zorder=7)
draw_line_3d(ax, (skimmer_x, skimmer_y, PIPE_Z), (POND_W - 0.3, skimmer_y, PIPE_Z), color='#BF360C', lw=2.0, zorder=7)
draw_line_3d(ax, (POND_W - 0.3, skimmer_y, PIPE_Z), (POND_W - 0.3, pump_y, PIPE_Z), color='#BF360C', lw=2.0, ls='--', zorder=7)
draw_line_3d(ax, (POND_W - 0.3, pump_y, PIPE_Z), (pump_x, pump_y, pump_z), color='#BF360C', lw=2.0, ls='--', zorder=7, alpha=0.6)

drain_x = POND_W / 2
drain_y = 2.5
draw_line_3d(ax, (drain_x, drain_y, SWIM_FLOOR_Z), (drain_x, drain_y, SWIM_FLOOR_Z - 0.15), color='#BF360C', lw=2.0, zorder=2)
draw_line_3d(ax, (drain_x, drain_y, SWIM_FLOOR_Z - 0.15), (POND_W + 0.3, drain_y, SWIM_FLOOR_Z - 0.15), color='#BF360C', lw=2.0, ls='--', zorder=2, alpha=0.5)
draw_line_3d(ax, (POND_W + 0.3, drain_y, SWIM_FLOOR_Z - 0.15), (POND_W + 0.3, pump_y, pump_z - 0.3), color='#BF360C', lw=2.0, ls='--', zorder=2, alpha=0.5)

# 7. PUMP CHAMBER
draw_box(ax, pump_x - 0.4, pump_y - 0.4, pump_z - 0.6, 0.8, 0.8, 0.8,
         '#FF6F00', '#E65100', '#F57C00', alpha=0.8, zorder=10)
ppx, ppy = iso_project(pump_x, pump_y, pump_z + 0.4)
ax.annotate('PUMP\nCHAMBER', (ppx, ppy), fontsize=7, fontweight='bold',
            color='#BF360C', ha='center', va='bottom', zorder=20,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF3E0', edgecolor='#E65100', alpha=0.9))

# 8. SKIMMER
draw_box(ax, skimmer_x - 0.2, skimmer_y - 0.2, WATER_Z - 0.3, 0.4, 0.4, 0.35,
         '#FFB74D', '#F57C00', '#FFA726', alpha=0.8, zorder=10)
sk_px, sk_py = iso_project(skimmer_x, skimmer_y, WATER_Z + 0.15)
ax.annotate('SKIMMER', (sk_px, sk_py), fontsize=6, fontweight='bold', color='#E65100', ha='center', va='bottom', zorder=20)

# 9. BOTTOM DRAIN
drain_pts = [(drain_x - 0.25, drain_y - 0.25, SWIM_FLOOR_Z + 0.01),
             (drain_x + 0.25, drain_y - 0.25, SWIM_FLOOR_Z + 0.01),
             (drain_x + 0.25, drain_y + 0.25, SWIM_FLOOR_Z + 0.01),
             (drain_x - 0.25, drain_y + 0.25, SWIM_FLOOR_Z + 0.01)]
draw_face(ax, drain_pts, '#E65100', alpha=0.7, edgecolor='#BF360C', lw=1.5, zorder=3)
bd_px, bd_py = iso_project(drain_x, drain_y, SWIM_FLOOR_Z + 0.15)
ax.annotate('BOTTOM\nDRAIN', (bd_px, bd_py), fontsize=5, fontweight='bold', color='#BF360C', ha='center', va='bottom', zorder=20)

# 10. ENTRY STEPS
step_x_start = (POND_W - STEP_W) / 2
for i, depth in enumerate(STEP_DEPTHS):
    sx = step_x_start + i * 0.3
    sw = STEP_W - i * 0.6
    sy = i * STEP_D
    prev_z = 0 if i == 0 else STEP_DEPTHS[i-1]
    step_h = abs(depth - prev_z)
    draw_box(ax, sx, sy, depth, sw, STEP_D, step_h,
             '#BDBDBD', '#9E9E9E', '#ABABAB', alpha=0.7, zorder=9)
sp_x, sp_y = iso_project(POND_W/2, 0.6, 0.2)
ax.annotate('ENTRY STEPS', (sp_x, sp_y), fontsize=6, fontweight='bold', color='#616161', ha='center', va='bottom', zorder=20)

# 11. WATER SURFACES
draw_face(ax,
    [(0, 0, WATER_Z), (POND_W, 0, WATER_Z), (POND_W, WALL_Y, WATER_Z), (0, WALL_Y, WATER_Z)],
    '#0288D1', alpha=0.2, edgecolor='#0288D1', lw=0.5, zorder=11)
draw_face(ax,
    [(0, WALL_Y, WATER_Z), (POND_W, WALL_Y, WATER_Z), (POND_W, POND_L, WATER_Z), (0, POND_L, WATER_Z)],
    '#4DB6AC', alpha=0.2, edgecolor='#00897B', lw=0.5, zorder=11)
for y_val in [0, POND_L]:
    draw_line_3d(ax, (0, y_val, WATER_Z), (POND_W, y_val, WATER_Z), color='#0288D1', lw=1.0, ls='--', zorder=12, alpha=0.6)
for x_val in [0, POND_W]:
    draw_line_3d(ax, (x_val, 0, WATER_Z), (x_val, POND_L, WATER_Z), color='#0288D1', lw=1.0, ls='--', zorder=12, alpha=0.6)

# 12. TERRACE / DECK
deck_depth = 2.0
deck_thickness = 0.15
draw_box(ax, -0.5, -deck_depth, TERRACE_Z - deck_thickness,
         POND_W + 1.0, deck_depth, deck_thickness,
         '#A0522D', '#7B3F1A', '#8B4513', alpha=0.6, zorder=12)
for plank_y in np.linspace(-deck_depth + 0.2, -0.2, 8):
    draw_line_3d(ax, (-0.5, plank_y, TERRACE_Z), (POND_W + 0.5, plank_y, TERRACE_Z), color='#6D3A1A', lw=0.5, zorder=13, alpha=0.4)
deck_px, deck_py = iso_project(POND_W/2, -deck_depth/2, TERRACE_Z + 0.15)
ax.annotate('WOODEN DECK / TERRACE', (deck_px, deck_py), fontsize=8, fontweight='bold',
            color='#5D4037', ha='center', va='bottom', zorder=20,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#EFEBE9', edgecolor='#8D6E63', alpha=0.9))
draw_box(ax, -0.1, -0.1, TERRACE_Z - 0.05, POND_W + 0.2, 0.15, 0.05,
         '#E0E0E0', '#BDBDBD', '#CCCCCC', alpha=0.8, zorder=13)

# 13. PLANTS
plant_positions = [
    (1.0, WALL_Y + 0.5), (2.5, WALL_Y + 0.6), (4.0, WALL_Y + 0.4),
    (5.5, WALL_Y + 0.5), (6.5, WALL_Y + 0.6),
    (2.0, WALL_Y + 1.2), (4.0, WALL_Y + 1.5), (6.0, WALL_Y + 1.2),
    (1.0, z2_y0 + 0.3), (3.0, z2_y0 + 0.5), (5.0, z2_y0 + 0.4), (7.0, z2_y0 + 0.3),
    (0.5, z1_y0 + 0.3), (2.0, z1_y0 + 0.5), (3.5, z1_y0 + 0.7),
    (5.0, z1_y0 + 0.5), (6.8, z1_y0 + 0.4),
]
for px_val, py_val in plant_positions:
    if py_val < z3_y1:
        base_z = GRAVEL_TOP_Z
    elif py_val < z2_y1:
        base_z = Z2_Z
    else:
        base_z = Z1_Z
    stem_top = WATER_Z + np.random.uniform(0.15, 0.35)
    p_base = iso_project(px_val, py_val, base_z)
    p_top = iso_project(px_val, py_val, stem_top)
    ax.plot([p_base[0], p_top[0]], [p_base[1], p_top[1]], color='#4CAF50', linewidth=1.0, zorder=14)
    ax.plot(p_top[0], p_top[1], marker=6, color='#2E7D32', markersize=np.random.uniform(6, 10), zorder=14)

# 14. ZONE LABELS
swim_px, swim_py = iso_project(POND_W/2, WALL_Y/2, WATER_Z + 0.3)
ax.annotate('SWIMMING ZONE\n2.0m deep\n38 m2', (swim_px, swim_py),
            fontsize=10, fontweight='bold', color='#01579B', ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#E1F5FE', edgecolor='#0277BD', alpha=0.9))

regen_px, regen_py = iso_project(POND_W/2, (WALL_Y + POND_L)/2, WATER_Z + 0.3)
ax.annotate('REGENERATION &\nFILTRATION ZONE\n3 banded depth zones  |  38 m2',
            (regen_px, regen_py),
            fontsize=9, fontweight='bold', color='#1B5E20', ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#E8F5E9', edgecolor='#2E7D32', alpha=0.9))

wall_px, wall_py = iso_project(POND_W/2, WALL_Y, WALL_TOP_Z + 0.55)
ax.annotate('SEPARATION WALL\n(top 0.3m below water)\n3 water passages', (wall_px, wall_py),
            fontsize=7, fontweight='bold', color='#424242', ha='center', va='bottom', zorder=20,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#616161', alpha=0.9))

pipe_px, pipe_py = iso_project(POND_W/2, manifold_y + 0.3, PIPE_Z - 0.15)
ax.annotate('DISTRIBUTION PIPES\n(perforated, under gravel)', (pipe_px, pipe_py),
            fontsize=6, color='#BF360C', ha='center', va='top', zorder=20,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FBE9E7', edgecolor='#E65100', alpha=0.9))

# 15. DIMENSION ANNOTATIONS
d1 = iso_project(-0.3, 0, TERRACE_Z + 0.1)
d2 = iso_project(-0.3, POND_L, TERRACE_Z + 0.1)
ax.annotate('', xy=d2, xytext=d1, arrowprops=dict(arrowstyle='<->', color='#333', lw=1.2), zorder=20)
dm = iso_project(-0.8, POND_L/2, TERRACE_Z + 0.1)
ax.annotate('10.0m', dm, fontsize=8, fontweight='bold', color='#333', ha='right', va='center', zorder=20,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

d3 = iso_project(0, POND_L + 0.3, TERRACE_Z + 0.1)
d4 = iso_project(POND_W, POND_L + 0.3, TERRACE_Z + 0.1)
ax.annotate('', xy=d4, xytext=d3, arrowprops=dict(arrowstyle='<->', color='#333', lw=1.2), zorder=20)
dm2 = iso_project(POND_W/2, POND_L + 0.8, TERRACE_Z + 0.1)
ax.annotate('7.5m', dm2, fontsize=8, fontweight='bold', color='#333', ha='center', va='bottom', zorder=20,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

dd1 = iso_project(POND_W + 0.3, 1.0, TERRACE_Z)
dd2 = iso_project(POND_W + 0.3, 1.0, SWIM_FLOOR_Z)
ax.annotate('', xy=dd2, xytext=dd1, arrowprops=dict(arrowstyle='<->', color='#0277BD', lw=1.2), zorder=20)
ddm = iso_project(POND_W + 0.8, 1.0, (TERRACE_Z + SWIM_FLOOR_Z)/2)
ax.annotate('2.0m\ndeep', ddm, fontsize=7, fontweight='bold', color='#01579B', ha='left', va='center', zorder=20)

# 16. FLOW DIRECTION ARROWS
for offset_x in [2.0, 5.5]:
    a1 = iso_project(offset_x, 1.5, WATER_Z - 0.3)
    a2 = iso_project(offset_x, WALL_Y - 0.5, WATER_Z - 0.3)
    ax.annotate('', xy=a2, xytext=a1, arrowprops=dict(arrowstyle='->', color='#0288D1', lw=1.5, alpha=0.5), zorder=15)
for offset_x in [2.0, 5.5]:
    a1 = iso_project(offset_x, POND_L - 1.0, WATER_Z - 0.2)
    a2 = iso_project(offset_x, WALL_Y + 0.5, WATER_Z - 0.2)
    ax.annotate('', xy=a2, xytext=a1, arrowprops=dict(arrowstyle='->', color='#43A047', lw=1.5, alpha=0.5), zorder=15)

# 17. TITLE AND LEGEND
ax.set_title(
    'Natural Swimming Pond (Schwimmteich) -- 3D Isometric Cutaway View\n'
    'Version 2 -- Banded Zones  (vertical scale 1.5x for clarity)',
    fontsize=16, fontweight='bold', pad=20)

legend_items = [
    mpatches.Patch(facecolor='#0288D1', alpha=0.3, edgecolor='#0277BD', label='Swimming water (2.0m)'),
    mpatches.Patch(facecolor='#4DB6AC', alpha=0.3, edgecolor='#00897B', label='Regen zone water (0.1-1.0m)'),
    mpatches.Patch(facecolor='#616161', alpha=0.7, edgecolor='#333', label='Separation wall (RC)'),
    mpatches.Patch(facecolor='#E65100', alpha=0.65, edgecolor='#BF360C',
                   label='Zone 3: Deep gravel (60-100cm) -- %.1f m2' % z3_area),
    mpatches.Patch(facecolor='#FDD835', alpha=0.65, edgecolor='#F9A825',
                   label='Zone 2: Shallow (30-60cm) -- %.1f m2' % z2_area),
    mpatches.Patch(facecolor='#43A047', alpha=0.65, edgecolor='#2E7D32',
                   label='Zone 1: Marginal (0-30cm) -- %.1f m2' % z1_area),
    mpatches.Patch(facecolor='#A0522D', alpha=0.6, edgecolor='#6D3A1A', label='Wooden deck/terrace'),
    mpatches.Patch(facecolor='#BDBDBD', alpha=0.7, edgecolor='#9E9E9E', label='Entry steps'),
    plt.Line2D([0], [0], color='#E65100', lw=2.5, label='Supply piping (pump -> regen)'),
    plt.Line2D([0], [0], color='#BF360C', lw=2.0, ls='--', label='Return piping (skimmer/drain -> pump)'),
    mpatches.Patch(facecolor='#FF6F00', alpha=0.8, edgecolor='#E65100', label='Pump chamber'),
    plt.Line2D([0], [0], color='#2E7D32', marker=6, markersize=8, lw=0, label='Aquatic plants'),
]
ax.legend(handles=legend_items, loc='lower left', fontsize=7, framealpha=0.95,
          edgecolor='#ccc', fancybox=True, ncol=2, title='Legend', title_fontsize=8)

info_text = (
    "CIRCULATION: Skimmer + bottom drain -> pump -> distribution manifold\n"
    "-> perforated pipes under gravel -> biological filtration through\n"
    "gravel layers -> clean water flows through wall passages -> swim zone\n"
    "\n"
    "BANDED ZONES: Z3 (gravel, 2.35m) -> Z2 (shallow, 1.10m) -> Z1 (marginal, 1.55m)\n"
    "Water rises from deep gravel bed through progressively shallower bands\n"
    "GRAVEL: 3 layers -- coarse (16-32mm), medium (8-16mm), fine (2-8mm)"
)
ax.text(0.98, 0.02, info_text, transform=ax.transAxes,
        fontsize=6, verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FAFAFA', edgecolor='#ccc', alpha=0.95),
        fontfamily='monospace', zorder=25)

plt.tight_layout()
plt.savefig('schwimmteich_3d_isometric_v2.png', dpi=200, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print('Saved schwimmteich_3d_isometric_v2.png')
