from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=r_paddle.go_up)
screen.onkey(key="Down",fun=r_paddle.go_down)
screen.onkey(key="w",fun=l_paddle.go_up)
screen.onkey(key="s",fun=l_paddle.go_down)

is_on=True
while is_on:
    time.sleep(0.08)
    screen.update()
    ball.move()

    # collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # collision with the paddle
    if  ball.distance(r_paddle)<50 and ball.xcor()>320  or  ball.distance(l_paddle)<50 and ball.xcor()<-320 :
        ball.bounce_x()

    # detect r paddle misses the ball
    if ball.xcor()>380:
        ball.reset()
        scoreboard.l_point()

    # detect l padddle misses the ball
    if ball.xcor()<-380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()