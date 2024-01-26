from turtle import Turtle,Screen
import random

arrow_ = Turtle()
arrow_.speed("fastest")


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def go_to_end(ptr):
    ptr.penup()
    ptr.right(90)
    ptr.forward(200)
    ptr.right(90)
    ptr.forward(300)
    ptr.right(180)
    ptr.pendown()


def draw_line(ptr):
    for _ in range(10):
        ptr.pendown()
        ptr.dot(30,random_color())
        ptr.penup()
        ptr.forward(50)
        ptr.pendown()
        ptr.dot(30,random_color())


def reset_position(ptr):
    ptr.penup()
    ptr.right(180)
    ptr.forward(500)
    ptr.right(90)
    ptr.forward(50)
    ptr.right(90)
    ptr.pendown()


def draw(arrow):
    go_to_end(arrow)
    for _ in range(10):
        draw_line(arrow)
        reset_position(arrow)


draw(arrow_)
screen = Screen()
screen.exitonclick()
