from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
#1st player
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

#2nd player
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



gameOn = True
while gameOn:
    time.sleep(ball.ball_spd)
    screen.update()
    ball.move()

    #Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce(wall_bounce = 1, paddle_bounce = 0)

    #Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        #need to bounce
        ball.bounce(wall_bounce = 0, paddle_bounce = 1)

    #Reset the ball R side
    if ball.xcor() > 350:
        ball.reset_pos()
        scoreboard.score_increase("l")

    # Reset the ball L side
    if ball.xcor() < -350:
        ball.reset_pos()
        scoreboard.score_increase("r")



screen.exitonclick()