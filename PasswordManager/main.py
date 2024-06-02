import string
import pyperclip
import json
from random import choices, randint, shuffle
from tkinter import *
from tkinter import ttk, messagebox

# GLOBAL CONSTANTS
FONTSTYLE = ("Courier", 11, "bold")


def add_data():
    """Saves the user input as a dictionary entry to a cv file. User will be prevented to input an already existing
    data for a website. Clears all fields upon successful entry of new data."""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website.title(): {"email": username, "password": password}}
    if not website.strip():
        messagebox.showinfo(message=f"Website cannot be empty")
    if not username.strip():
        messagebox.showinfo(message=f"Username cannot be empty")
    if not password.strip():
        messagebox.showinfo(message=f"Password cannot be empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                messagebox.showinfo(
                    title="Data saved", message=f"Username/password added for {website}"
                )
                clear()
        else:
            if website.title() in data:
                messagebox.showinfo(title="Warning", message="Existing data")
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
                messagebox.showinfo(
                        title="Data saved", message=f"Username/password added for {website}"
                        )
                clear()


def clear():
    """Clears all entry fields."""
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


def generate_password():
    """Creates a random password that combines alphanumeric characters and symbols."""
    password_entry.delete(0, END)
    new_password = choices(string.ascii_letters, k=randint(8, 10))
    new_password += choices(string.punctuation, k=randint(2, 4))
    new_password += choices(string.digits, k=randint(2, 4))
    shuffle(new_password)
    password_entry.insert(END, string="".join(new_password))
    pyperclip.copy(password_entry.get())


def search():
    """Reads from data.json file for existing data on a particular website. Displays the data if it exists."""
    website = website_entry.get().title()
    try:
        with open("data.json") as file:
            data = json.load(file)
            if website in data:
                messagebox.showinfo(
                        title=website.title(),
                        message=f"Username/email: {data[website]['email']}\nPassword: {data[website]['password']}"
                                f"\n\nPassword copied to clipboard."
                    )
                pyperclip.copy(data[website]["password"])
            else:
                messagebox.showinfo(title="Error", message="No data found")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(message="No data found")


# UI objects
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)
window.resizable(FALSE, FALSE)

canvas = Canvas(window, width=200, height=200)
img_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_file)
canvas.grid()

frame = ttk.Frame(window)
frame.config(padding=3, borderwidth=2, relief="groove")
website_label = Label(frame, text="Website:", font=FONTSTYLE)
username_label = Label(frame, text="Email/Username:", font=FONTSTYLE)
password_label = Label(frame, text="Password:", font=FONTSTYLE)
website_entry = Entry(frame, width=30)
website_entry.focus()
username_entry = Entry(frame)
username_entry.insert(END, string="icemonst3r@gmail.com")
password_entry = Entry(frame)
gen_pass = ttk.Button(frame, text="Generate Password", command=generate_password)
add_button = ttk.Button(frame, text="Add", command=add_data)
clear_button = ttk.Button(frame, text="Clear", command=clear)
search_button = ttk.Button(frame, text="Search", command=search)
# UI object placement
frame.grid()
website_label.grid(column=0, row=0, sticky="W", padx=2, pady=2)
username_label.grid(column=0, row=1, sticky="W", padx=2, pady=2)
password_label.grid(column=0, row=2, sticky="W", padx=2, pady=2)
website_entry.grid(column=1, row=0, padx=2, pady=2)
username_entry.grid(column=1, row=1, padx=2, pady=2, columnspan=2, sticky="EW")
password_entry.grid(column=1, row=2, padx=2, pady=2, sticky="EW")
gen_pass.grid(column=2, row=2, padx=2, pady=2)
add_button.grid(column=1, row=3, padx=2, pady=2, sticky="EW")
clear_button.grid(column=2, row=3, padx=2, pady=2, sticky="EW")
search_button.grid(column=2, row=0, padx=2, pady=2, sticky="EW")

window.mainloop()
