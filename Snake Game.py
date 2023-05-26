from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("🐍 Snake Game 🐍")
screen.tracer(0)

start_position = [(0,0),(-20,0),(-40,0)]
segment = []
for pos in start_position:
    new_square = Turtle('square')
    new_square.color('white')
    new_square.penup()
    new_square.goto(pos)
    segment.append(new_square)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segment)-1,0,-1):
        segment[seg].goto(segment[seg-1].xcor(), segment[seg-1].ycor())
    segment[0].forward(20)
    segment[0].left(90)
        
screen.exitonclick()