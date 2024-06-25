from tkinter import *
import pandas
import random
from pathlib import Path


def get_random_card():
    global card_word, card_title, current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_word, text=current_card["French"])
    flip_timer = window.after(3000, func=flip_card)


def word_known():
    global known_words, words_to_learn
    file_path = Path(WORDS_TO_LEAR_FILE)
    _needs_header = True
    # we only need the header if it is a new file.
    if file_path.exists():
        _needs_header = False
    if current_card not in known_words:
        current_card_df = pandas.DataFrame([current_card])
        current_card_df.to_csv(WORDS_TO_LEAR_FILE, mode='a', header=_needs_header, index=False)

    words_to_learn.remove(current_card)
    flip_card()
    get_random_card()


def flip_card():
    global card_word, card_title
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_title, text="English")


WORDS_TO_LEAR_FILE = "data/words_to_learn.csv"
ALL_WORDS = "./data/french_words.csv"
BACKGROUND_COLOR = "#B1DDC6"

LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

current_card = {}

try:
    words_to_learn_data = pandas.read_csv(WORDS_TO_LEAR_FILE)
except FileNotFoundError:
    known_words = []
else:
    known_words = words_to_learn_data.to_dict(orient="records")

all_words_data = pandas.read_csv(ALL_WORDS)
all_words_data = all_words_data.to_dict(orient="records")
words_to_learn = [entry for entry in all_words_data if entry not in known_words]

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="English", font=LANGUAGE_FONT, fill="black")
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT, fill="black")

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0, command=word_known)
right_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0, command=get_random_card)
wrong_button.grid(column=1, row=1)

get_random_card()

window.mainloop()
