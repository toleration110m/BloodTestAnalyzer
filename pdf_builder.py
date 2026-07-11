"""
pdf_builder.py

Create the PDF report.
"""

from io import BytesIO

from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from config import (
    BODY_FONT,
    BODY_FONT_SIZE,
    BOTTOM_MARGIN,
    FOOTER_FONT,
    FOOTER_FONT_SIZE,
    FOOTER_HEIGHT,
    HEADER_FONT,
    HEADER_FONT_SIZE,
    HEADER_HEIGHT,
    LEFT_MARGIN,
    OUTPUT_FILE,
    PAGE_HEIGHT,
    PAGE_WIDTH,
    PATIENT_NAME,
    RIGHT_MARGIN,
    TOP_MARGIN,
)


class PdfReport:
    """
    Generate the PDF report.
    """

    def __init__(self, output_file=OUTPUT_FILE):

        self.canvas = canvas.Canvas(
            str(output_file),
            pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        )

        self.page_number = 0

    # ------------------------------------------------------------------

    def add_page(self, figure, parameter):

        self.page_number += 1

        self._draw_header(parameter.name)
        self._draw_plot(figure)
        self._draw_footer()

        self.canvas.showPage()

    # ------------------------------------------------------------------

    def save(self):

        self.canvas.save()

    # ------------------------------------------------------------------

    def _draw_header(self, parameter_name):

        y = PAGE_HEIGHT - TOP_MARGIN

        #
        # Patient
        #
        self.canvas.setFont(
            HEADER_FONT,
            HEADER_FONT_SIZE,
        )

        self.canvas.drawString(
            LEFT_MARGIN,
            y,
            f"Patient: {PATIENT_NAME}",
        )

        #
        # Parameter
        #
        self.canvas.setFont(
            BODY_FONT,
            BODY_FONT_SIZE,
        )

        self.canvas.drawString(
            LEFT_MARGIN,
            y - HEADER_HEIGHT + 4,
            f"Parameter: {parameter_name}",
        )

        #
        # Separator line
        #
        line_y = PAGE_HEIGHT - TOP_MARGIN - HEADER_HEIGHT

        self.canvas.line(
            LEFT_MARGIN,
            line_y,
            PAGE_WIDTH - RIGHT_MARGIN,
            line_y,
        )

    # ------------------------------------------------------------------

    def _draw_plot(self, figure):

        image_buffer = BytesIO()

        figure.savefig(
            image_buffer,
            format="png",
            dpi=300,
            bbox_inches="tight",
        )

        image_buffer.seek(0)

        image = ImageReader(image_buffer)

        img_width, img_height = image.getSize()

        # Available plot area
        plot_width = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
        plot_height = (
            PAGE_HEIGHT
            - TOP_MARGIN
            - BOTTOM_MARGIN
            - HEADER_HEIGHT
            - FOOTER_HEIGHT
        )

        #
        # Rotate the image by 90°.
        # After rotation, width and height are swapped.
        #
        scale = min(
            plot_width / img_height,
            plot_height / img_width,
        )

        draw_width = img_height * scale
        draw_height = img_width * scale

        x = LEFT_MARGIN + (plot_width - draw_width) / 2
        y = BOTTOM_MARGIN + FOOTER_HEIGHT + (plot_height - draw_height) / 2

        self.canvas.saveState()

        #
        # Move origin to lower-left corner of rotated image
        #
        self.canvas.translate(x, y)

        #
        # Rotate counter-clockwise
        #
        self.canvas.rotate(90)

        #
        # Draw image
        #
        self.canvas.drawImage(
            image,
            0,
            -draw_width,
            width=draw_height,
            height=draw_width,
            mask="auto",
        )

        self.canvas.restoreState()

        image_buffer.close()

    # ------------------------------------------------------------------

    def _draw_footer(self):

        #
        # Separator
        #
        line_y = BOTTOM_MARGIN + FOOTER_HEIGHT

        self.canvas.line(
            LEFT_MARGIN,
            line_y,
            PAGE_WIDTH - RIGHT_MARGIN,
            line_y,
        )

        #
        # Page number
        #
        self.canvas.setFont(
            FOOTER_FONT,
            FOOTER_FONT_SIZE,
        )

        self.canvas.drawCentredString(
            PAGE_WIDTH / 2,
            BOTTOM_MARGIN / 2,
            f"Page {self.page_number}",
        )