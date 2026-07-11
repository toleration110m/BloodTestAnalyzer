"""
plot_data.py

Generate blood test trend charts.
"""

from __future__ import annotations

from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

from config import (
    PLOT_YEARS,
    LINE_COLOR,
    LINE_WIDTH,
    LIMIT_FILL_COLOR,
    MARKER_SIZE,
    GRID_ALPHA,
)

from models import ParameterData


# =============================================================================
# Helper functions
# =============================================================================

def jalali_to_float(date_value) -> float:
    """
    Convert a Jalali date to a fractional year.

    Supported formats
    -----------------
    "06/06/1403"
    "6/6/1403"

    Returns
    -------
    float
        Example:
            1403.00
            1403.50
            1403.92
    """

    if isinstance(date_value, str):

        day, month, year = map(int, date_value.strip().split("/"))

        return year + ((month - 1) + (day - 1) / 31.0) / 12.0

    raise TypeError(
        f"Unsupported date type: {type(date_value)}"
    )


# =============================================================================

def filter_last_years(parameter: ParameterData):
    """
    Filter data according to PLOT_YEARS.
    """

    x = [jalali_to_float(d) for d in parameter.dates]

    if PLOT_YEARS is None:
        index = list(range(len(x)))
    else:

        latest_year = int(max(x))
        first_year = latest_year - PLOT_YEARS + 1

        index = [
            i
            for i, year in enumerate(x)
            if year >= first_year
        ]

    return (
        [x[i] for i in index],
        [parameter.values[i] for i in index],
        [parameter.lower_limits[i] for i in index],
        [parameter.upper_limits[i] for i in index],
    )


# =============================================================================

def create_plot(
    parameter: ParameterData,
    figure_width: float,
    figure_height: float,
    ):
    """
    Create a matplotlib Figure for one blood parameter.
    """

    x, values, lower, upper = filter_last_years(parameter)

    #
    # Landscape figure
    #
    fig = plt.figure(
    figsize=(figure_width, figure_height),
    dpi=300,
    )

    ax = fig.add_subplot(111)

    #
    # Reference interval
    #
    ax.fill_between(
        x,
        lower,
        upper,
        color=LIMIT_FILL_COLOR,
        alpha=0.35,
        zorder=1,
    )

    #
    # Trend line
    #
    ax.plot(
        x,
        values,
        color=LINE_COLOR,
        linewidth=LINE_WIDTH,
        zorder=2,
    )

    #
    # Previous measurements
    #
    if len(values) > 1:

        ax.scatter(
            x[:-1],
            values[:-1],
            s=MARKER_SIZE ** 2,
            color=LINE_COLOR,
            zorder=3,
        )

    #
    # Latest measurement
    #
    ax.scatter(
        x[-1],
        values[-1],
        s=(MARKER_SIZE + 4) ** 2,
        color=LINE_COLOR,
        edgecolors="black",
        linewidths=0.8,
        zorder=4,
    )

    #
    # Title
    #
    ax.set_title(
        parameter.name,
        fontsize=16,
        weight="bold",
        pad=12,
    )

    #
    # Dynamic Y-axis
    #
    ymin = min(min(values), min(lower))
    ymax = max(max(values), max(upper))

    margin = (ymax - ymin) * 0.10

    if margin == 0:
        margin = 1

    ax.set_ylim(
        ymin - margin,
        ymax + margin,
    )

    #
    # X-axis
    #
    first_year = int(min(x))
    last_year = int(max(x))

    ax.set_xlim(
        first_year,
        last_year + 1,
    )

    years = list(range(first_year, last_year + 1))

    ax.set_xticks(years)
    ax.set_xticklabels(
        [str(y) for y in years],
        fontsize=9,
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
        alpha=GRID_ALPHA,
    )

    ax.grid(
        which="minor",
        linestyle=":",
        linewidth=0.5,
        alpha=GRID_ALPHA * 0.8,
    )

    #
    # Remove axis labels
    #
    ax.set_xlabel("")
    ax.set_ylabel("")

    #
    # Tight margins
    #
    fig.subplots_adjust(
        left=0.08,
        right=0.985,
        top=0.88,
        bottom=0.15,
    )

    return fig