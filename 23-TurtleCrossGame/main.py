import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with cars
    for car in car_manager.allcars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            print("Game Over!")

    if player.is_at_finish_line():
        print("You've crossed the finish line!")
        player.reset_position()
        scoreboard.increase_level()
        
screen.exitonclick()
