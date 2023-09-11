from tkinter import *
import random


def randomPasswordGenerator(password_Length): #generates the random password
    length = password_Length
    password = ""
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y",
                  "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_characters = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "_", "-", "[", "]", "{", "}", "@", "?", "/", ".",
                          "<", ">", "#", "`"]
    # Generates the random password
    for i in range(length):
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
        return str(password)

# window
window = Tk()
window.title("Password generator")
window.geometry("800x500")

# top label
top_label = Label(window, text="Random Password Generator", font="70")

# check buttons
special_characters_checkbox = BooleanVar()
numbers_checkbox = BooleanVar()
upper_letters_checkbox = BooleanVar()

# checkbox to either include or remove special characters
checkbox_special_characters = Checkbutton(window, text="Include special Characters", onvalue=True, offvalue=False,
                                          height=2, width=20)

# checkbox to either include or remove numbers
checkbox_numbers = Checkbutton(window, text="Include numbers", onvalue=True, offvalue=False, height=2, width=20)

# checkbox to either include or remove upper case letters
checkbox_uppercase_characters = Checkbutton(window, text="Include uppercase characters", onvalue=True, offvalue=False,
                                            height=2, width=30)

# button to generate password
button_generate_password = Button(window, text="Generate Password", height=2, width=20, font=10)

"""
layout grid
"""
#top label
top_label.grid(row=0, column=0)

# checkboxes
checkbox_numbers.grid(row=1, column=0)
checkbox_special_characters.grid(row=1, column=1)
checkbox_uppercase_characters.grid(row=1, column=2)


# button
button_generate_password.grid(row=3, column=1,pady=30)

# runs program, do not touch!
window.mainloop()
