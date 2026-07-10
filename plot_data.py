"""
plot_data.py

Generate trend charts for blood test parameters.
"""

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from config import (
    DATE_ROTATION,
    FIGURE_HEIGHT,
    FIGURE_WIDTH,
    GRID_ALPHA,
    LINE_COLOR,
    LINE_WIDTH,
    LIMIT_FILL_COLOR,
    MARKER_SIZE,
)

from models import ParameterData


def create_plot(parameter: ParameterData):
    """
    Create a trend chart for a blood test parameter.

    Parameters
    ----------
    parameter : ParameterData

    Returns
    -------
    matplotlib.figure.Figure
    """

    fig, ax = plt.subplots(
        figsize=(FIGURE_WIDTH, FIGURE_HEIGHT),
        constrained_layout=True,
    )

    #
    # Plot reference interval
    #
    ax.fill_between(
        parameter.dates,
        parameter.lower_limits,
        parameter.upper_limits,
        color=LIMIT_FILL_COLOR,
        alpha=0.35,
        label="Reference Range",
    )

    #
    # Plot measured values
    #
    ax.plot(
        parameter.dates,
        parameter.values,
        color=LINE_COLOR,
        linewidth=LINE_WIDTH,
        marker="o",
        markersize=MARKER_SIZE,
    )

    #
    # Titles
    #
    ax.set_title(parameter.name, fontsize=14, weight="bold")

    #
    # Axis labels
    #
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")

    #
    # Grid
    #
    ax.grid(True, alpha=GRID_ALPHA)

    #
    # Date formatting
    #
    try:
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator)

        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)

    except Exception:
        pass

    plt.setp(
        ax.get_xticklabels(),
        rotation=DATE_ROTATION,
        ha="right",
    )

    #
    # Small margin around data
    #
    ax.margins(x=0.03, y=0.08)

    return fig