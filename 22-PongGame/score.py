from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, score_1=0, score_2=0):
        super().__init__()
        self.score_1 = score_1
        self.score_2 = score_2
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score_1} | {self.score_2}", align="center", font=("Courier", 24, "normal"))
        
    def player_1_score(self):
        self.score_1 += 1
        self.update_score()
        
    def player_2_score(self):
        self.score_2 += 1
        self.update_score()