from turtle import Turtle
class Scoreboard(Turtle):
        
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
        
    def update_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def fail_scoreboard(self):
        self.clear()
        self.write("GAME OVER", align="center", font=("Arial", 20, "bold"))
        self.goto(0, 0)
        
class FailScoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.write("GAME OVER", align="center", font=("Arial",20,"bold"))
        self.penup()
        self.goto(0,0)
    
    
    
    
    