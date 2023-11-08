"""Test my zip function."""

__author__ = "730718389"


from lessons.zip import zip


def test_lists_of_different_lengths() -> None:
    """Tests `zip` function by passing two lists of different lengths."""
    assert zip([], [1, 2, 3]) == {}


def test_empty_lists() -> None:
    """Tests `zip` function by passing two empty lists."""
    assert zip([], []) == {}


def test_valid_input() -> None:
    """Tests `zip` by passing two valid input lists."""
    res: dict[str, int] = zip(["Hello", "World"], [1, 2])
    assert len(res) == 2
    assert "Hello" in res
    assert "World" in res
