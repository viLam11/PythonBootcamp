from turtle import *
import time
from paddle import Paddle
from score import ScoreBoard
from ball import Ball

screen = Screen()
screen.title("Pong Game")
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")

scoreboard = ScoreBoard(0, 0)

player_1 = Paddle((-290, 0))
player_2 = Paddle((280, 0))

ball = Ball()

screen.listen()
screen.onkey(player_1.move_up, 'w')
screen.onkey(player_1.move_down, 's')
screen.onkey(player_2.move_up, 'Up')
screen.onkey(player_2.move_down, 'Down')

game_is_on = True   
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    
    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()
    
    if ball.distance(player_1) < 50 and ball.xcor() < -268 or ball.distance(player_2) < 50 and ball.xcor() > 260:
        ball.bounce_x()
        
    if ball.xcor() > 290 and ball.distance(player_2) > 50:
        ball.reset_position()
        scoreboard.player_1_score()
        screen.update()
    
    if ball.xcor() < -288 and ball.distance(player_1) > 50:
        ball.reset_position()
        scoreboard.player_2_score()
        screen.update()

    
screen.exitonclick()    