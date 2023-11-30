"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730718389"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        self.values = values

    def __str__(self):
        return f"Simpy({self.values})"

    def fill(self, value: float, count: int):
        self.values = []
        while count > 0:
            self.values.append(value)
            count -= 1

    def arange(self, start: float, stop: float, step: float = 1.0):
        assert step != 0.0

        self.values = []
        val: float = start
        while val < stop:
            self.values.append(val)
            val += step

    def sum(self) -> float:
        total: float = 0.0
        for v in self.values:
            total += v
        return total

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
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
