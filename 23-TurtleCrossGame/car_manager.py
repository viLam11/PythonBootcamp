from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.allcars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_car()
        
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            car.setheading(180)
            self.allcars.append(car)

    def move_cars(self):
        for car in self.allcars:
            car.forward(self.move_distance)


