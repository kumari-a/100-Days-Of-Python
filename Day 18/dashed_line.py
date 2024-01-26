from turtle import Turtle, Screen

line_ = Turtle()


def draw(line):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)


for _ in range(10):
    draw(line_)

screen = Screen()
screen.exitonclick()
