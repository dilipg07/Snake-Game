from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("🐍 Snake Game 🐍")

start_position = [(0,0),(-20,0),(-40,0)]

for pos in start_position:
    new_square = Turtle('square')
    new_square.color('white')
    new_square.goto(pos)

screen.exitonclick()