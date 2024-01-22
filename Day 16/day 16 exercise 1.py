from turtle import  Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
for i in range(100):
    timmy.forward(1)

timmy.right(90)
timmy.forward(100)
my_screen = Screen()

print(my_screen.canvheight)
my_screen.exitonclick()