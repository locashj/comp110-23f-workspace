"""File to define Fish class."""

__author__ = "730718389"


class Fish:
    """Fish class definition."""

    age: int
    
    def __init__(self):
        """Initializes the fish with an age of zero."""
        self.age = 0
    
    def one_day(self):
        """Simulates one day by increasing the fish's age."""
        self.age += 1
