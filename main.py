import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India States Game")
image = "India.gif"
screen.addshape(image)
turtle.shape(image)
india_dataset = pd.read_csv("india_dataset.csv")
all_states = india_dataset.state.to_list()
guessed_states = []

while len(guessed_states) <= 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 States Correct",
                                    prompt="What's the state's name?").title()

    if answer_state == "Exit":
        states_not_guessed = [state for state in all_states if state not in guessed_states]
        states_to_learn_dataframe = pd.DataFrame(states_not_guessed, columns=['States to learn'])
        states_to_learn_dataframe.to_csv('States not guessed need to learn-2.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()  # hides the turtle
        t.penup()  # hides the lines made by turtle when drawing
        answered_state_row = india_dataset[india_dataset.state == answer_state]
        t.goto(int(answered_state_row.x), int(answered_state_row.y))
        t.write(answer_state)
        # writing_turle.write(answered_state_Date_row.state.item())
        # Returns the first element of the underlying data as a python scalar

turtle.mainloop()
