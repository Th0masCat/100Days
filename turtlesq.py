import random
from turtle import Turtle, Screen

the_turtle = Turtle()
direction = [0, 90, 180, 360]
colours = ["red", "purple", "brown", "pink", "green"]

the_turtle.speed(10000000)
the_turtle.width(5)

for i in range(200):
    the_turtle.color(random.choice(colours))
    the_turtle.forward(10)
    the_turtle.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
