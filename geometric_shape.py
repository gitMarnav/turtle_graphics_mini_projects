from turtle import Turtle, Screen
import random
colours = ['red', 'blue', 'lightseagreen', 'yellow',
           'darkgreen', 'hotpink', 'wheat', 'lavenderblush4']
tim = Turtle()
for i in range(3, 11):
    new_color = random.choice(colours)
    tim.color(new_color)
    colours.remove(new_color)
    for _ in range(i):
        tim.fd(50)
        tim.rt(360/i)


screen = Screen()
screen.exitonclick()
