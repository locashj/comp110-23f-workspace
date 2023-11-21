"""File to define Bear class."""

__author__ = "730718389"


class Bear:
    """Bear class definition."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes the Bear class with an age and hunger score of zero."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Simulates one day by increasing the bear's age and decreasing its hunger score."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Increases the bear's hunger score by the number of fish it has eaten."""
        self.hunger_score += num_fish
