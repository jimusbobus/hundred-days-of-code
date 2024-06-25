from tkinter import *


def calculate():
    miles = float(miles_entry.get())
    km = miles * 1.60934
    km_val_lab.config(text=str(round(km, 2)))


win = Tk()
win.title("gui")
win.minsize(width=300, height=200)
win.config(padx=25, pady=25)

default_miles = StringVar(win, value='0')

miles_entry = Entry(width=10, textvariable=default_miles)
miles_entry.grid(column=1, row=0)

miles_lab = Label(text='Miles')
miles_lab.grid(column=2, row=0)

miles_lab = Label(text='is equal to')
miles_lab.grid(column=0, row=1)

km_lab = Label(text='Km')
km_lab.grid(column=2, row=1)

km_val_lab = Label(text='0')
km_val_lab.grid(column=1, row=1)

b = Button(text='Calculate', command=calculate)
b.grid(column=1, row=2)

win.mainloop()
