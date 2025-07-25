import random
import turtle as t




sq_scr = t.Screen()
game_on = False
sq_scr.setup(500,400)
ur_bet = sq_scr.textinput("Make your bet", "Which turtle will win the bet? choose the colour")
turtles_list = []
colors = ["pink", "red", "orange", "yellow", "grey", "brown"]

for i in range(0,6):
    new_sqrtle = t.Turtle(shape="turtle")
    new_sqrtle.penup()
    new_sqrtle.color(colors[i])
    new_sqrtle.goto(-230, (-50+(i*30)))
    turtles_list.append(new_sqrtle)

if ur_bet:
    game_on = True

while game_on:
    for turt in turtles_list:
        if turt.xcor()>230:
            game_on = False
            winning_color = turt.pencolor()
            if winning_color == ur_bet:
                print("you won")
            else:
                print("You lost")

        distance = random.randint(0,15)
        turt.fd(distance)

sq_scr.exitonclick()
