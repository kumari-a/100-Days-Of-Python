from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")


def move_forward(timmy):
    timmy.forward(100)
    timmy_the_turtle.right(90)


for _ in range(4):
    move_forward(timmy_the_turtle)

screen = Screen()
screen.exitonclick()
