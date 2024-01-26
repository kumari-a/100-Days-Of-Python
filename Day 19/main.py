from turtle import Turtle,Screen

ptr = Turtle()
screen = Screen()


def move_forward():
    ptr.forward(10)


screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()
