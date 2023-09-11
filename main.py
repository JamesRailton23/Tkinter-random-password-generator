import random
from tkinter import *
from tkinter.scrolledtext import ScrolledText

import clipboard


def copy_to_clipboard():
    clipboard.copy(text_display_password.get("1.0", "end"))
    copied_to_clipboard_window = Toplevel(window)
    copied_to_clipboard_window.resizable(False, False)
    copied_to_clipboard_window.geometry("300x100")
    copied_to_clipboard_window.title("Success")
    Label(copied_to_clipboard_window, text="Successfully copied password to clipboard").pack()


def clear_text():
    text_display_password.delete("1.0", "end")


def random_password_generator():
    password_length = int(slider_password_length.get())

    password = ""
    shuffled_password = ""
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y",
                  "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_characters = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "_", "-", "[", "]", "{", "}", "@", "?", "/", ".",
                          "<", ">", "#", "`", "¬", ";", "+", "="]
    # Generates the full random password
    for i in range(password_length):
        selector = random.randint(1, 4)
        if selector == 1:  # characters
            password += random.choice(characters)
        elif selector == 2:  # upper case letters
            upper_character = random.choice(characters)
            password += str(upper_character).upper()
        elif selector == 3:  # numbers
            password += random.choice(numbers)
        elif selector == 4:  # special characters
            password += random.choice(special_characters)

    # shuffles and returns random password
    password = list(password)
    random.shuffle(password)
    shuffled_password = shuffled_password.join(password)
    clear_text()
    text_display_password.insert(INSERT, shuffled_password)


# window
window = Tk()
window.title("Password generator")
window.geometry("500x600")
window.configure(background="light blue")
window.resizable(False, False)

# top label
top_label = Label(window, text="Random Password Generator", font="Arial 20 underline")

# password length counter
slider_password_length = Scale(window, from_=0, to=100, orient=HORIZONTAL, length=470, tickinterval=5,
                               label="Select how many characters you want in your password", relief=GROOVE)

# generate password button
button_generate_password = Button(window, text="Generate Password", height=2, width=20, font=10,
                                  command=random_password_generator)

# text area
text_display_password = ScrolledText(window, bd=4, font=15, height=2, width=40, )

# copy to clipboard button
button_copy_to_clipboard = Button(window, text="Copy to clipboard", height=2, width=15, command=copy_to_clipboard)

# layout grid
top_label.pack(pady=30)  # top Label
slider_password_length.pack(pady=20)  # character amount slider
slider_password_length.set(16)  # sets default character value
button_generate_password.pack(pady=20)  # Generate password button
text_display_password.pack()  # Text area
button_copy_to_clipboard.pack(pady=15)  # copy to clipboard

# runs program, do not touch!
window.mainloop()
