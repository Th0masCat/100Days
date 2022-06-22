from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake.create_snake()
gameOver = False

while not gameOver:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        gameOver = True
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            gameOver = True
            scoreboard.game_over()

screen.exitonclick()
