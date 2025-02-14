from turtle import Turtle, Screen
from random import randint
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet !!",
                            prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'blue', 'purple', 'green', 'orange']
y_positions = [-100, -50, 0, 50, 100]
all_turtles = []
for turtle_index in range(5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    new_turtle.speed(3)
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            print(f"{winner.title()} turtle wins !!")
            if user_bet == winner:
                print("You've won the bet")
            else:
                print("Sorry,you lost the bet")

        else:
            random_distance = randint(0, 10)
            turtle.fd(random_distance)

screen.mainloop()
