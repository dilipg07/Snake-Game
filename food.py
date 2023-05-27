from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(1, 1)
        self.color('green')
        self.speed('fastest')
        self.goto(randint(-280,280),randint(-280,280))
