import pandas as pd
import os
import sys
from random import choice
from tkinter import *
from tkinter import messagebox

# constant for the BG color
BACKGROUND_COLOR = "#B1DDC6"


class Word:
    """A class representing each words to be displayed in the flash card. Opens a csv file from the last time
    the program was run. If there's no such file, creates a new dictionary of words from another csv file."""
    def __init__(self):
        data = None
        try:
            data = pd.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            data = pd.read_csv("data/french_words.csv")
        finally:
            self.data_dict = data.to_dict(orient="records")
            self.current_word = None

    def generate_random_word(self):
        """Creates a random word with each round"""
        self.current_word = choice(self.data_dict)
        return self.current_word

    def remove_word(self):
        """Removes the word from the remaining dictionary of words"""
        self.data_dict.remove(self.current_word)


word = Word()


def next_card():
    """Generates the flash card and restart the timer if the remaining words in the dictionary is more than one.
    Once all words in the dictionary have been used, it will remove the csv file and exit the program."""
    root.after_cancel(timer)
    if len(word.data_dict) > 0:
        canvas.itemconfig(card_word, text=word.generate_random_word()["French"], fill="black")
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_image, image=card_front)
        root.after(3000, flip_card)
    else:
        messagebox.showinfo(title="Awesome!", message="You have no more words to learn!")
        messagebox.showinfo(title="Notice", message="Refreshing the list of words now. Please run the program again")
        os.remove("data/words_to_learn.csv")
        sys.exit()


def flip_card():
    """Displays the english counterpart of the current word in the card"""
    root.after_cancel(timer)
    canvas.itemconfig(card_word, text=word.current_word["English"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_image, image=card_back)


def save_words_to_learn():
    """Saves the remaining words in the dictionary to a csv file which wil be opened when the program is run again"""
    word.remove_word()
    df = pd.DataFrame(word.data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# UI objects
root = Tk()
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
root.title("Flashy")

canvas = Canvas(root, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))

x_button_img = PhotoImage(file="./images/wrong.png")
x_button = Button(root,
                  image=x_button_img, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0, command=next_card)
check_button_img = PhotoImage(file="./images/right.png")
check_button = Button(root, image=check_button_img,
                      bg=BACKGROUND_COLOR, bd=0, highlightthickness=0, command=save_words_to_learn)
# Placement of UI objects in the window
canvas.grid(column=0, row=0, columnspan=2)
x_button.grid(column=0, row=1)
check_button.grid(column=1, row=1)
# create a 3-second timer for when the english word will be displayed
timer = root.after(3000, flip_card)
# call the function to generate and display random words
next_card()

root.mainloop()
