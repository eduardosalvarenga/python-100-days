# Create a Brazil-States-Learning-Game using Pandas and Turtle Library

import pandas
import turtle

screen = turtle.Screen()
screen.title("Brazil States Game")
image = "blank_states.gif"
screen.addshape(image)
screen.setup(1028, 1024)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 27:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/27", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        state_data = data[data.state == answer_state]
        text.goto(int(state_data.x), int(state_data.y))
        text.write(answer_state, align="center", font=("Arial", 10, "normal"))
