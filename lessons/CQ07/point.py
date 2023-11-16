"""CQ07 - A class to represent a cartesian Point."""

from __future__ import annotations

__author__ = "730718389"


class Point:
    """Point represents a cartesian point."""
    x: float
    y: float

    def __init__(self, x: float = 0.0, y: float = 0.0):
        """Accepts an x and y value used to initialize the class."""
        self.x = x
        self.y = y

    def scale_by(self, factor: int | float) -> None:
        """Accepts a multiplying factor that is used to scale the x and y coordinates."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int | float) -> Point:
        """Accepts a multiplying factor and returns a new Point whose x and y coordinates are scaled."""
        return Point(self.x * factor, self.y * factor)

    def __str__(self) -> str:
        """`__str__` returns the string representation of the Point."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """`__mul__` returns a new point scaled by `factor`."""
        return self.scale(factor)

    def __add__(self, value: int | float) -> Point:
        """`__add__` returns a new point whose x and y values are increased by `factor`."""
        return Point(self.x + value, self.y + value)
