"""
models.py

Data models used by the Blood Test Analyzer.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ParameterData:
    """
    Represents a single blood test parameter and its historical values.
    """

    name: str

    dates: list[Any] = field(default_factory=list)

    values: list[float] = field(default_factory=list)

    lower_limits: list[float] = field(default_factory=list)

    upper_limits: list[float] = field(default_factory=list)

    @property
    def count(self) -> int:
        """Return the number of available measurements."""
        return len(self.values)

    @property
    def latest_value(self) -> float | None:
        """Return the most recent measurement."""
        if self.values:
            return self.values[-1]
        return None

    @property
    def latest_date(self) -> Any | None:
        """Return the date of the most recent measurement."""
        if self.dates:
            return self.dates[-1]
        return None

    @property
    def latest_lower_limit(self) -> float | None:
        """Return the latest lower reference limit."""
        if self.lower_limits:
            return self.lower_limits[-1]
        return None

    @property
    def latest_upper_limit(self) -> float | None:
        """Return the latest upper reference limit."""
        if self.upper_limits:
            return self.upper_limits[-1]
        return None