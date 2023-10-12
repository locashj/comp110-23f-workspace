"""EX04 - List utility methods."""

__author__ = "730718389"

def all(numbers: list[int], match: int) -> bool:
    """`all` accepts a list of integers `nubmers` and an integer `match` and returns `True` if all items in the list are equivalent to `match`"""
    idx: int = 0
    while idx < len(numbers):
        if numbers[idx] != match:
            return False
        idx += 1
    return True


def max(numbers: list[int]) -> int:
    """`max` accepts a list of integers `numbers` and returns the integer in the list with the greatest value"""
    if len(numbers) == 0:
        return ValueError("max() arg is an empty List")
    current_max: int = numbers[0]
    idx: int = 1
    while idx < len(numbers):
        if numbers[idx] > current_max:
            current_max = numbers[idx]
        idx += 1
    return current_max


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """`is_equal` accepts two lists of integers and returns True if they are of the same length and have identical values at each index."""
    if len(l1) != len(l2):
        return False
    idx: int = 0
    while idx < len(l1):
        if l1[idx] != l2[idx]:
            return False
        idx += 1
    return True
