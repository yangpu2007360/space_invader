from turtle import Turtle


class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y_move = 7
        self.speed('fastest')
        self.on_space = True

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
