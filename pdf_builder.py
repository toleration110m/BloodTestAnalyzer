"""
pdf_builder.py

Generate the PDF report.
One blood parameter is plotted per page.
"""

from __future__ import annotations

from io import BytesIO

from PIL import Image

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from config import (
    PAGE_WIDTH,
    PAGE_HEIGHT,
    LEFT_MARGIN,
    RIGHT_MARGIN,
    TOP_MARGIN,
    BOTTOM_MARGIN,
    HEADER_HEIGHT,
    HEADER_FONT,
    HEADER_FONT_SIZE,
    PATIENT_NAME,
    PDF_TITLE,
    PDF_AUTHOR,
    OUTPUT_FILE,
    DPI,
)

from plot_data import create_plot


POINTS_PER_INCH = 72.0


class PdfReport:
    """
    Create the blood test report PDF.
    """

    def __init__(self, output_file=OUTPUT_FILE):

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.canvas = canvas.Canvas(
            str(output_file),
            pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        )

        self.canvas.setTitle(PDF_TITLE)
        self.canvas.setAuthor(PDF_AUTHOR)

        self.page_number = 0

    # ------------------------------------------------------------------
    # Geometry
    # ------------------------------------------------------------------

    @property
    def plot_width(self) -> float:
        return PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN

    @property
    def plot_height(self) -> float:
        return (
            PAGE_HEIGHT
            - TOP_MARGIN
            - BOTTOM_MARGIN
            - HEADER_HEIGHT
        )

    @property
    def figure_width(self) -> float:
        """
        Width BEFORE rotation.

        Because the chart will be rotated by 90°,
        width and height are intentionally swapped.
        """
        return self.plot_height / POINTS_PER_INCH

    @property
    def figure_height(self) -> float:
        """
        Height BEFORE rotation.
        """
        return self.plot_width / POINTS_PER_INCH

    # ------------------------------------------------------------------
    # Header
    # ------------------------------------------------------------------

    def _draw_header(self):

        top = PAGE_HEIGHT - TOP_MARGIN

        self.canvas.setFont(
            HEADER_FONT,
            HEADER_FONT_SIZE,
        )

        #
        # Patient name
        #
        self.canvas.drawString(
            LEFT_MARGIN,
            top,
            PATIENT_NAME,
        )

        #
        # Page number
        #
        self.canvas.drawRightString(
            PAGE_WIDTH - RIGHT_MARGIN,
            top,
            f"Page {self.page_number}",
        )

        #
        # Separator line
        #
        y = top - 5

        self.canvas.setLineWidth(1)

        self.canvas.setStrokeGray(0.55)

        self.canvas.line(
            LEFT_MARGIN,
            y,
            PAGE_WIDTH - RIGHT_MARGIN,
            y,
        )

        self.canvas.setStrokeGray(0)

    # ------------------------------------------------------------------
    # Plot
    # ------------------------------------------------------------------

    def _draw_plot(self, parameter):
        """
        Draw one rotated chart on the current PDF page.
        """

        #
        # Create matplotlib figure
        #
        fig = create_plot(
            parameter,
            self.figure_width,
            self.figure_height,
        )

        #
        # Render figure
        #
        FigureCanvasAgg(fig)

        #
        # Save to PNG buffer
        #
        png_buffer = BytesIO()

        fig.savefig(
            png_buffer,
            format="png",
            dpi=DPI,
            facecolor="white",
        )

        plt.close(fig)

        png_buffer.seek(0)

        #
        # Rotate 90° clockwise
        #
        image = Image.open(png_buffer)

        image = image.rotate(
            90,
            expand=True,
        )

        rotated_buffer = BytesIO()

        image.save(
            rotated_buffer,
            format="PNG",
        )

        rotated_buffer.seek(0)

        #
        # Available drawing area
        #
        x = LEFT_MARGIN
        y = BOTTOM_MARGIN

        #
        # Draw rotated image
        #
        self.canvas.drawImage(
            ImageReader(rotated_buffer),
            x,
            y,
            width=self.plot_width,
            height=self.plot_height,
            preserveAspectRatio=False,
            mask="auto",
        )

        #
        # Cleanup
        #
        png_buffer.close()
        rotated_buffer.close()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def add_page(self, parameter):
        """
        Add one report page.
        """

        self.page_number += 1

        self._draw_header()

        self._draw_plot(parameter)

        self.canvas.showPage()

    # ------------------------------------------------------------------

    def save(self):
        """
        Save the PDF document.
        """

        self.canvas.save()