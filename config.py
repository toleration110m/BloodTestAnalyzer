"""
config.py

Project configuration.

Modify this file to change application settings.
"""

from reportlab.lib.units import mm

# =============================================================================
# Excel Configuration
# =============================================================================

SHEET_NAME = "Number"

# Excel layout:
#
# A : Date
# B : Location
# C : Doctor
# D : Lower Limit
# E : Upper Limit
# F : Parameter
#
# Then repeats every three columns:
#
# G : Lower Limit
# H : Upper Limit
# I : Parameter
#

FIRST_PARAMETER_COLUMN = 6
PARAMETER_COLUMN_STEP = 3

# =============================================================================
# PDF Page Settings
# =============================================================================

# Optimized for viewing on a typical mobile phone.

PAGE_WIDTH = 90 * mm
PAGE_HEIGHT = 170 * mm

LEFT_MARGIN = 6 * mm
RIGHT_MARGIN = 6 * mm

TOP_MARGIN = 6 * mm
BOTTOM_MARGIN = 6 * mm

HEADER_HEIGHT = 12 * mm

# =============================================================================
# Plot Style
# =============================================================================

LINE_WIDTH = 2.0

MARKER_SIZE = 5

GRID_ALPHA = 0.35

LINE_COLOR = "tab:blue"

LIMIT_FILL_COLOR = "#6AFF40"

# =============================================================================
# Time Axis
# =============================================================================

# Number of recent years to display.
#
# Example:
#     5  -> last five years
#     None -> display all available history

PLOT_YEARS = 10

# Major grid every year

MAJOR_YEAR_STEP = 1

# Minor grid every three months

MINOR_MONTH_STEP = 3

# =============================================================================
# Fonts
# =============================================================================

HEADER_FONT = "Helvetica-Bold"

BODY_FONT = "Helvetica"

HEADER_FONT_SIZE = 12

BODY_FONT_SIZE = 10

# =============================================================================
# PDF Metadata
# =============================================================================

PDF_TITLE = "Blood Test Report"

PDF_AUTHOR = "Blood Test Analyzer"

# =============================================================================
# Rendering
# =============================================================================

DPI = 300