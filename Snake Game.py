from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("🐍 Snake Game 🐍")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collison
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_increase()
        
    # detect collison with wall
    if snake.segment[0].xcor() > 285 or snake.segment[0].xcor() < -285 or snake.segment[0].ycor() > 285 or snake.segment[0].ycor() < -285:
        game_on = False
        scoreboard.game_over()
        print(snake.segment[0].position())
    if snake.segment[0].position() in [x.position() for x in snake.segment[1:]]:
        scoreboard.game_over()
        game_on = False
        

screen.exitonclick()