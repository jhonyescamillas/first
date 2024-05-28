"""
A program that implements a Pomodoro timer. Displays a countdown timer with a 25-min work and 5-min break patterns.
After four work repetitions, a 20-minute break will be displayed on timer.

This program relies on Tkinter for the UI objects.
"""
from tkinter import *

# GLOBAL CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
# noinspection SpellCheckingInspection
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


class Repetition:
    """A class representing the reps that will be used for the timer function"""
    def __init__(self):
        self.reps = 0
        self.work_reps = 0
        self.timer = None

    def add_rep(self):
        self.reps += 1


# create a Repetition Class instance
reps = Repetition()


def countdown_timer(count):
    """Start the countdown timer and display it on the canvass"""
    seconds = count % 60
    minutes = count // 60
    if count > 0:
        reps.timer = window.after(1000, countdown_timer, count-1)
    else:
        start_timer()
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")


def start_timer():
    """Function to configure the work-break pattern"""
    window.deiconify()
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    reps.add_rep()
    print(f"Reps: {reps.reps}")
    print(f"Work reps: {reps.work_reps}")
    if reps.reps % 8 == 0:
        countdown_timer(LONG_BREAK_MIN * 60)
        label.config(text="LONG BREAK", fg=RED)
    elif reps.reps % 2 != 0:
        countdown_timer(WORK_MIN * 60)
        label.config(text="WORK", fg=GREEN)
        reps.work_reps += 1
    else:
        countdown_timer(SHORT_BREAK_MIN * 60)
        label.config(text="BREAK", fg=PINK)
    check_mark.config(text="✔" * (reps.reps // 2))
    start["state"] = "disabled"


def reset():
    """Function to restart the timer"""
    window.after_cancel(reps.timer)
    reps.reps = 0
    reps.work_reps = 0
    label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="25:00")
    start["state"] = "active"


# draw the window and all other UI components
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
window.columnconfigure(1, minsize=250)

canvas = Canvas()
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text=f"25:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

label = Label(text="Timer", font=(FONT_NAME, 28, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

start = Button(text="Start", command=start_timer)
start.config(text="Start", font=(FONT_NAME, 10, "bold"))
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset)
reset.config(text="Reset", font=(FONT_NAME, 10, "bold"))
reset.grid(column=2, row=2)

check_mark = Label(font=(FONT_NAME, 10), fg="GREEN", bg=YELLOW)
check_mark.grid(column=1, row=3)
# initiate the endless loop to keep the window open
window.mainloop()
