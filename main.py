from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
from lineas import Lanes

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()
lines_positions = [(0, 270), (0, 200), (0, 130), (0, 60), (0, -10), (0, -80), (0, -150), (0, -220), (0, -290)]
for position in lines_positions:
    line = Lanes()
    line.position(position)

screen.listen()
screen.onkey(paddle_r.up, 'Up')
screen.onkey(paddle_r.down, 'Down')
screen.onkey(paddle_l.up, 'w')
screen.onkey(paddle_l.down, 's')


def ball_up():
    return ball.ycor() + 10


def ball_down():
    return ball.ycor() - 10


game_is_on = True
going_up = True
going_down = False
moving_left = False
moving_right = True
intentos = 1
on = True
while on:
    while game_is_on:
        sleep(0.1)
        screen.update()
        # golpear los muros
        new_x = ball.xcor() + 10
        if ball.ycor() == 280:
            new_y = ball_down()
            going_down = True
            going_up = False
        elif ball.ycor() == -280:
            new_y = ball_up()
            going_up = True
            going_down = False
        elif going_up:
            new_y = ball.ycor() + 10
        elif going_down:
            new_y = ball.ycor() - 10
        else:
            new_y = ball.ycor() + 10

        if ball.xcor() > 280 and ball.distance(paddle_r) < 50:
            new_x = ball.xcor() - 10
            moving_left = True
            moving_right = False
        elif ball.xcor() < 280 and ball.distance(paddle_l) < 50:
            new_x = ball.xcor() + 10
            moving_left = False
            moving_right = False
        elif moving_right:
            new_x = ball.xcor() + 10
        elif moving_left:
            new_x = ball.xcor() - 10
        else:
            new_x = ball.xcor() + 10

        if ball.xcor() > 400:
            score.lsup()
            game_is_on = False
        elif ball.xcor() < -400:
            score.rsup()
            game_is_on = False
        screen.update()

        ball.move(new_x, new_y)

    ball.move(0, 0)
    screen.update()
    game_is_on = True
screen.exitonclick()
