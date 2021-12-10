# Create a password manager/generator

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = ("Arial", 10, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    login = login_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\nLogin: {login} \nPassword: {password}")

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"Website: {website}, Login: {login}, Password: {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                login_input.delete(0, END)
                login_input.insert(0, "email@email.com")
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

website_input = Entry(width=41)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

login_label = Label(text="Email/Username: ", font=FONT)
login_label.grid(column=0, row=2)

login_input = Entry(width=41)
login_input.grid(column=1, row=2, columnspan=2)
login_input.insert(0, "email@email.com")

password_label = Label(text="Password: ", font=FONT)
password_label.grid(column=0, row=3)

password_input = Entry(width=22)
password_input.grid(column=1, row=3)

generate_password_button = Button(width=15, text="Generate Password", command=pass_generator)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
