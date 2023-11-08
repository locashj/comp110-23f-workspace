"""CQ07 - A class to represent a cartesian Point."""

from __future__ import annotations

__author__ = "730718389"


class Point:
    """Point represents a cartesian point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Accepts an x and y value used to initialize the class."""
        self.x = x
        self.y = y

    def scale_by(self, factor: int) -> None:
        """Accepts a multiplying factor that is used to scale the x and y coordinates."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Accepts a multiplying factor and returns a new Point whose x and y coordinates are scaled."""
        return Point(self.x * factor, self.y * factor)
