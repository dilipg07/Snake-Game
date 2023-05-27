from turtle import Turtle
ALIGN = "center"
FONT = ("ariel", 15, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align = ALIGN, font = FONT)

    def score_increase(self):
        self.clear()
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.color('white')
        self.write(f"Game Over!", align = "center", font = ('ariel', 30, 'bold'))