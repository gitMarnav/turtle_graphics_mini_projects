import turtle as t
from random import randint, choice
tim = t.Turtle()
angle = [0, 90, 180, 270]
screen = t.Screen()
t.colormode(255)
tim.hideturtle()
tim.pensize(5)
tim.speed(0)

for _ in range(randint(100, 500)):
    tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    tim.forward(10)
    tim.setheading(choice(angle))

screen.exitonclick()
