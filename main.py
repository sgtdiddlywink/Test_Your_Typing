# --------------------------------------------------Import Modules-----------------------------------------------------#
from tkinter import *
import random

# --------------------------------------------------Set CONSTANTS------------------------------------------------------#
FONT_NAME = "Arial"
FONT_HEIGHT = 12
FONT_TYPE = "bold"
BACKGROUND_COLOR = "#A5C9CA"
timer = 60

# -------------------------------Random Text. Feel free to add your own to the list.-----------------------------------#
example_text = [
    "This is going to be a lot of sample text.",
    "This should hopefully be even more sample text."
]


# ------------------------------Function for the timer to count down and post the WPM at the end.----------------------#
def start_timer():
    global timer
    if timer > 0:
        time_remaining = f"{timer:02d} Seconds"
        canvas.itemconfig(timer_text, text=time_remaining)
        timer -= 1
        window.after(1000, start_timer)
    else:
        global generated_text
        inputted_user_text = typed_entry_box.get()
        check_wpm(generated_text, inputted_user_text)


# -----------------------Function to generate a random text string from the example list.------------------------------#
def generate_text():
    random_text = random.choice(example_text)
    return random_text


# -Determines the inputted words compared to the original text and calculates how many were correct to determine WPM.--#
def check_wpm(initial_text, inputted_text):
    initial_list = initial_text.split()
    inputted_list = inputted_text.split()
    del initial_list[len(inputted_list):]
    compared_list = [i == j for i, j in zip(initial_list, inputted_list)]
    wpm = 0
    for n in compared_list:
        if n:
            wpm += 1
    wpm_label.config(text=f"You typed at {wpm} words per minute.")


# --------------------------------------------Open Tk Window Box-------------------------------------------------------#
window = Tk()
window.title("WPM Test")
window.config(pady=20, padx=20, bg=BACKGROUND_COLOR)

# ------------------------------------------Create a canvas for the window---------------------------------------------#
canvas = Canvas(width=500, height=500, bg=BACKGROUND_COLOR, highlightthickness=0)
# Create a text object for the timer.
timer_text = canvas.create_text(250, 25, text="60 Seconds", fill="black", font=(FONT_NAME, 18, FONT_TYPE))
canvas.grid(column=0, row=5)

# ------------------------------------------Instructions Label at the top----------------------------------------------#
label_1 = "Test Your Typing Speed. Click the button below and type out the text string shown below. Good Luck!\n" \
          "---------------------------------------------------------------------------------------------------\n\n"
instructions_label = Label(text=label_1, font=(FONT_NAME, 14, FONT_TYPE), bg=BACKGROUND_COLOR)
instructions_label.config(padx=5, pady=5)
instructions_label.grid(row=0, column=0)

# -------------------------------------------------Random text label---------------------------------------------------#
generated_text = generate_text()
random_text_label = Label(text=generated_text, font=(FONT_NAME, 18, FONT_TYPE), bg=BACKGROUND_COLOR)
random_text_label.config(padx=5, pady=5)
random_text_label.grid(row=2, column=0)

# -------------------------------------------Add label for entry box below---------------------------------------------#
label_3 = "\n\n-----------------------------------------------------------------------\n\n\n" \
          "Click the button below to start the timer and immediately start typing.\n"
start_typing_label = Label(text=label_3, font=(FONT_NAME, 14, FONT_TYPE), bg=BACKGROUND_COLOR)
start_typing_label.grid(row=3, column=0)

# ----------------------------------------------Add start timer button-------------------------------------------------#
start_timer_button = Button(text="Start Timer", command=start_timer, font=(FONT_NAME, 16, FONT_TYPE))
start_timer_button.config(padx=2, pady=2)
start_timer_button.grid(row=4, column=0)

# -----------------------------------------Add entry box for the typed text--------------------------------------------#
typed_entry_box = Entry(width=100, font=(FONT_NAME, 16, FONT_TYPE), bd=5)
typed_entry_box.grid(row=5, column=0)

# -----------------------------------Adds a WPM label to inform user of the outcome------------------------------------#
wpm_label = Label(text="", font=(FONT_NAME, 14, FONT_TYPE), bg=BACKGROUND_COLOR)
wpm_label.grid(row=6, column=0)

# -----------------------------------------------Keeps window open-----------------------------------------------------#
window.mainloop()
