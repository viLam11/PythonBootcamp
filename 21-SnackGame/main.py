import time
from snake import Snake
from turtle import *
from fruit import Fruit 
from scoreboard import Scoreboard, FailScoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

the_snake = Snake()
the_fruit = Fruit()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(the_snake.turn_up, "Up")
screen.onkey(the_snake.turn_down, "Down")
screen.onkey(the_snake.turn_left, "Left")
screen.onkey(the_snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    the_snake.move()
    if the_snake.segment[0].distance(the_fruit) < 15:
        the_fruit.refresh()
        the_snake.snake_grow()      
    
    if the_snake.collision_wall() or the_snake.collision_self():
        game_is_on = False
        fail_screen = FailScoreboard()
        
screen.exitonclick()