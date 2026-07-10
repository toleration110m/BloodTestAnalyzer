"""
config.py

Project configuration.

Modify this file to change application settings.
"""

from pathlib import Path
from reportlab.lib.units import mm

# =============================================================================
# Project Paths
# =============================================================================

# Project root directory
PROJECT_DIR = Path(__file__).resolve().parent

# Input / Output
INPUT_FILE = PROJECT_DIR / "Test.xlsx"
OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "BloodTestReport.pdf"

# =============================================================================
# Excel Configuration
# =============================================================================

SHEET_NAME = "Number"

# =============================================================================
# Patient Information
# =============================================================================

PATIENT_NAME = "John Smith"

# =============================================================================
# PDF Page Settings
# =============================================================================

# Mobile-friendly page size (Portrait)
PAGE_WIDTH = 90 * mm
PAGE_HEIGHT = 170 * mm

# Margins
LEFT_MARGIN = 6 * mm
RIGHT_MARGIN = 6 * mm
TOP_MARGIN = 6 * mm
BOTTOM_MARGIN = 6 * mm

# Header / Footer
HEADER_HEIGHT = 12 * mm
FOOTER_HEIGHT = 8 * mm

# =============================================================================
# Plot Area
# =============================================================================

PLOT_WIDTH = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN

PLOT_HEIGHT = (
    PAGE_HEIGHT
    - TOP_MARGIN
    - BOTTOM_MARGIN
    - HEADER_HEIGHT
    - FOOTER_HEIGHT
)

# =============================================================================
# Fonts
# =============================================================================

HEADER_FONT = "Helvetica-Bold"
BODY_FONT = "Helvetica"
FOOTER_FONT = "Helvetica"

HEADER_FONT_SIZE = 12
BODY_FONT_SIZE = 10
FOOTER_FONT_SIZE = 9

# =============================================================================
# Plot Appearance
# =============================================================================

FIGURE_WIDTH = 4.0      # inches
FIGURE_HEIGHT = 6.2     # inches

LINE_WIDTH = 2.0
MARKER_SIZE = 5

GRID_ALPHA = 0.35

LINE_COLOR = "tab:blue"
LIMIT_COLOR = "tab:red"
LIMIT_FILL_COLOR = "#B2F79F"

# =============================================================================
# Output
# =============================================================================

PDF_TITLE = "Blood Test Report"
PDF_AUTHOR = "Blood Test Analyzer"

# =============================================================================
# Miscellaneous
# =============================================================================

DATE_ROTATION = 45
DPI = 300