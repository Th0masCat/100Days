import random
import turtle

import colorgram
from turtle import Turtle, Screen

turtle.colormode(255)

the_turtle = Turtle()
direction = [0, 90, 180, 360]
colours = colorgram.extract("image.jpg", 10)
rgb_colours = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b

    colour_tuple = (r, g, b)
    rgb_colours.append(colour_tuple)


the_turtle.speed(100)
the_turtle.width(4)

for _ in range(100):
    the_turtle.color(random.choice(rgb_colours))
    the_turtle.circle(100)
    the_turtle.rt(10)

screen = Screen()
screen.exitonclick()
