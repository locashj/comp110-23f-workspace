"""Combining two lists into a dictionary."""

__author__ = "730718389"


def zip(keys: list[str], vals: list[int]) -> dict[str, int]:
    """`zip` accepts a list[str], `keys`, and a list[int], `vals`, and creates a dict[str,int] using `keys` as keys, and `vals` as values."""
    res: dict[str, int] = dict()
    if len(keys) != len(vals):
        return res
    for i in range(0, len(keys)):
        res[keys[i]] = vals[i]
    return res
