from turtle import Screen, Turtle
import time

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

pos_arr = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in pos_arr:
    turtle_object = Turtle(shape="square")
    turtle_object.color("white")
    turtle_object.penup()
    turtle_object.goto(position)
    segments.append(turtle_object)

gameOver = False

while not gameOver:
    screen.update()
    time.sleep(0.1)

    for seg in segments:
        seg.forward(20)

screen.exitonclick()
