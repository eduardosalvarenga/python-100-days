# Create a Mile to KM converter using Tkinter

from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=200, height=30)
window.config(padx=10, pady=10)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

result_label = Label(text="is equal to")
result_label.grid(column=3, row=0)

km_label = Label(text="0")
km_label.grid(column=4, row=0)

km_text = Label(text="Km")
km_text.grid(column=5, row=0)


def calculate():
    miles = float(miles_input.get())
    km = "{0:.2f}".format(miles * 1.609344)
    km_label["text"] = km


button = Button(text="Convert", command=calculate)
button.grid(column=5, row=3)


window.mainloop()
