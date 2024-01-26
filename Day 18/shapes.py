from turtle import Turtle, Screen

line = Turtle()
original_time = 3
colors = ["red", "green", "blue", "orange", "purple", "pink", "brown", "cyan", "magenta"]


def move(num_sides, side_length, obj):
    interior_angle = 180 - (360 / num_sides)
    for _ in range(num_sides):
        obj.forward(side_length)
        obj.right(180 - interior_angle)


line.penup()
line.left(90)
line.forward(100)
line.left(90)
line.forward(100)
line.right(90)
line.right(90)
line.pendown()
for num_sides, color in zip(range(3, 11), colors):
    line.color(color)
    move(num_sides, 100, line)

screen = Screen()
screen.exitonclick()
