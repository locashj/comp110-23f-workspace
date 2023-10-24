"""EX05 - Turtle """

__author__ = "730718389"

from turtle import Turtle, colormode, done, Screen
import random

def move(t: Turtle, pos_x: float, pos_y: float):
    """`move` accepts a Turtle handle, and an x and y coordinate (`pos_x` and `pos_y`) and moves the turtle handle to that position, without drawing."""
    t.penup()
    t.goto(pos_x, pos_y)
    t.pendown()


def draw_pizza(t: Turtle, start_x: float, start_y: float, radius: float):
    """`draw_pizza` accepts a starting x and y coordinate, `start_x` and `start_y`, and a radius ,`radius`, and draws a basic cheese pizza."""
    move(t, start_x, start_y)

    # crust
    t.fillcolor(150, 75, 0)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # cheesy part
    move(t, start_x, start_y + (radius * 0.1))
    t.fillcolor(255, 166, 0)
    t.begin_fill()
    t.circle(radius * 0.90)
    t.end_fill()

    # slices
    center_x = start_x
    center_y = start_y + radius

    for i in range(0, 8):
        move(t, center_x, center_y)
        t.forward(radius)
        t.left(45)


def main():
    """`main` initializes the Turtle handle and draws 15 pizzas."""
    screen = Screen()
    screen.bgcolor(0, 0, 0)
    bob: Turtle = Turtle()
    bob.speed(500)
    bob.hideturtle()
    colormode(255)

    num_pizzas: int = 15
    # draw 10 pizzas randomly on the screen
    pizza_radius: float = 350
    while num_pizzas > 0:
        start_x: int = random.randrange(-500, 500)
        start_y: int = random.randrange(-1000, 0)
        draw_pizza(bob, start_x, start_y, pizza_radius)
        num_pizzas -= 1
    done()


if __name__ == '__main__':
    main()
