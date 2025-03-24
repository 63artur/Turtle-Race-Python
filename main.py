import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Entar a color: ")
colors = ["red", "blue", "green", "yellow", "purple", "cyan", "pink"]
positions = [-100,-50,0,50,100,150]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(random.choice(colors))
    new_turtle.penup()
    new_turtle.goto(-350,positions[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    dalej = True
while dalej:
    for turtle in all_turtles:
        if turtle.xcor()>400:
            dalej = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print(f"You win! The {winning} turtle is the winner!")
            else:
                print(f"You lose! The {winning} turtle is the winner!")
        random_distance = random.randint(0,50)
        turtle.forward(random_distance)
screen.mainloop()