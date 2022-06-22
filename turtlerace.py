import random
import turtle
from turtle import Turtle, Screen

game_over = False

turtle.colormode(255)
screen = Screen()
screen.setup(width=700, height=500)
user_bet = screen.textinput(title="Place your bet", prompt="Enter a colour")

colours = ["red", "blue", "green", "cyan", "magenta", "yellow"]
dist = [30, 60, 90, 120, 150, 180]
turtle_list = []

for turtle_index in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colours[turtle_index])
    turtle.penup()
    turtle.goto(-300, -100 + dist[turtle_index])
    turtle_list.append(turtle)

while not game_over:
    for turtle_obj in turtle_list:
        turtle_speed = random.randint(0, 10)
        turtle_obj.forward(turtle_speed)

        if turtle_obj.xcor() >= 300:
            game_over = True
            winner_color = turtle_obj.pencolor()

            if winner_color == user_bet:
                print("You won")
            else:
                print(f"{winner_color} won. You Lost")

screen.exitonclick()
