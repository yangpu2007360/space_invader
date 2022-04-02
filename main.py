import turtle
from turtle import Screen, Turtle
from bullet import Bullet
from invader import Invader

import time
import random
import easygui
import sys
import os

game_is_on = True

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=600)
screen.title("Space Invader")
screen.tracer(False)

# set up the spaceship
space = Turtle()
space.shape("square")
space.color("green")
space.shapesize(stretch_wid=1.5, stretch_len=1)
space.penup()
space.goto(0, -260)

# set up the bullet on the spaceship.
bullet = Bullet()
bullet.goto(space.xcor(), space.ycor() + 20)
b_list = []
b_list.append(bullet)

i_list = []
invaded = 0
destroyed = 0


def go_left():
    if space.xcor() > -240:
        new_x = space.xcor() - 10
        space.goto(new_x, space.ycor())
        b_list[-1].goto(new_x, space.ycor() + 20)


def go_right():
    if space.xcor() < 230:
        new_x = space.xcor() + 10
        space.goto(new_x, space.ycor())
        b_list[-1].goto(new_x, space.ycor() + 20)


def create_invader():
    new_invader = Invader()
    i_list.append(new_invader)


def shoot_bullet():
    new_bullet = Bullet()
    new_bullet.speed("fastest")
    new_bullet.goto(space.xcor(), space.ycor() + 20)
    b_list.append(new_bullet)


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    print("rerun")
    python = sys.executable
    os.execl(python, python, *sys.argv)


screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(shoot_bullet, "space")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_chance = random.randint(1, 10)
    if random_chance == 1:
        create_invader()

    # invader movement
    for invader in i_list:
        invader.move_invaders()
        if invader.ycor() < -280:
            print("reach the end")
            invaded = invaded + 1
            i_list.remove(invader)
            if invaded == 5:
                game_is_on = False
                turtle.hideturtle()
                turtle.color("white")
                turtle.write("5 invaders came through. Game Over!", move=False, align="center",
                             font=("Arial", 20, "normal"))
                answer = easygui.ynbox('Click Yes to play again', 'Game Over!')
                if answer:
                    print("restart")
                    restart_program()

        for num in range(0, len(b_list)-1):

            b_list[num].move()

            if b_list[num].ycor() > 320:
                b_list.remove(b_list[num])
                print("remove this bullet")

            if b_list[num].distance(invader) < 50:
                i_list.remove(invader)
                print("destroy this invader")
                destroyed = destroyed + 1
                invader.goto(1000, 1000)
                if destroyed == 20:
                    turtle.hideturtle()
                    turtle.color("white")
                    turtle.write("You have destroyed 20 invaders. You win!", move=False, align="center",
                                 font=("Arial", 20, "normal"))
                    game_is_on = False
                    answer = easygui.ynbox('Click Yes to play again', 'You won!')
                    if answer:
                        print("restart")
                        restart_program()

screen.exitonclick()
