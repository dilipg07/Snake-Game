from turtle import Turtle
start_position = [(0,0),(-20,0),(-40,0)]
move_distance = 20
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        
    def create_snake(self):    
        for pos in start_position:
            self.add_seg(pos)
            
    
    def add_seg(self, position):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.segment.append(new_square)

    def extend(self):
        self.add_seg(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment)-1,0,-1):
            self.segment[seg].goto(self.segment[seg-1].xcor(), self.segment[seg-1].ycor())
        self.segment[0].forward(move_distance)

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].seth(90)
    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].seth(270)
    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].seth(180)
    def right(self):
        if self.segment[0].heading() != 180:    
            self.segment[0].seth(0)