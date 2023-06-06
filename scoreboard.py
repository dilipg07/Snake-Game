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
        # self.highscore = 0
        with open("Snake Game\data.txt") as data:
            self.highscore = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score} High score: {self.highscore}", align = ALIGN, font = FONT)

    def score_increase(self):
        self.clear()
        self.score +=1
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Snake Game\data.txt", mode = 'w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.update_scoreboard()