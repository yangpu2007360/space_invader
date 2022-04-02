from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Invader(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1.5)
        self.penup()
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.hideturtle()
        self.goto(random.randint(-230, 230), 260)

    def move_invaders(self):
        self.showturtle()
        new_y = self.ycor() - 3
        self.goto(self.xcor(), new_y)







