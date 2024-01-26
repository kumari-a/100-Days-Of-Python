import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

directions = {"up": 90, "down": 270, "left": 180, "right": 0}

t.speed(0)
t.pensize(5)

for _ in range(200):
    t.color(random_color())
    direction = random.choice(list(directions.keys()))
    distance = random.randint(10, 50)

    t.setheading(directions[direction])
    t.forward(distance)

screen.exitonclick()
