"""Visualize any DXF file. Usage: python visualize_dxf.py [file.dxf]"""
import sys
import os
import ezdxf
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import LineCollection

# --- Input / output paths ---
if len(sys.argv) > 1:
    dxf_path = sys.argv[1]
else:
    # Default: first .dxf in same directory as script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dxf_files = [f for f in os.listdir(script_dir) if f.lower().endswith(".dxf")]
    if not dxf_files:
        sys.exit("No .dxf file found. Pass one as an argument.")
    dxf_path = os.path.join(script_dir, dxf_files[0])

dxf_name = os.path.basename(dxf_path)
out_path = os.path.splitext(dxf_path)[0] + "_visualization.png"

doc = ezdxf.readfile(dxf_path)
msp = doc.modelspace()

# --- Auto-generate distinct colors per layer ---
PALETTE = [
    '#333333', '#2196F3', '#4CAF50', '#FF9800', '#9C27B0',
    '#795548', '#E91E63', '#00BCD4', '#FF5722', '#8BC34A',
    '#CDDC39', '#607D8B', '#3F51B5', '#009688', '#FFC107',
    '#673AB7', '#F44336', '#03A9F4', '#FFEB3B', '#9E9E9E',
]

layers_used = sorted({e.dxf.get("layer", "0") for e in msp})
layer_colors = {layer: PALETTE[i % len(PALETTE)] for i, layer in enumerate(layers_used)}

def get_color(entity):
    return layer_colors.get(entity.dxf.get("layer", "0"), '#666666')

# --- Figure setup ---
fig, ax = plt.subplots(1, 1, figsize=(16, 16))

# Draw LINEs
lines, line_colors = [], []
for e in msp.query("LINE"):
    lines.append([(e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)])
    line_colors.append(get_color(e))
if lines:
    ax.add_collection(LineCollection(lines, colors=line_colors, linewidths=0.5))

# Draw LWPOLYLINEs
for e in msp.query("LWPOLYLINE"):
    pts = list(e.get_points(format="xy"))
    if e.closed:
        pts.append(pts[0])
    if len(pts) >= 2:
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=get_color(e), linewidth=0.7)

# Draw CIRCLEs
for e in msp.query("CIRCLE"):
    c, r = e.dxf.center, e.dxf.radius
    ax.add_patch(plt.Circle((c.x, c.y), r, fill=False, edgecolor=get_color(e), linewidth=0.5))

# Draw ARCs
for e in msp.query("ARC"):
    c, r = e.dxf.center, e.dxf.radius
    ax.add_patch(mpatches.Arc(
        (c.x, c.y), 2*r, 2*r, angle=0,
        theta1=e.dxf.start_angle, theta2=e.dxf.end_angle,
        edgecolor=get_color(e), linewidth=0.5,
    ))

# Draw TEXT
for e in msp.query("TEXT"):
    pos = e.dxf.insert
    fontsize = max(3, min(e.dxf.height * 2, 8))
    ax.text(pos.x, pos.y, e.dxf.text, fontsize=fontsize, color=get_color(e),
            rotation=e.dxf.get("rotation", 0), ha='left', va='bottom')

# Draw MTEXT
for e in msp.query("MTEXT"):
    pos = e.dxf.insert
    fontsize = max(3, min(e.dxf.char_height * 2, 8))
    ax.text(pos.x, pos.y, e.text, fontsize=fontsize, color=get_color(e),
            rotation=e.dxf.get("rotation", 0), ha='left', va='bottom')

# Draw POINTs
for e in msp.query("POINT"):
    loc = e.dxf.location
    ax.plot(loc.x, loc.y, 'k.', markersize=3)

# Draw INSERTs (block references) as markers
for e in msp.query("INSERT"):
    pos = e.dxf.insert
    ax.plot(pos.x, pos.y, '+', color=get_color(e), markersize=3, markeredgewidth=0.5)

# --- Formatting ---
ax.set_aspect('equal')
ax.autoscale()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title(dxf_name, fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.2, linewidth=0.3)
ax.tick_params(labelsize=7)

# Legend (only layers that were actually drawn)
legend_patches = [mpatches.Patch(color=c, label=f'Layer {l}') for l, c in layer_colors.items()]
if legend_patches:
    ax.legend(handles=legend_patches, loc='upper left', fontsize=7, framealpha=0.8)

plt.tight_layout()
plt.savefig(out_path, dpi=200, bbox_inches='tight')
print(f"Saved to {out_path}")
plt.close()
