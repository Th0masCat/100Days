from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20


class Snake:
    def __init__(self):
        self.segments = []

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_corr = self.segments[seg_num - 1].xcor()
            y_corr = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(x_corr, y_corr)

        self.segments[0].forward(MOVE_SPEED)

    def extend(self):
        self.add_segment(self.segments[-1].position())

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
