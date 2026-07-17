"""
BloodTest.py

Main entry point for the Blood Test Analyzer.
"""

from pathlib import Path
import os
import tkinter as tk
from tkinter import filedialog

from excel_reader import read_excel
from pdf_builder import PdfReport


def select_input_file() -> Path | None:
    """
    Show a file selection dialog and return the selected Excel file.
    """

    root = tk.Tk()
    root.withdraw()

    filename = filedialog.askopenfilename(
        title="Select Blood Test Excel File",
        filetypes=[
            ("Excel Files", "*.xlsx *.xlsm"),
            ("All Files", "*.*"),
        ],
    )
    root.destroy()

    if not filename:
        return None

    return Path(filename)


def main() -> None:
    """
    Generate the blood test report.
    """

    input_file = select_input_file()

    if input_file is None:
        print("No file selected.")
        return
    output_file = input_file.with_name(
        f"{input_file.stem}_Report.pdf"
    )
    
    report_title = input_file.stem

    print("Reading Excel file...")

    parameters = read_excel(input_file)

    if not parameters:
        raise RuntimeError(
            "No blood test parameters found."
        )

    print(f"{len(parameters)} parameters loaded.\n")

    report = PdfReport(
        output_file=output_file,
        report_title=report_title,
    )

    total = len(parameters)

    for index, parameter in enumerate(parameters, start=1):

        print(
            f"[{index:02d}/{total:02d}] "
            f"Generating {parameter.name}"
        )

        report.add_page(parameter)

    report.save()

    print()
    print(f"Report saved to:\n{output_file}")

    #
    # Open the generated PDF using the default viewer.
    #
    try:
        os.startfile(output_file)
    except Exception:
        pass


if __name__ == "__main__":
    main()