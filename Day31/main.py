# Create a flashcard program

from tkinter import *

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_d = {}

# ---------------------------- GETTING THE CSV LIST WITH THE WORDS ------------------------------- #
try:
    words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/chinese words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    words_d = words.to_dict(orient="records")


# ----------------------- GENERATE NEW WORD, FLIP CARD, CHECK IF CARD IS KNOWN ----------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_d)
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card_text, text=current_card['Chinese'], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(4000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card['English'], fill="white")


def is_known():
    global current_card
    words_d.remove(current_card)
    data = pandas.DataFrame(words_d)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
