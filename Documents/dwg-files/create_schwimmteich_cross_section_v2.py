"""
Detailed cross-section through the Schwimmteich (natural swimming pond).
Version 2 — Banded Zones: regeneration zone has three sequential depth bands
(staircase profile) instead of symmetric concentric rings.

Layout left-to-right:
  Deck -> Steps -> Swimming Zone (2.0m) -> Separation Wall ->
  Zone 3 (deepest, 2.35m) -> Zone 2 (medium, 1.10m) -> Zone 1 (shallowest, 1.55m) -> end
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Rectangle

# =============================================================
# DIMENSIONS (matching 3D isometric script)
# =============================================================

# Horizontal positions (distance from terrace edge, positive = away from house)
DECK_START = -2.0     # deck extends 2m behind pond edge
DECK_END = 0.0        # deck/terrace edge
POND_START = 0.1      # coping stone gap
POND_END = 10.1       # far end of pond (10m long)
WALL_POS = 5.1        # separation wall centre (5m from pond start)
WALL_T = 0.30         # wall thickness

# Elevation (relative, terrace = 0)
TERRACE_Z = 0.0
WATER_Z = -0.10
SWIM_FLOOR_Z = -2.00
WALL_TOP_Z = -0.40
WALL_BASE_Z = -2.00

# Regen zone depths (3 zones) — banded layout
Z1_Z = -0.15    # marginal zone floor (shallowest)
Z2_Z = -0.45    # medium zone floor
Z3_Z = -1.00    # deep gravel bed floor (= GRAVEL_BOT_Z)

# Banded zone lengths (left-to-right after wall)
Z3_LEN = 2.35   # Zone 3: directly after wall, deepest
Z2_LEN = 1.10   # Zone 2: medium
Z1_LEN = 1.55   # Zone 1: shallowest, at far end
# Total = 5.0m

# Gravel layers within Zone 3
GRAVEL_COARSE_TOP = -1.00   # bottom of zone = coarse base
GRAVEL_COARSE_Z = -0.87     # top of coarse layer
GRAVEL_MED_Z = -0.73        # top of medium layer
GRAVEL_FINE_Z = -0.60       # top of fine layer (= gravel surface)

# Pipe level
PIPE_Z = -1.10

# Steps
STEP_DEPTHS = [-0.30, -0.60, -0.90]
STEP_D = 0.4  # each step tread depth

# Deck
DECK_THICKNESS = 0.15

# Liner thickness (exaggerated for visibility)
LINER_T = 0.06

# Shell/concrete thickness
SHELL_T = 0.15

# =============================================================
# COMPUTED ZONE BOUNDARIES (banded, sequential)
# =============================================================
regen_start = WALL_POS + WALL_T / 2          # start of regen zone
z3_end = regen_start + Z3_LEN                 # end of Zone 3
z2_end = z3_end + Z2_LEN                      # end of Zone 2
z1_end = z2_end + Z1_LEN                      # end of Zone 1
# z1_end = 5.25 + 2.35 + 1.10 + 1.55 = 10.25
POND_END_ACTUAL = z1_end  # actual far edge of regen zone

# =============================================================
# FIGURE SETUP
# =============================================================

fig, ax = plt.subplots(1, 1, figsize=(22, 10))

# =============================================================
# HELPER: draw a filled polygon
# =============================================================
def poly(ax, xs, zs, color, alpha=1.0, ec='#333', lw=0.5, zorder=2, label=None):
    ax.fill(xs, zs, color=color, alpha=alpha, edgecolor=ec, linewidth=lw,
            zorder=zorder, label=label)

# =============================================================
# 1. GROUND / EARTH (background)
# =============================================================
ground_xs = [DECK_START - 1.0, POND_END_ACTUAL + 1.5, POND_END_ACTUAL + 1.5, DECK_START - 1.0]
ground_zs = [TERRACE_Z, TERRACE_Z - 0.5, -3.0, -3.0]
poly(ax, ground_xs, ground_zs, '#C4A882', alpha=0.3, ec='none', zorder=0)

# Ground surface line
ax.plot([DECK_START - 1.0, DECK_END], [TERRACE_Z, TERRACE_Z],
        color='#8B7355', lw=2, zorder=1)
ax.plot([POND_END_ACTUAL, POND_END_ACTUAL + 1.5], [TERRACE_Z - 0.05, TERRACE_Z - 0.5],
        color='#8B7355', lw=2, zorder=1)

# =============================================================
# 2. CONCRETE SHELL (pond structure)
# =============================================================
shell_color = '#B0BEC5'

# Swimming zone shell — Floor
poly(ax, [POND_START, WALL_POS - WALL_T/2, WALL_POS - WALL_T/2, POND_START],
         [SWIM_FLOOR_Z, SWIM_FLOOR_Z, SWIM_FLOOR_Z - SHELL_T, SWIM_FLOOR_Z - SHELL_T],
     shell_color, alpha=0.6, ec='#78909C', lw=1.0, zorder=1)
# Left wall
poly(ax, [POND_START - SHELL_T, POND_START, POND_START, POND_START - SHELL_T],
         [SWIM_FLOOR_Z - SHELL_T, SWIM_FLOOR_Z, TERRACE_Z, TERRACE_Z],
     shell_color, alpha=0.6, ec='#78909C', lw=1.0, zorder=1)

# Regen zone shell — staircase profile (Z3 -> Z2 -> Z1 left to right)
regen_profile_x = [regen_start, z3_end, z3_end, z2_end, z2_end, z1_end]
regen_profile_z = [Z3_Z,        Z3_Z,   Z2_Z,   Z2_Z,   Z1_Z,   Z1_Z]

# Shell under regen stepped floor
for i in range(len(regen_profile_x) - 1):
    x0, x1 = regen_profile_x[i], regen_profile_x[i+1]
    z_top = regen_profile_z[i]
    z_bot = z_top - SHELL_T
    z_top_next = regen_profile_z[i+1]
    z_bot_next = z_top_next - SHELL_T
    poly(ax, [x0, x1, x1, x0], [z_top, z_top_next, z_bot_next, z_bot],
         shell_color, alpha=0.5, ec='#78909C', lw=0.5, zorder=1)

# Far wall shell
poly(ax, [POND_END_ACTUAL, POND_END_ACTUAL + SHELL_T, POND_END_ACTUAL + SHELL_T, POND_END_ACTUAL],
         [Z1_Z, Z1_Z - SHELL_T, TERRACE_Z, TERRACE_Z],
     shell_color, alpha=0.6, ec='#78909C', lw=1.0, zorder=1)

# =============================================================
# 3. SWIMMING ZONE
# =============================================================

# Steps profile (left side of swim zone)
step_profile_x = [POND_START]
step_profile_z = [WATER_Z]
for i, depth in enumerate(STEP_DEPTHS):
    sx = POND_START + i * STEP_D
    step_profile_x.extend([sx, sx + STEP_D])
    step_profile_z.extend([depth, depth])
# After last step, go down to floor
last_step_x = POND_START + len(STEP_DEPTHS) * STEP_D
step_profile_x.extend([last_step_x, last_step_x])
step_profile_z.extend([STEP_DEPTHS[-1], SWIM_FLOOR_Z])

# Full swimming zone water
full_swim_x = step_profile_x + [WALL_POS - WALL_T/2, WALL_POS - WALL_T/2, POND_START]
full_swim_z = step_profile_z + [SWIM_FLOOR_Z, WATER_Z, WATER_Z]
poly(ax, full_swim_x, full_swim_z, '#0288D1', alpha=0.25, ec='none', zorder=3,
     label='Swimming water (2.0m)')

# Swimming floor
ax.plot([POND_START, WALL_POS - WALL_T/2], [SWIM_FLOOR_Z, SWIM_FLOOR_Z],
        color='#546E7A', lw=2, zorder=4)

# =============================================================
# 4. ENTRY STEPS
# =============================================================
for i, depth in enumerate(STEP_DEPTHS):
    sx = POND_START + i * STEP_D
    prev_z = TERRACE_Z if i == 0 else STEP_DEPTHS[i-1]
    poly(ax, [sx, sx + STEP_D, sx + STEP_D, sx],
             [prev_z, prev_z, depth, depth],
         '#BDBDBD', alpha=0.8, ec='#9E9E9E', lw=1.0, zorder=5)
    # Step number
    mid_x = sx + STEP_D / 2
    mid_z = (prev_z + depth) / 2
    ax.text(mid_x, mid_z, f'{i+1}', fontsize=7, ha='center', va='center',
            color='#616161', fontweight='bold', zorder=6)

# =============================================================
# 5. SEPARATION WALL
# =============================================================
wall_x0 = WALL_POS - WALL_T/2
wall_x1 = WALL_POS + WALL_T/2

poly(ax, [wall_x0, wall_x1, wall_x1, wall_x0],
         [WALL_BASE_Z, WALL_BASE_Z, WALL_TOP_Z, WALL_TOP_Z],
     '#616161', alpha=0.85, ec='#424242', lw=1.5, zorder=8)

# Wall hatching (diagonal lines for concrete)
for hatch_z in np.arange(WALL_BASE_Z, WALL_TOP_Z, 0.08):
    ax.plot([wall_x0, wall_x1], [hatch_z, hatch_z + 0.04],
            color='#424242', lw=0.3, zorder=9, alpha=0.5)

# Water passage (opening in wall, shown as blue gap)
passage_z_bot = WALL_BASE_Z + 0.3
passage_z_top = WALL_TOP_Z - 0.2
poly(ax, [wall_x0, wall_x1, wall_x1, wall_x0],
         [passage_z_bot, passage_z_bot, passage_z_top, passage_z_top],
     '#29B6F6', alpha=0.5, ec='#0288D1', lw=1.0, zorder=9)

# Flow arrow through passage
passage_mid_z = (passage_z_bot + passage_z_top) / 2
ax.annotate('', xy=(wall_x0 - 0.15, passage_mid_z), xytext=(wall_x1 + 0.15, passage_mid_z),
            arrowprops=dict(arrowstyle='->', color='#0288D1', lw=2.0), zorder=10)

# =============================================================
# 6. REGENERATION ZONE - THREE BANDED DEPTH ZONES (staircase)
# =============================================================

# --- Zone 3: Deep gravel bed (deepest, directly after wall) ---
# Water above gravel in Zone 3
poly(ax, [regen_start, z3_end, z3_end, regen_start],
         [WATER_Z, WATER_Z, GRAVEL_FINE_Z, GRAVEL_FINE_Z],
     '#4DB6AC', alpha=0.2, ec='none', zorder=3)
# Zone 3 floor line
ax.plot([regen_start, z3_end], [Z3_Z, Z3_Z], color='#5D4037', lw=2, zorder=4)

# --- Zone 2: Medium (0.3-0.6m) ---
poly(ax, [z3_end, z2_end, z2_end, z3_end, z3_end],
         [WATER_Z, WATER_Z, Z2_Z, Z2_Z, Z3_Z],
     '#FDD835', alpha=0.35, ec='#F9A825', lw=1.0, zorder=3)
# Zone 2 floor line
ax.plot([z3_end, z2_end], [Z2_Z, Z2_Z], color='#F9A825', lw=2, zorder=4)

# --- Zone 1: Marginal / shallowest (0-0.3m, at far end) ---
poly(ax, [z2_end, z1_end, z1_end, z2_end, z2_end],
         [WATER_Z, WATER_Z, Z1_Z, Z1_Z, Z2_Z],
     '#43A047', alpha=0.35, ec='#2E7D32', lw=1.0, zorder=3)
# Zone 1 floor line
ax.plot([z2_end, z1_end], [Z1_Z, Z1_Z], color='#2E7D32', lw=2, zorder=4)

# Step-down faces (vertical lines at zone boundaries)
# Z3->Z2 boundary
ax.plot([z3_end, z3_end], [Z3_Z, Z2_Z], color='#BF360C', lw=2.5, zorder=5)
# Z2->Z1 boundary
ax.plot([z2_end, z2_end], [Z2_Z, Z1_Z], color='#33691E', lw=2.5, zorder=5)

# =============================================================
# 7. GRAVEL LAYERS (in Zone 3 only)
# =============================================================

# Coarse gravel (bottom layer)
poly(ax, [regen_start + 0.05, z3_end - 0.05, z3_end - 0.05, regen_start + 0.05],
         [Z3_Z, Z3_Z, GRAVEL_COARSE_Z, GRAVEL_COARSE_Z],
     '#5D4037', alpha=0.7, ec='#4E342E', lw=0.8, zorder=5,
     label='Gravel: coarse (16-32mm)')

# Medium gravel (middle layer)
poly(ax, [regen_start + 0.05, z3_end - 0.05, z3_end - 0.05, regen_start + 0.05],
         [GRAVEL_COARSE_Z, GRAVEL_COARSE_Z, GRAVEL_MED_Z, GRAVEL_MED_Z],
     '#795548', alpha=0.65, ec='#5D4037', lw=0.8, zorder=5,
     label='Gravel: medium (8-16mm)')

# Fine gravel (top layer)
poly(ax, [regen_start + 0.05, z3_end - 0.05, z3_end - 0.05, regen_start + 0.05],
         [GRAVEL_MED_Z, GRAVEL_MED_Z, GRAVEL_FINE_Z, GRAVEL_FINE_Z],
     '#A1887F', alpha=0.6, ec='#795548', lw=0.8, zorder=5,
     label='Gravel: fine (2-8mm)')

# Gravel texture (dots)
np.random.seed(42)
for _ in range(120):
    gx = np.random.uniform(regen_start + 0.1, z3_end - 0.1)
    gz = np.random.uniform(Z3_Z + 0.02, GRAVEL_FINE_Z - 0.02)
    size = np.random.uniform(1.0, 3.0)
    if gz < GRAVEL_COARSE_Z:
        gc = '#4E342E'
    elif gz < GRAVEL_MED_Z:
        gc = '#6D4C41'
    else:
        gc = '#8D6E63'
    ax.plot(gx, gz, '.', color=gc, markersize=size, zorder=6, alpha=0.7)

# =============================================================
# 8. PIPING (manifold under Zone 3 gravel)
# =============================================================

pipe_lw = 3.5

# Distribution manifold (horizontal, under gravel in zone 3)
ax.plot([regen_start + 0.3, z3_end - 0.3], [PIPE_Z, PIPE_Z],
        color='#E65100', lw=pipe_lw, zorder=7, solid_capstyle='round')
# Pipe outline
ax.plot([regen_start + 0.3, z3_end - 0.3], [PIPE_Z, PIPE_Z],
        color='#BF360C', lw=pipe_lw + 1.5, zorder=6.5, solid_capstyle='round', alpha=0.3)

# Perforated holes (upward arrows from pipe)
for px in np.linspace(regen_start + 0.5, z3_end - 0.5, 7):
    ax.annotate('', xy=(px, PIPE_Z + 0.08), xytext=(px, PIPE_Z),
                arrowprops=dict(arrowstyle='->', color='#E65100', lw=1.0), zorder=8)
    ax.plot(px, PIPE_Z + 0.08, 'o', color='#E65100', markersize=2.5, zorder=8)

# Feed pipe from pump (vertical rise to manifold level)
pump_x = POND_END_ACTUAL + 0.8
pump_z = -0.50
ax.plot([pump_x, pump_x], [pump_z, PIPE_Z], color='#E65100', lw=pipe_lw, zorder=7,
        solid_capstyle='round')
ax.plot([pump_x, z3_end - 0.3], [PIPE_Z, PIPE_Z], color='#E65100', lw=pipe_lw, zorder=7,
        solid_capstyle='round', linestyle='--', alpha=0.6)

# Return pipe from skimmer/drain to pump (dashed, under swim zone)
skimmer_x = POND_START + 0.5
ax.plot([skimmer_x, skimmer_x], [WATER_Z - 0.05, SWIM_FLOOR_Z - 0.2],
        color='#BF360C', lw=2.5, ls='--', zorder=2, alpha=0.6)
ax.plot([skimmer_x, pump_x], [SWIM_FLOOR_Z - 0.2, SWIM_FLOOR_Z - 0.2],
        color='#BF360C', lw=2.5, ls='--', zorder=2, alpha=0.5)
ax.plot([pump_x, pump_x], [SWIM_FLOOR_Z - 0.2, pump_z], color='#BF360C', lw=2.5,
        ls='--', zorder=2, alpha=0.5)

# Bottom drain pipe
drain_x = (POND_START + WALL_POS) / 2
ax.plot([drain_x, drain_x], [SWIM_FLOOR_Z, SWIM_FLOOR_Z - 0.2],
        color='#BF360C', lw=2.5, ls='--', zorder=2, alpha=0.6)

# =============================================================
# 9. SKIMMER & BOTTOM DRAIN symbols
# =============================================================

# Skimmer at water surface
sk_rect = Rectangle((skimmer_x - 0.15, WATER_Z - 0.25), 0.3, 0.30,
                     facecolor='#FFB74D', edgecolor='#E65100', lw=1.5, zorder=10)
ax.add_patch(sk_rect)

# Bottom drain grate
bd_rect = Rectangle((drain_x - 0.2, SWIM_FLOOR_Z - 0.05), 0.4, 0.05,
                     facecolor='#E65100', edgecolor='#BF360C', lw=1.5, zorder=10)
ax.add_patch(bd_rect)

# Pump chamber
pump_rect = Rectangle((pump_x - 0.3, pump_z - 0.5), 0.6, 0.7,
                       facecolor='#FF6F00', edgecolor='#E65100', lw=2.0, zorder=10)
ax.add_patch(pump_rect)

# =============================================================
# 10. WATER LEVEL LINE
# =============================================================
ax.plot([POND_START, POND_END_ACTUAL], [WATER_Z, WATER_Z],
        color='#0288D1', lw=1.5, ls='--', zorder=11, alpha=0.7)

# =============================================================
# 11. TERRACE / DECK
# =============================================================
poly(ax, [DECK_START, DECK_END + 0.05, DECK_END + 0.05, DECK_START],
         [TERRACE_Z, TERRACE_Z, TERRACE_Z - DECK_THICKNESS, TERRACE_Z - DECK_THICKNESS],
     '#A0522D', alpha=0.7, ec='#6D3A1A', lw=1.5, zorder=10)

# Deck plank lines
for dx in np.linspace(DECK_START + 0.15, DECK_END - 0.05, 6):
    ax.plot([dx, dx], [TERRACE_Z, TERRACE_Z - DECK_THICKNESS],
            color='#7B3F1A', lw=0.5, zorder=11, alpha=0.5)

# Coping stone
poly(ax, [DECK_END, POND_START, POND_START, DECK_END],
         [TERRACE_Z + 0.02, TERRACE_Z + 0.02, TERRACE_Z - 0.05, TERRACE_Z - 0.05],
     '#E0E0E0', alpha=0.9, ec='#BDBDBD', lw=1.0, zorder=11)

# =============================================================
# 12. PLANTS (positioned for banded zones)
# =============================================================

def draw_plant(ax, x, base_z, height, leaf_size=8):
    """Draw a simple plant symbol."""
    top_z = base_z + height
    ax.plot([x, x], [base_z, top_z], color='#4CAF50', lw=1.2, zorder=12)
    ax.plot(x, top_z, marker=6, color='#2E7D32', markersize=leaf_size, zorder=12)
    # Roots
    for rx in [-0.08, 0, 0.08]:
        ax.plot([x, x + rx], [base_z, base_z - 0.06], color='#795548', lw=0.5,
                zorder=12, alpha=0.6)

# Zone 1 plants (tall emergent, above water) — at far end
for px in np.linspace(z2_end + 0.3, z1_end - 0.3, 3):
    draw_plant(ax, px, Z1_Z, 0.45, leaf_size=10)

# Zone 2 plants (medium, partially above water) — middle band
for px in np.linspace(z3_end + 0.2, z2_end - 0.2, 2):
    draw_plant(ax, px, Z2_Z, 0.55, leaf_size=9)

# Zone 3 plants (submerged oxygenators + lily pads at surface) — near wall
for px in np.linspace(regen_start + 0.4, z3_end - 0.4, 4):
    # Submerged stem
    ax.plot([px, px], [GRAVEL_FINE_Z, WATER_Z - 0.02], color='#4CAF50', lw=0.8,
            zorder=12, alpha=0.6)
    # Lily pad at surface
    ax.plot(px, WATER_Z, 'o', color='#2E7D32', markersize=6, zorder=12)
    ax.plot(px, WATER_Z + 0.02, '_', color='#1B5E20', markersize=10, mew=2, zorder=12)

# =============================================================
# 13. DIMENSION ANNOTATIONS
# =============================================================

dim_color = '#333333'
dim_lw = 0.8

# --- Vertical dimensions (left side) ---
# Swimming zone depth
vd_x = POND_START - 0.4
ax.annotate('', xy=(vd_x, SWIM_FLOOR_Z), xytext=(vd_x, TERRACE_Z),
            arrowprops=dict(arrowstyle='<->', color='#0277BD', lw=1.2), zorder=15)
ax.text(vd_x - 0.15, (TERRACE_Z + SWIM_FLOOR_Z)/2, '2.0m',
        fontsize=9, fontweight='bold', color='#01579B', ha='right', va='center',
        rotation=90, zorder=15,
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=2))

# Regen zone depths (far right side)
rd_x = POND_END_ACTUAL + 0.3
# Zone 1
ax.annotate('', xy=(rd_x, Z1_Z), xytext=(rd_x, TERRACE_Z),
            arrowprops=dict(arrowstyle='<->', color='#2E7D32', lw=1.0), zorder=15)
ax.text(rd_x + 0.15, (TERRACE_Z + Z1_Z)/2, '0.15m',
        fontsize=7, fontweight='bold', color='#2E7D32', ha='left', va='center', zorder=15)
# Zone 2
rd_x2 = POND_END_ACTUAL + 0.6
ax.annotate('', xy=(rd_x2, Z2_Z), xytext=(rd_x2, Z1_Z),
            arrowprops=dict(arrowstyle='<->', color='#F57F17', lw=1.0), zorder=15)
ax.text(rd_x2 + 0.15, (Z1_Z + Z2_Z)/2, '0.30m',
        fontsize=7, fontweight='bold', color='#F57F17', ha='left', va='center', zorder=15)
# Zone 3
rd_x3 = POND_END_ACTUAL + 0.9
ax.annotate('', xy=(rd_x3, Z3_Z), xytext=(rd_x3, Z2_Z),
            arrowprops=dict(arrowstyle='<->', color='#BF360C', lw=1.0), zorder=15)
ax.text(rd_x3 + 0.15, (Z2_Z + Z3_Z)/2, '0.55m',
        fontsize=7, fontweight='bold', color='#BF360C', ha='left', va='center', zorder=15)
# Total regen depth
rd_x4 = POND_END_ACTUAL + 1.3
ax.annotate('', xy=(rd_x4, Z3_Z), xytext=(rd_x4, TERRACE_Z),
            arrowprops=dict(arrowstyle='<->', color=dim_color, lw=1.0), zorder=15)
ax.text(rd_x4 + 0.15, (TERRACE_Z + Z3_Z)/2, '1.0m\ntotal',
        fontsize=8, fontweight='bold', color=dim_color, ha='left', va='center', zorder=15)

# --- Horizontal dimensions (below) ---
dim_z = -2.5

# Swimming zone
ax.annotate('', xy=(WALL_POS - WALL_T/2, dim_z), xytext=(POND_START, dim_z),
            arrowprops=dict(arrowstyle='<->', color=dim_color, lw=dim_lw), zorder=15)
ax.text((POND_START + WALL_POS)/2, dim_z - 0.1, '5.0m\nSwimming Zone',
        fontsize=8, fontweight='bold', color=dim_color, ha='center', va='top', zorder=15)

# Regen zone
ax.annotate('', xy=(POND_END_ACTUAL, dim_z), xytext=(WALL_POS + WALL_T/2, dim_z),
            arrowprops=dict(arrowstyle='<->', color=dim_color, lw=dim_lw), zorder=15)
ax.text((WALL_POS + POND_END_ACTUAL)/2, dim_z - 0.1, '5.0m\nRegeneration Zone',
        fontsize=8, fontweight='bold', color=dim_color, ha='center', va='top', zorder=15)

# Total
dim_z2 = -2.8
ax.annotate('', xy=(POND_END_ACTUAL, dim_z2), xytext=(POND_START, dim_z2),
            arrowprops=dict(arrowstyle='<->', color=dim_color, lw=1.2), zorder=15)
ax.text((POND_START + POND_END_ACTUAL)/2, dim_z2 - 0.1, '10.0m total',
        fontsize=9, fontweight='bold', color=dim_color, ha='center', va='top', zorder=15)

# Zone widths within regen (banded: Z3 | Z2 | Z1)
dim_z3 = Z3_Z - 0.25
# Z3 (nearest to wall)
ax.annotate('', xy=(z3_end, dim_z3), xytext=(regen_start, dim_z3),
            arrowprops=dict(arrowstyle='<->', color='#BF360C', lw=0.8), zorder=15)
ax.text((regen_start + z3_end)/2, dim_z3 - 0.06, f'{Z3_LEN:.2f}m', fontsize=6,
        color='#BF360C', ha='center', va='top', zorder=15)
# Z2
ax.annotate('', xy=(z2_end, dim_z3), xytext=(z3_end, dim_z3),
            arrowprops=dict(arrowstyle='<->', color='#F57F17', lw=0.8), zorder=15)
ax.text((z3_end + z2_end)/2, dim_z3 - 0.06, f'{Z2_LEN:.2f}m', fontsize=6,
        color='#F57F17', ha='center', va='top', zorder=15)
# Z1 (far end)
ax.annotate('', xy=(z1_end, dim_z3), xytext=(z2_end, dim_z3),
            arrowprops=dict(arrowstyle='<->', color='#2E7D32', lw=0.8), zorder=15)
ax.text((z2_end + z1_end)/2, dim_z3 - 0.06, f'{Z1_LEN:.2f}m', fontsize=6,
        color='#2E7D32', ha='center', va='top', zorder=15)

# =============================================================
# 14. ELEVATION LABELS
# =============================================================

elev_x = DECK_START - 0.5
elev_items = [
    (TERRACE_Z, '397.15', 'Terrace'),
    (WATER_Z, '397.05', 'Water level'),
    (WALL_TOP_Z, '396.75', 'Wall top'),
    (SWIM_FLOOR_Z, '395.15', 'Swim floor'),
]

for z, elev_str, label in elev_items:
    ax.plot([elev_x + 0.3, POND_START - 0.1], [z, z], color='#999', lw=0.5,
            ls=':', zorder=1, alpha=0.5)
    ax.text(elev_x, z, f'{elev_str}\n{label}', fontsize=6, color='#555',
            ha='right', va='center', zorder=15,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

# Regen zone elevations
relev_x = POND_END_ACTUAL + 1.8
relev_items = [
    (Z1_Z, '396.90', 'Z1 floor'),
    (Z2_Z, '396.60', 'Z2 floor'),
    (Z3_Z, '396.05', 'Z3 floor'),
]
for z, elev_str, label in relev_items:
    ax.text(relev_x, z, f'{elev_str} — {label}', fontsize=6, color='#555',
            ha='left', va='center', zorder=15,
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

# =============================================================
# 15. LABELS
# =============================================================

# Main zone labels
ax.text((POND_START + WALL_POS)/2, (WATER_Z + SWIM_FLOOR_Z)/2 + 0.2,
        'SWIMMING ZONE\n2.0m deep', fontsize=12, fontweight='bold',
        color='#01579B', ha='center', va='center', zorder=15,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#E1F5FE',
                  edgecolor='#0277BD', alpha=0.9))

# Zone labels in regen (banded: Z3 near wall, Z2 middle, Z1 far)
ax.text((regen_start + z3_end)/2, (WATER_Z + GRAVEL_FINE_Z)/2,
        'ZONE 3\nDeep Gravel\nBed', fontsize=9, fontweight='bold', color='#BF360C',
        ha='center', va='center', zorder=15,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FBE9E7',
                  edgecolor='#E65100', alpha=0.9))

ax.text((z3_end + z2_end)/2, (WATER_Z + Z2_Z)/2 - 0.05,
        'Z2', fontsize=8, fontweight='bold', color='#F57F17',
        ha='center', va='center', zorder=15,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF9C4',
                  edgecolor='#F9A825', alpha=0.9))

ax.text((z2_end + z1_end)/2, (WATER_Z + Z1_Z)/2,
        'Z1', fontsize=8, fontweight='bold', color='#1B5E20',
        ha='center', va='center', zorder=15,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#C8E6C9',
                  edgecolor='#2E7D32', alpha=0.9))

# Component labels
ax.text(DECK_START + 1.0, TERRACE_Z + 0.12, 'WOODEN DECK',
        fontsize=8, fontweight='bold', color='#5D4037', ha='center', zorder=15)

ax.text(WALL_POS, WALL_TOP_Z + 0.15, 'SEPARATION\nWALL (RC)',
        fontsize=7, fontweight='bold', color='#424242', ha='center', va='bottom', zorder=15,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5',
                  edgecolor='#616161', alpha=0.9))

ax.text(skimmer_x, WATER_Z + 0.12, 'SK', fontsize=7, fontweight='bold',
        color='#E65100', ha='center', zorder=15)
ax.text(drain_x, SWIM_FLOOR_Z + 0.12, 'BD', fontsize=7, fontweight='bold',
        color='#BF360C', ha='center', zorder=15)
ax.text(pump_x, pump_z + 0.35, 'PUMP', fontsize=7, fontweight='bold',
        color='#BF360C', ha='center', zorder=15,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF3E0',
                  edgecolor='#E65100', alpha=0.9))

ax.text(POND_START + 0.6, TERRACE_Z + 0.12, 'STEPS', fontsize=7,
        fontweight='bold', color='#757575', ha='center', zorder=15)

# Coping stone label
ax.text(POND_START / 2, TERRACE_Z + 0.1, 'coping', fontsize=5,
        color='#999', ha='center', zorder=15)

# Pipe labels
ax.text((regen_start + z3_end)/2, PIPE_Z - 0.1,
        'DISTRIBUTION MANIFOLD\n(perforated pipes under gravel)',
        fontsize=6, color='#BF360C', ha='center', va='top', zorder=15,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#FBE9E7',
                  edgecolor='#E65100', alpha=0.9))

# Gravel layer labels (on the cross-section face)
gravel_label_x = regen_start + 0.15
ax.text(gravel_label_x, (Z3_Z + GRAVEL_COARSE_Z)/2, 'coarse 16-32mm',
        fontsize=5, color='white', fontweight='bold', ha='left', va='center', zorder=7)
ax.text(gravel_label_x, (GRAVEL_COARSE_Z + GRAVEL_MED_Z)/2, 'medium 8-16mm',
        fontsize=5, color='white', fontweight='bold', ha='left', va='center', zorder=7)
ax.text(gravel_label_x, (GRAVEL_MED_Z + GRAVEL_FINE_Z)/2, 'fine 2-8mm',
        fontsize=5, color='white', fontweight='bold', ha='left', va='center', zorder=7)

# Water flow annotation
ax.text(WALL_POS, passage_mid_z - 0.2, 'water flow\nthrough passage',
        fontsize=5, color='#0288D1', ha='center', va='top', zorder=15, fontstyle='italic')

# =============================================================
# 16. LEGEND
# =============================================================

legend_items = [
    mpatches.Patch(facecolor='#0288D1', alpha=0.25, edgecolor='#0277BD', label='Swimming water (2.0m)'),
    mpatches.Patch(facecolor='#43A047', alpha=0.35, edgecolor='#2E7D32', label='Zone 1: Marginal (0-30cm)'),
    mpatches.Patch(facecolor='#FDD835', alpha=0.35, edgecolor='#F9A825', label='Zone 2: Shallow (30-60cm)'),
    mpatches.Patch(facecolor='#4DB6AC', alpha=0.2, edgecolor='#00897B', label='Zone 3: Water above gravel'),
    mpatches.Patch(facecolor='#5D4037', alpha=0.7, edgecolor='#4E342E', label='Gravel: coarse (16-32mm)'),
    mpatches.Patch(facecolor='#795548', alpha=0.65, edgecolor='#5D4037', label='Gravel: medium (8-16mm)'),
    mpatches.Patch(facecolor='#A1887F', alpha=0.6, edgecolor='#795548', label='Gravel: fine (2-8mm)'),
    mpatches.Patch(facecolor='#616161', alpha=0.85, edgecolor='#424242', label='Separation wall (RC)'),
    mpatches.Patch(facecolor='#BDBDBD', alpha=0.8, edgecolor='#9E9E9E', label='Entry steps'),
    mpatches.Patch(facecolor='#A0522D', alpha=0.7, edgecolor='#6D3A1A', label='Wooden deck'),
    mpatches.Patch(facecolor='#B0BEC5', alpha=0.6, edgecolor='#78909C', label='Concrete shell'),
    plt.Line2D([0], [0], color='#E65100', lw=3, label='Supply pipe (pump -> gravel)'),
    plt.Line2D([0], [0], color='#BF360C', lw=2.5, ls='--', label='Return pipe (SK/BD -> pump)'),
    mpatches.Patch(facecolor='#FF6F00', alpha=0.8, edgecolor='#E65100', label='Pump chamber'),
]

ax.legend(handles=legend_items, loc='lower left', fontsize=6, framealpha=0.95,
          edgecolor='#ccc', fancybox=True, ncol=2, title='Legend', title_fontsize=7)

# =============================================================
# 17. TITLE AND AXES
# =============================================================

ax.set_title('Natural Swimming Pond (Schwimmteich) — Cross-Section B-B\u2032\n'
             'Version 2 — Banded Zones (staircase profile: deep near wall, shallow at far end)',
             fontsize=14, fontweight='bold', pad=15)

ax.set_xlabel('Distance from terrace edge (m)', fontsize=10)
ax.set_ylabel('Elevation (m, relative to terrace = 0)', fontsize=10)

ax.set_xlim(DECK_START - 1.5, POND_END_ACTUAL + 2.5)
ax.set_ylim(-3.1, 0.7)
ax.set_aspect('equal')
ax.grid(True, alpha=0.1)

# Secondary y-axis with absolute elevations
ax2 = ax.twinx()
ax2.set_ylim(397.15 - 3.1, 397.15 + 0.7)
ax2.set_ylabel('Elevation (m Bpv)', fontsize=10)

plt.tight_layout()
plt.savefig('schwimmteich_cross_section_v2.png', dpi=200, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print('Saved schwimmteich_cross_section_v2.png')
