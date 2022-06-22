import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

the_turtle = Turtle()


def mov_forward():
    the_turtle.forward(10)


def mov_backward():
    the_turtle.backward(10)


def mov_right():
    the_turtle.rt(30)


def mov_left():
    the_turtle.rt(-30)


def clean():
    screen.reset()


screen = Screen()

screen.listen()

screen.onkeypress(key="w", fun=mov_forward)
screen.onkeypress(key="s", fun=mov_backward)
screen.onkeypress(key="d", fun=mov_right)
screen.onkeypress(key="a", fun=mov_left)
screen.onkeypress(key="c", fun=clean)

screen.exitonclick()
