import turtle
import random


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

num_circles = 75
radius_multiplier = 100

for _ in range(num_circles):
    t.color(random_color())
    t.circle(radius_multiplier)
    t.left(10)

screen.exitonclick()
