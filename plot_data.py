"""
plot_data.py

Generate trend charts for blood test parameters.
"""

from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

from config import (
    FIGURE_WIDTH,
    FIGURE_HEIGHT,
    GRID_ALPHA,
    LINE_COLOR,
    LINE_WIDTH,
    LIMIT_FILL_COLOR,
    MARKER_SIZE,
    PLOT_YEARS,
)

from models import ParameterData


# -----------------------------------------------------------------------------


def _date_to_float(date_string: str) -> float:
    """
    Convert Jalali date string (dd/mm/yyyy) to fractional year.

    Example
    -------
    15/04/1403 -> 1403.29
    """

    day, month, year = map(int, date_string.split("/"))

    return year + ((month - 1) * 31 + day - 1) / 372.0


# -----------------------------------------------------------------------------


def create_plot(parameter: ParameterData):
    """
    Create a trend chart.
    """

    #
    # Convert dates to numeric axis
    #

    x = [_date_to_float(d) for d in parameter.dates]

    #
    # Keep only recent years if requested
    #

    if PLOT_YEARS is not None:

        latest_year = int(max(x))

        minimum_year = latest_year - PLOT_YEARS + 1

        indices = [
            i
            for i, value in enumerate(x)
            if value >= minimum_year
        ]

        x = [x[i] for i in indices]
        values = [parameter.values[i] for i in indices]
        lower = [parameter.lower_limits[i] for i in indices]
        upper = [parameter.upper_limits[i] for i in indices]

    else:

        values = parameter.values
        lower = parameter.lower_limits
        upper = parameter.upper_limits

    #
    # Figure
    #

    fig, ax = plt.subplots(
        figsize=(FIGURE_WIDTH, FIGURE_HEIGHT),
        constrained_layout=True,
    )

    #
    # Reference interval
    #

    ax.fill_between(
        x,
        lower,
        upper,
        color=LIMIT_FILL_COLOR,
        alpha=0.35,
    )

    #
    # Trend
    #

    ax.plot(
        x,
        values,
        color=LINE_COLOR,
        linewidth=LINE_WIDTH,
        marker="o",
        markersize=MARKER_SIZE,
    )

    #
    # Title
    #

    ax.set_title(
        parameter.name,
        fontsize=14,
        weight="bold",
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Value")

    #
    # Major ticks (every year)
    #

    first_year = int(min(x))
    last_year = int(max(x))

    major_ticks = list(range(first_year, last_year + 1))

    ax.set_xticks(major_ticks)

    ax.set_xticklabels(
        [str(year) for year in major_ticks]
    )

    #
    # Minor ticks every 3 months
    #

    ax.xaxis.set_minor_locator(
        MultipleLocator(0.25)
    )

    #
    # Grid
    #

    ax.grid(
        which="major",
        linewidth=0.8,
        alpha=0.6,
    )

    ax.grid(
        which="minor",
        linewidth=0.3,
        linestyle=":",
        alpha=0.4,
    )

    #
    # Margins
    #

    ax.margins(
        x=0.02,
        y=0.08,
    )

    return fig