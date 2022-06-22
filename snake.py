from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20


class Snake:
    def __init__(self):
        self.segments = []

    def create_snake(self):
        for position in STARTING_POSITIONS:
            turtle_object = Turtle(shape="square")
            turtle_object.color("white")
            turtle_object.penup()
            turtle_object.goto(position)
            self.segments.append(turtle_object)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_corr = self.segments[seg_num - 1].xcor()
            y_corr = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(x_corr, y_corr)

        self.segments[0].forward(MOVE_SPEED)

    def up(self):
        if self.segments[0].heading != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading != 180:
            self.segments[0].setheading(0)
