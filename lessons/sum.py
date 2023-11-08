"""Summing the elements of a list using different loops."""

__author__ = "730718389"


def w_sum(vals: list[float]) -> float:
    """`w_sum` accepts a list of floats `vals` and computes the sum using a while loop."""
    sum: float = 0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """`f_sum` accepts a list of floats `vals` and computes the sum using a for loop."""
    sum: float = 0
    for val in vals:
        sum += val
    return sum


def f_range_sum(vals: list[float]) -> float:
    """`f_range_sum` accepts a list of floats `vals` and computes the sum using a for loop and range() method."""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
