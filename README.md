# DSP + DPS — Novostavba RD Edwards, Jevany

Complete building permit documentation (DSP — Dokumentace pro stavebni povoleni + DPS — Dokumentace pro provadeni stavby) for a new family house in Jevany, Czech Republic.

## Project Details

| | |
|---|---|
| **Project** | Novostavba rodinneho domu (New family house) |
| **Location** | Jevany [533378], k.u. Jevany [659312], parcels 154/10 and 154/16 |
| **Investor** | Bc. Marketa Edwards |
| **Design firm** | LUCERN DREVOSTAVBY s.r.o., Praha 4 - Branik |
| **Construction type** | Timber-frame (drevostavba), LUCERN EKO PLUS system |
| **Lead designer** | Ing. Josef Frydryn |
| **Authorized by** | Ing. Milos Slavik (2026-03-09) |
| **Elevation reference** | +/-0,000 = 397.402 m n. m. (Bpv) |

## Building Summary

Single-storey family house with attached garage on a sloping garden site (1,091 m2).

- **House footprint:** 180.38 m2
- **Usable area:** 142.07 m2 (4 bedrooms, open-plan living/kitchen, 2 bathrooms, utility room)
- **Terrace:** 38.18 m2
- **Garage:** 18.00 m2
- **Site coverage:** 15.67%
- **Remaining green area:** 84.33%

## Repository Structure

```
A. Pruvodni list/                  Cover / introductory report
B. Souhrnna technicka zprava/      Summary technical report
C. Situacni vykresy/               Site plans (C.1-C.4)
D.1. Dokumentace stavebniho objektu/
    D.1.1. Architektonicko stavebni cast/   Architecture (13 drawings)
    D.1.2. Stavebne konstrukcni cast/       Structural engineering
    D.1.3. Pozarni bezpecnost staveb/       Fire safety
    D.1.4. Technika prostredi staveb/
        D.1.4.1. Zdravotne technicke instalace/  Plumbing (5 docs)
        D.1.4.2. Vytapeni/                       Heating (2 docs)
        D.1.4.3. Elektroinstalace/               Electrical (3 docs)
        D.1.4.4. Nucene vetrani/                  Ventilation (2 docs)
E. Dokladova cast/                 Supporting documents
    GEOLOGICKY PRUZKUM/                Geological survey
    PENB/                              Energy performance certificate
    RADON/                             Radon report
_TITULKY/                          Title / cover pages
Documents/                         Analysis, tools, and working notes
    dwg-files/                         Survey plan (DXF/DWG) and tools
```

## Survey Plan & CAD Tools

The geodetic survey plan (`Documents/dwg-files/10225.dxf`) is the primary working file for site design. It contains terrain elevations, parcel boundaries, and existing features in S-JTSK coordinates.

**Tools included:**

- `visualize_dxf.py` — Generic DXF visualizer. Usage: `python visualize_dxf.py [file.dxf]`
- `create_site_plan.py` — Overlays the building footprint on the survey plan (approximate placement based on C.3 dimensions and elevation matching)

## Documents

| Document | Description |
|----------|-------------|
| [Survey Plan Analysis](Documents/Survey%20Plan%20Analysis%20-%2010225.md) | Detailed analysis of the geodetic survey plan |
| [Swimming Pond - Project Design Document](Documents/Swimming%20Pond%20-%20Project%20Design%20Document.md) | Consolidated feasibility, geotechnical assessment, and technical design specification for the swimming pond |
| [CAD Workflow and File Status](Documents/CAD%20Workflow%20and%20File%20Status.md) | CAD file tracking, DXF analysis, coordinate system issues, and project context |
| [Natural Swimming Ponds Reference](Documents/reseach/natural-swimming-ponds-reference.md) | Comprehensive reference guide: design principles, construction, planting, regulations, costs (UK/EU) |
| [Image Generation Prompt](Documents/image-generation-prompt.md) | AI visualization prompt specifications for the house and pond |

## Key Site Data

| Parameter | Value |
|-----------|-------|
| Site area | 1,091 m2 (parcels 154/10 + 154/16) |
| Terrain elevation | 392.7 - 399.6 m ASL |
| Slope | ~7 m fall over ~100 m (S to N) |
| Soil type | F5 ML (low-plasticity silt/clay), stiff consistency |
| Groundwater | ~7 m below ground |
| Soil permeability (kv) | 5.0 x 10-6 m/s |
| Radon index | HIGH |
| Coordinate system | S-JTSK (EPSG:5514) |

## Tools & Services

### Online Viewers

| Tool | URL | Purpose |
|------|-----|---------|
| **Autodesk Viewer** | https://viewer.autodesk.com | Free online viewer for DWG, DXF, and PDF files — no software install required. Upload files to inspect layers, measure geometry, and navigate 2D/3D drawings in the browser. |

### CAD Software

| Tool | Purpose |
|------|---------|
| **AutoCAD** | Industry-standard CAD software. The DWG files originate from AutoCAD (AC1027 / AutoCAD 2013 format). |
| **ODA File Converter** | Free tool from the Open Design Alliance for batch converting between DWG and DXF without an AutoCAD licence. Download from https://www.opendesign.com/guestfiles/oda_file_converter |

### Python Libraries

| Library | Purpose |
|---------|---------|
| **ezdxf** | Read, write, and manipulate DXF files programmatically. Used by `visualize_dxf.py` and `create_site_plan.py`. Install: `pip install ezdxf` |
| **matplotlib** | Plotting and PNG export of DXF visualizations. Install: `pip install matplotlib` |
| **numpy** | Numerical operations for coordinate and geometry processing. Install: `pip install numpy` |

### PDF Processing (optional)

| Library | Purpose |
|---------|---------|
| **pdfplumber** | Extract text and tables from PDF documents. Install: `pip install pdfplumber` |
| **PyPDF2** | PDF merging, splitting, and metadata extraction. Install: `pip install PyPDF2` |
| **PyMuPDF (fitz)** | High-performance PDF rendering and text extraction. Install: `pip install PyMuPDF` |

### Coordinate Systems

| System | Code | Description |
|--------|------|-------------|
| **S-JTSK** | EPSG:5514 | Czech national geodetic coordinate system used in all survey and site plan files |
| **Bpv** | — | Baltic Vertical Datum — elevation reference for all height data |

## Source Files

The original project files are available at:
[Dropbox — DSP + DPS original files](https://www.dropbox.com/scl/fo/dlxxf2gikck120so64mw4/ANBmE9GKqDEZeK-OOHEcK_o?rlkey=yjp06j1fsihprm6xai4ws58ar&e=4&st=s74td683&dl=0)

## Next Steps

1. Obtain remaining DWG files from LUCERN DREVOSTAVBY (see [CAD Workflow](Documents/CAD%20Workflow%20and%20File%20Status.md))
2. Create accurate combined site plan with exact building footprint
3. Design natural swimming pond layout on the DXF base
