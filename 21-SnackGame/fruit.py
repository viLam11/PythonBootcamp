from turtle import Turtle
import random

class Fruit(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        x = random.randint(-260, 260)
        y = random.randint(-260, 280)
        self.goto(x, y) 
    