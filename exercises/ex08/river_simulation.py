"""Simulate life in a river."""

__author__ = "730718389"


from exercises.ex08.river import River

my_river = River(10, 2)
my_river.view_river()

my_river.one_river_day()
my_river.view_river()

my_river.one_river_week()
my_river.view_river()
