from tkinter import *
from tkinter import messagebox
import pandas
from random import shuffle, randint, choice
import pyperclip
import json

FONT_NAME = "Courier"
FONT_SIZE = 14


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print("DEBUG: generate password")
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")
    pyperclip.copy(password)
    password_e.delete(0, END)
    password_e.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    global credentials
    print("DEBUG: Add Password")
    if (len(website_e.get()) == 0) or (len(username_e.get()) == 0) or (len(password_e.get()) == 0):
        messagebox.showinfo(title="Oops", message="Fields cannot be empty")
        return
    else:
        new_entry = {website_e.get(): {
            "username": username_e.get(),
            "password": password_e.get()
        }}
        try:
            with open("data.json") as file_data:
                credentials = json.load(file_data)
        except FileNotFoundError as msg:
            with open("data.json", 'w') as file_data:
                json.dump(new_entry, file_data, indent=4)
        else:
            credentials.update(new_entry)
            with open("data.json", 'w') as file_data:
                json.dump(credentials, file_data, indent=4)
        finally:
            website_e.delete(0, END)
            password_e.delete(0, END)
            website_e.focus()


# ---------------------------- Search------------------------------- #

def search():
    try:
        with open("data.json") as file_data:
            _credentials = json.load(file_data)
        _entry = _credentials[website_e.get()]
        print(f"DEBUG: {_entry}")
    except KeyError:
        messagebox.showinfo(title=website_e.get(), message=f"This website is unknown")
    except FileNotFoundError:
        messagebox.showinfo(title="File Error", message=f"No data file")
    else:
        messagebox.showinfo(title=website_e.get(),
                            message=f"Username: {_entry['username']}, Password: {_entry['password']}")


# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Password Manager")
win.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_l = Label(text="Website:")
website_l.grid(column=0, row=1)
username_l = Label(text="Email/Username:")
username_l.grid(column=0, row=2)
password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

website_e = Entry(width=20)
website_e.grid(column=1, row=1)
website_e.focus()
username_e = Entry(width=35)
username_e.grid(column=1, row=2, columnspan=2)
username_e.insert(0, "jamrobi2@cisco.com")
password_e = Entry(width=20)
password_e.grid(column=1, row=3)

generate_password_b = Button(text="Generate Password", command=generate_password, width=12)
generate_password_b.grid(column=2, row=3)

search_b = Button(text="Search", command=search, width=12)
search_b.grid(column=2, row=1)

add_b = Button(text="Add", command=add_password, width=32)
add_b.grid(column=1, row=4, columnspan=2)

win.mainloop()
