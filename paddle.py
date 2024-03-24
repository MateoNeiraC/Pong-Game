from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x=xcor, y=ycor)

    def up(self):
        new_y = super().ycor() + 20
        super().goto(super().xcor(), new_y)

    def down(self):
        new_y = super().ycor() - 20
        super().goto(super().xcor(), new_y)
