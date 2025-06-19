from tkinter import *
import os
import pandas
import random

data_path = os.path.join(os.path.dirname(__file__), "data", "french_words.csv")
data = pandas.read_csv(data_path).to_dict(orient='records')
flip_timer = None  # Add this at the top, after your imports

def next_card():
    global flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
        
    global data
    if os.path.exists(os.path.join(os.path.dirname(__file__), "data", "words_to_learn.csv")):
        data_path = os.path.join(os.path.dirname(__file__), "data", "words_to_learn.csv")
        data = pandas.read_csv(data_path).to_dict(orient='records')
    else:
        data_path = os.path.join(os.path.dirname(__file__), "data", "french_words.csv")
        data = pandas.read_csv(data_path).to_dict(orient='records')
    
    global current_word
    current_word = random.choice(data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word['French'], fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)  

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word['English'], fill="white")
    canvas.itemconfig(card_img, image=card_after_img)

def is_known():
    global data
    data.remove(current_word)
    print(f"length of data: {len(data)}")
    pandas.DataFrame(data).to_csv(os.path.join(os.path.dirname(__file__), "data", "words_to_learn.csv"), index=False)
    next_card()


script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "images", "card_front.png")

BACKGROUND_COLOR = "#B1DDC6"

window= Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=600, height = 420)
card_front_img = PhotoImage(file=image_path)
card_after_img = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "card_back.png"))
card_img = canvas.create_image(300, 200, image=card_front_img)

card_title = canvas.create_text(300, 90, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(300, 250, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, pady=20)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

check_img = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "right.png"))
known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

cross_img = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "wrong.png"))
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()
window.mainloop()
