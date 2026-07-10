"""
BloodTest.py

Main application entry point.
"""

import matplotlib.pyplot as plt

from excel_reader import read_excel
from pdf_builder import PdfReport
from plot_data import create_plot


def main():
    """
    Generate the blood test report.
    """

    print("Reading Excel workbook...")

    parameters = read_excel()

    print(f"Found {len(parameters)} parameters.")

    report = PdfReport()

    for parameter in parameters:

        print(f"Generating plot: {parameter.name}")

        fig = create_plot(parameter)

        report.add_page(fig, parameter)

        # Free matplotlib resources
        plt.close(fig)

    report.save()

    print("Done.")
    print("Report saved successfully.")


if __name__ == "__main__":
    main()