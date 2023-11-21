"""File to define River class."""

__author__ = "730718389"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River class definition."""

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks the ages of both the fish and the bears, and removes them from the river if they are too old."""
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish

        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears

    def bears_eating(self) -> None:
        """Simulates bears eating fish from the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self) -> None:
        """Checks for starving bears and removes them if they have starved to death."""
        not_starving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                not_starving_bears.append(bear)
        self.bears = not_starving_bears

    def remove_fish(self, amount: int) -> None:
        """Removes `amount` of fish from the river."""
        while amount > 0:
            self.fish.pop(0)
            amount -= 1

    def repopulate_fish(self) -> None:
        """Increases the fish population such that for every two fish, four new ones will be added to the river."""
        new_fish_count = (len(self.fish) // 2) * 4
        while new_fish_count > 0:
            self.fish.append(Fish())
            new_fish_count -= 1
    
    def repopulate_bears(self) -> None:
        """Increases the bear population such that for every two bears, one new one will be added to the river."""
        new_bear_count = len(self.bears) // 2
        while new_bear_count > 0:
            self.bears.append(Bear())
            new_bear_count -= 1
    
    def view_river(self) -> None:
        """Prints the current state of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self) -> None:
        """Simulates one river week by progressing the day seven times."""
        day = 0
        while day < 7:
            self.one_river_day()
            day += 1
            