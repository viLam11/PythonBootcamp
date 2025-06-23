from turtle import Turtle
import random
COLORS = ["red", "green", "blue", "yellow", "purple"]

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = []
        for i in range(4):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.shapesize(stretch_wid=1, stretch_len=1)
            new_segment.penup()
            new_segment.goto(0, -200-20*i)
            new_segment.setheading(90)
            self.segment.append(new_segment)       
        
    def move(self):
        for i in range(len(self.segment)-1, 0 , -1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].goto(new_x, new_y)    
        self.segment[0].forward(20)
   
    def turn_up(self):    
        self.segment[0].setheading(90)
    
    def turn_right(self):  
        self.segment[0].setheading(0)
        
    def turn_left(self):   
        self.segment[0].setheading(180)
        
    def turn_down(self):
        self.segment[0].setheading(270)
            
    def snake_grow(self):
        new_segment = Turtle("square")
        new_segment.color(random.choice(COLORS))
        new_segment.shapesize(stretch_wid=1, stretch_len=1)
        fx = self.segment[-1].xcor()
        fy = self.segment[-1].ycor()
        new_segment.penup()
        new_segment.goto(fx, fy)
        self.segment.append(new_segment)
    
    def collision_wall(self) -> bool:
        current_x = self.segment[0].xcor()
        current_y = self.segment[0].ycor()
        if current_x > 295 or current_x < -295 or current_y > 295 or current_y < -295:
            return True
        return False
        
    def collision_self(self) -> bool:
        head = self.segment[0]
        for x in self.segment[1:]:
            if head.distance(x) < 5:
                return True
        return False