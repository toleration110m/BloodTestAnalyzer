"""
BloodTest.py

Main entry point for the Blood Test Analyzer.
"""

from config import INPUT_FILE, OUTPUT_FILE
from excel_reader import read_excel
from pdf_builder import PdfReport


def main() -> None:
    """
    Generate the blood test PDF report.
    """

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input Excel file not found:\n{INPUT_FILE}"
        )

    print("Reading Excel file...")

    parameters = read_excel(INPUT_FILE)

    if not parameters:
        raise RuntimeError(
            "No blood test parameters found."
        )

    print(f"{len(parameters)} parameters loaded.\n")

    report = PdfReport(OUTPUT_FILE)

    total = len(parameters)

    for index, parameter in enumerate(parameters, start=1):

        print(
            f"[{index:02d}/{total:02d}] "
            f"Generating {parameter.name}"
        )

        report.add_page(parameter)

    report.save()

    print()
    print(f"Report saved to:\n{OUTPUT_FILE}")


if __name__ == "__main__":
    main()