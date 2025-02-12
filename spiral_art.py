# import turtle as t
# import random
# tim = t.Turtle()
# screen = t.Screen()
# tim.speed(0)
# t.colormode(255)
# tim.pensize(2)
# tim.hideturtle()


# def set_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# angle = 0
# for i in range(80):
#     tim.color(set_color())
#     tim.setheading(angle)
#     tim.circle(100)
#     angle += 5
# screen.mainloop()


import turtle as t
import random
tim = t.Turtle()
screen = t.Screen()
tim.speed(0)
t.colormode(255)


def set_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(300):
    tim.color(set_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 5)
    if tim.heading() < 1:
        break

screen.mainloop()
