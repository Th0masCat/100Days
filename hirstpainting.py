import random
import turtle
import colorgram
from turtle import Turtle, Screen

turtle.colormode(255)

the_turtle = Turtle()
direction = [0, 90, 180, 360]
rgb_colours = []

colours = colorgram.extract("image.jpg", 6)

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b

    colour_tuple = (r, g, b)
    rgb_colours.append(colour_tuple)

the_turtle.penup()
the_turtle.hideturtle()
the_turtle.speed(10)

the_turtle.setheading(225)
the_turtle.forward(250)
the_turtle.setheading(0)

dots = 100

for dot_count in range(1, dots+1):
    the_turtle.dot(25, random.choice(rgb_colours))
    the_turtle.forward(50)

    if dot_count % 10 == 0:
        the_turtle.setheading(90)
        the_turtle.forward(50)
        the_turtle.setheading(180)
        the_turtle.forward(500)
        the_turtle.setheading(0)

screen = Screen()
screen.exitonclick()
