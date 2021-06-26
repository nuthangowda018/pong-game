from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_mov=10
        self.y_mov=10

    def move(self):
        self.goto(self.xcor()+self.x_mov,self.ycor()+self.y_mov)


    def bounce_y(self):
        self.y_mov *= -1

    def bounce_x(self):
        self.x_mov *= -1

    def reset(self):
        self.goto(0,0)
        self.bounce_x()
