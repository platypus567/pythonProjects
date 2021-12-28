import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("50 States Game")
image = "blank_states_img.gif"
data = pd.read_csv("50_states.csv")
screen.addshape(image)
turtle.shape(image)
all_states = data.state.to_list()
correct_counter = 0
for state in all_states:
    answer_state = screen.textinput(title=f"Name the state({correct_counter}/50)",prompt="Name a state:")
    if answer_state.lower() == "exit":
        break;
    if answer_state in all_states:
        correct_counter += 1
        print("Correct")
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
screen.exitonclick()

