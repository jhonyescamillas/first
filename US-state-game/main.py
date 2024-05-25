import pandas
import turtle

ALIGNMENT = "center"

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("Name the 50 states of the US")
# create 2 instance of Turtle class.
# 1 to write the name of states in their corresponding coordinates
# 2 to print the completion message upon answering all 50 states
t = turtle.Turtle()
t.hideturtle()
t.penup()
t2 = turtle.Turtle()
t2.hideturtle()
t2.penup()
t2.color("red")
t2.goto(0, 0)


def main():
    # read from the CSV file
    data = pandas.read_csv("50_states.csv")
    # make a list of all states from the csv file
    all_states = data.state.to_list()
    score = 0
    # make an empty list of all answered states
    answer_list = []
    # loop will keep going until all states have been answered
    while score < 50:
        ans_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Enter State name:").title().strip()
        if ans_state in answer_list:
            # clear the "state already answered" message
            t2.clear()
            t2.write(f"You already answered {ans_state}!", align=ALIGNMENT, font=("Courier", 18, "normal"))
        elif ans_state in all_states:
            t2.clear()
            score += 1
            state_data = data[data.state == ans_state]
            t.goto(state_data.x.iloc[0], state_data.y.iloc[0])
            # this will display the state name in the corresponding coordinate
            t.write(ans_state, align=ALIGNMENT, font=("Courier", 8, "normal"))
            answer_list.append(ans_state)
        elif ans_state == "Exit":
            # when user enters "Exit" call this function
            save_missing_states(all_states, answer_list)
            # break out of the loop to end the game
            break
        else:
            continue

    if score == 50:
        t2.write("Completed\nWell done!", align=ALIGNMENT, font=("Courier", 18, "normal"))
    screen.exitonclick()


def save_missing_states(alist, blist):
    """function to create a csv file that contains all the states that user did not guess"""
    missing_states = [i for i in alist if i not in blist]
    df = pandas.DataFrame(missing_states)
    df.to_csv("missing_states.csv")
    print(missing_states)


if __name__ == "__main__":
    main()
