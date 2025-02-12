# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_tuple = (r, g, b)
#     rgb_colors.append(my_tuple)

# print(rgb_colors)
######################## Used the above code to extract colours from a online((downloaded) damien hirst painting ######################
####################### Can ignore it , no need to import colorgram ###################################################################
import turtle as t
import random
color_list = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136),
    (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
    (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
    (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
    (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
    (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.hideturtle()
tim.speed(0)
y_cor = 0
for i in range(8):
    for _ in range(10):
        tim.dot(10, random.choice(color_list))
        tim.penup()
        tim.fd(30)
    y_cor += 30
    tim.teleport(0, y_cor)
screen.mainloop()
