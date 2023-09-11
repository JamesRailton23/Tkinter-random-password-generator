import tkinter.scrolledtext
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import random


def random_password_generator(password_length): # generates the random password
    password = ""
    shuffled_password = ""
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y",
                  "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_characters = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "_", "-", "[", "]", "{", "}", "@", "?", "/", ".",
                          "<", ">", "#", "`"]
    # Generates the random password
    for i in range(password_length):
        selector = random.randint(1, 4)
        if selector == 1:  # characters
            password += random.choice(characters)
        elif selector == 2: # upper case letters
            upper_character = random.choice(characters)
            password += str(upper_character).upper()
        elif selector == 3: # numbers
            password += random.choice(numbers)
        elif selector == 4: # special characters
            password += random.choice(special_characters)

    #shuffles and returns random password
    password = list(password)
    random.shuffle(password)
    shuffled_password = shuffled_password.join(password)
    return shuffled_password

# window
window = Tk()
window.title("Password generator")
window.geometry("500x600")
window.resizable(False, False)

# top label
top_label = Label(window, text="Random Password Generator", font="Arial 20 underline")

# check buttons
special_characters_checkbox = BooleanVar()
numbers_checkbox = BooleanVar()
upper_letters_checkbox = BooleanVar()

# checkbox to either include or remove special characters
checkbox_special_characters = Checkbutton(window, text="Include special Characters", onvalue=True, offvalue=False,
                                          height=2, width=25, font="Arial 15")

# checkbox to either include or remove numbers
checkbox_numbers = Checkbutton(window, text="Include numbers", onvalue=True, offvalue=False, height=2, width=20 ,
                               font="Arial 15")

# checkbox to either include or remove upper case letters
checkbox_uppercase_characters = Checkbutton(window, text="Include uppercase characters", onvalue=True, offvalue=False,
                                            height=2, width=25 , font="Arial 15")

# password length counter
slider_password_length = Scale(window, from_=0, to=100, orient=HORIZONTAL, length=470, tickinterval=5)

# button to generate password
button_generate_password = Button(window, text="Generate Password", height=2, width=20, font=10)

# text area
text_display_password = ScrolledText(window, bd=4, font=15, height=2, width=40, )

# copy to clipboard button
button_copy_to_clipboard = Button(window, text="Copy to clipboard", height=2, width=15)

"""
layout grid
"""
# grid settings
# Label
top_label.pack(pady=30)

# Checkboxes
checkbox_special_characters.pack()
checkbox_numbers.pack()
checkbox_uppercase_characters.pack()

# Slider
slider_password_length.pack(pady=20)
slider_password_length.set(16)

# Button
button_generate_password.pack(pady=20)

# Text area
text_display_password.pack()

#copy to clipboard
button_copy_to_clipboard.pack(pady=15)

# runs program, do not touch!
window.mainloop()
