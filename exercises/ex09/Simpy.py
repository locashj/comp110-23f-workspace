"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730718389"


class Simpy:
    """Simpy class definition."""

    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """Initializes the Simpy object with a list of values."""
        self.values = values

    def __str__(self) -> str:
        """Produce a string of the Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, value: float, count: int) -> None:
        """Fills the Simpy object's values with `count` number of `value`."""
        self.values = []
        while count > 0:
            self.values.append(value)
            count -= 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the Simpy object's values with a range."""
        assert step != 0.0
        if step < 0:
            assert stop < start
            self.values = []
            val: float = start
            while val > stop:
                self.values.append(val)
                val += step
        else:
            assert start < stop
            self.values = []
            val: float = start
            while val < stop:
                self.values.append(val)
                val += step

    def sum(self) -> float:
        """Computes the sum of the values list."""
        total: float = 0.0
        for v in self.values:
            total += v
        return total

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Allow either two Simpy objects or one Simpy object and a float to be added together."""
        values: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                values.append(self.values[i] + rhs.values[i])
        elif isinstance(rhs, float):
            for v in self.values:
                values.append(v + rhs)
        return Simpy(values)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Allow one Simpy object to be raised by the power of either another Simpy object or a float."""
        values: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                values.append(self.values[i] ** rhs.values[i])
        elif isinstance(rhs, float):
            for v in self.values:
                values.append(v ** rhs)
        return Simpy(values)

    def __eq__(self, other: Union[Simpy, float]) -> list[bool]:
        """Allow one Simpy object to be compared to either another Simpy object or a float for equality."""
        res = []
        if isinstance(other, Simpy):
            assert len(self.values) == len(other.values)
            for i in range(0, len(self.values)):
                res.append(self.values[i] == other.values[i])
        elif isinstance(other, float):
            for v in self.values:
                res.append(v == other)
        return res

    def __gt__(self, other: Union[Simpy, float]) -> list[bool]:
        """Allow one Simpy object is greater than either another Simpy object or a float."""
        res = []
        if isinstance(other, Simpy):
            assert len(self.values) == len(other.values)
            for i in range(0, len(self.values)):
                res.append(self.values[i] > other.values[i])
        elif isinstance(other, float):
            for v in self.values:
                res.append(v > other)
        return res

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Given an int, return the item in self.values at that index. When given a `list[bool]`, returns a new Simpy whose values are masked using that list."""
        if isinstance(rhs, int):
            assert 0 <= rhs < len(self.values)
            return self.values[rhs]
        else:
            assert len(rhs) == len(self.values)
            new_values: list[float] = []
            for i in range(0, len(self.values)):
                if rhs[i]:
                    new_values.append(self.values[i])
            return Simpy(new_values)
