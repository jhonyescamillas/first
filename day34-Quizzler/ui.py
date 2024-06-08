import requests
from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain
from question_model import Question
from data import Data

# GLOBAL CONSTANTS
THEME_COLOR = "#375362"
FONTSTYLE = ("Arial", 18, "italic")
FONTSTYLE_SMALL = ("Arial", 10)
FONTSTYLE_MEDIUM = ("Courier", 15)


class QuizInterface:
    """A class representing the user interface of the quiz game."""
    def __init__(self):
        self.data = Data()
        self.quiz_brain = None
        # main window
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)
        # noinspection SpellCheckingInspection
        self.root.title("Quizzler")
        # Spinbox
        question_num_val = StringVar(self.root)
        # noinspection PyTypeChecker
        question_num_val.set(10)
        self.question_num = Spinbox(self.root, from_=1, to=20, width=10,
                                    textvariable=question_num_val, justify="center", command=self.question_num_select)
        self.question_num.grid(row=2, column=1, pady=5, sticky="W")
        # canvas
        self.canvas = Canvas(self.root, width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, text="Questions go here...", width=280, font=FONTSTYLE)
        self.canvas.grid(row=5, column=0, columnspan=3, pady=40)
        # images
        true_button_img = PhotoImage(file="images/true.png")
        false_button_img = PhotoImage(file="images/false.png")
        # dropdown box
        category_val = StringVar(self.root)
        category_val.set("Any")
        self.category_box = ttk.Combobox(self.root, width=30, textvariable=category_val, values=self.data.categories)
        self.category_box.bind('<<ComboboxSelected>>', self.category_select)
        self.category_box.grid(row=0, column=1, pady=5, columnspan=2, sticky="EW")
        diff_val = StringVar(self.root)
        diff_val.set("Any")
        self.difficulty_box = ttk.Combobox(self.root, width=20, textvariable=diff_val, values=self.data.difficulty)
        self.difficulty_box.bind('<<ComboboxSelected>>', self.difficulty_select)
        self.difficulty_box.grid(row=1, column=1, pady=5, columnspan=2, sticky="EW")
        # make the options un-editable
        self.category_box.config(state="readonly")
        self.difficulty_box.config(state="readonly")
        # buttons
        self.true_button = Button(image=true_button_img, bd=0, highlightthickness=0,
                                  command=lambda: self.get_answer("True"))
        self.true_button.grid(row=6, column=0)
        self.false_button = Button(image=false_button_img, bd=0, highlightthickness=0,
                                   command=lambda: self.get_answer("False"))
        self.false_button.grid(row=6, column=2, sticky="W")
        self.start_button = ttk.Button(text="Start", command=self.start_quiz)
        self.start_button.grid(row=2, column=2, pady=5, sticky="W")
        # labels
        self.question_num_label = Label(text="Number of questions:",
                                        bg=THEME_COLOR, foreground="white", font=FONTSTYLE_SMALL)
        self.question_num_label.grid(row=2, column=0, sticky="W")
        self.category_label = Label(text="Select category:",
                                    bg=THEME_COLOR, foreground="white", font=FONTSTYLE_SMALL)
        self.category_label.grid(row=0, column=0, sticky="W")
        self.difficulty_label = Label(text="Select difficulty:",
                                      bg=THEME_COLOR, foreground="white", font=FONTSTYLE_SMALL)
        self.difficulty_label.grid(row=1, column=0, sticky="W")
        self.score = 0
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, foreground="white", font=FONTSTYLE_MEDIUM)
        self.score_label.grid(row=3, column=0, columnspan=3)
        self.disable_buttons()

        self.root.mainloop()

    def start_quiz(self):
        # start the quiz, generate the questions using the API
        response = requests.get(self.data.url, params=self.data.parameters)
        response.raise_for_status()
        if response.json()["response_code"] == 0:
            question_data = response.json()["results"]
            self.score = 0
            self.score_label.config(text=f"Score: 0")
            self.enable_buttons()
            question_bank = []
            for question in question_data:
                question_text = question["question"]
                question_answer = question["correct_answer"]
                new_question = Question(question_text, question_answer)
                question_bank.append(new_question)
            # instantiate the quiz mechanics
            self.quiz_brain = QuizBrain(question_bank)
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.canvas_text,
                                   text="Not enough questions for that category and/or difficulty.")

    def get_next_question(self):
        # get the next question from the question bank
        self.canvas.config(bg="white")
        self.enable_buttons()
        if self.quiz_brain.still_has_questions():
            current_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=current_question)
        else:
            self.disable_buttons()
            self.canvas.itemconfig(self.canvas_text, text="End of quiz.")

    def get_answer(self, user_answer):
        # check the user's answer against the correct answer
        self.disable_buttons()
        if self.quiz_brain.check_answer(user_answer):
            self.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.score}/{self.quiz_brain.question_number}")
        self.root.after(1000, self.get_next_question)

    def disable_buttons(self):
        self.true_button["state"] = "disabled"
        self.false_button["state"] = "disabled"

    def enable_buttons(self):
        self.true_button["state"] = "active"
        self.false_button["state"] = "active"

    # noinspection PyUnusedLocal
    def category_select(self, event=None):
        # get the current value of the category dropdown and set it to the parameters
        self.data.cat_sel = self.category_box.get()
        self.data.parameters["category"] = self.data.category_dict[self.data.cat_sel]

    # noinspection PyUnusedLocal
    def difficulty_select(self, event=None):
        # get the current value of the difficulty dropdown and set it to the parameters
        self.data.diff_sel = self.difficulty_box.get()
        if self.data.diff_sel == "Any":
            self.data.parameters["difficulty"] = None
        else:
            self.data.parameters["difficulty"] = self.data.diff_sel.lower()

    def question_num_select(self):
        # get the current value of the questions spinbox and set it to the parameters
        self.data.question_num_sel = self.question_num.get()
        self.data.parameters["amount"] = self.data.question_num_sel
