from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

snake.create_snake()
gameOver = False

while not gameOver:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
