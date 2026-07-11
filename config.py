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

PROJECT_DIR = Path(__file__).resolve().parent

INPUT_FILE = PROJECT_DIR / "Test.xlsx"

OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "BloodTestReport.pdf"

# =============================================================================
# Excel Configuration
# =============================================================================

SHEET_NAME = "Number"

FIRST_PARAMETER_COLUMN = 6
PARAMETER_COLUMN_STEP = 3

# =============================================================================
# Patient Information
# =============================================================================

PATIENT_NAME = "John Smith"

# =============================================================================
# PDF Page Settings
# =============================================================================

PAGE_WIDTH = 90 * mm
PAGE_HEIGHT = 170 * mm

LEFT_MARGIN = 6 * mm
RIGHT_MARGIN = 6 * mm
TOP_MARGIN = 6 * mm
BOTTOM_MARGIN = 6 * mm

HEADER_HEIGHT = 12 * mm
FOOTER_HEIGHT = 8 * mm

# =============================================================================
# Plot Area
# =============================================================================

FIGURE_WIDTH = 4.0       # inches (landscape)
FIGURE_HEIGHT = 6.2      # inches

LINE_WIDTH = 2.0
MARKER_SIZE = 5

GRID_ALPHA = 0.35

LINE_COLOR = "tab:blue"
LIMIT_FILL_COLOR = "#D8F5D0"

# =============================================================================
# Time Axis
# =============================================================================

# Number of recent years to display.
# None = display all available history.
PLOT_YEARS = 5

# Major grid every year
MAJOR_YEAR_STEP = 1

# Minor grid every 3 months
MINOR_MONTH_STEP = 3

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
# Output
# =============================================================================

PDF_TITLE = "Blood Test Report"
PDF_AUTHOR = "Blood Test Analyzer"

# =============================================================================
# Miscellaneous
# =============================================================================

DPI = 300