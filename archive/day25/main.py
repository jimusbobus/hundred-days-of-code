import turtle
import pandas

screen = turtle.Screen()
screen.title("US States")
IMAGE = "./blank_states_img.gif"
screen.addshape(IMAGE)

turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")

guessed_states = []


def write_state(_state_name, _x, _y):
    _state = turtle.Turtle()
    print(f"DEBUG: X: {_x}, Y: {_y}, State: {_state_name}")
    _state.penup()
    _state.hideturtle()
    _state.goto(_x, _y)
    _state.write(_state_name)


def ask_question():
    while len(guessed_states) < 52:
        guess = screen.textinput(title=f"States Guessed: {len(guessed_states)}", prompt="State? ").title()
        if not data[data.state == guess].empty:  # User closed the dialog or clicked "Cancel"
            # print(data[data.state == guess])
            x_cor = data[data.state == guess].x.iloc[0]
            # print(f"X: {x_cor}")
            y_cor = data[data.state == guess].y.iloc[0]
            # print(f"Y: {y_cor}")
            write_state(guess, x_cor, y_cor)
            guessed_states.append(guess)
        elif guess == "Exit":
            # screen.bye()
            break
        else:
            print(f"Guess {guess} is invalid")


# write out unknown states

# def get_mouse_click_cor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_cor)
ask_question()

mising_states = [item for item in data.state.to_list() if item not in guessed_states]


to_learn = pandas.DataFrame(mising_states)
to_learn.to_csv("to_learn.csv")

# turtle.mainloop()

# screen.exitonclick()
