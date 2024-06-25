from tkinter import *


def cb():
    print("clicked")
    lab.config(text=inp.get())


win = Tk()
win.title("gui")
win.minsize(width=500, height=400)
win.config(padx=100, pady=100)

lab = Label(text='label', font=("Arial", 24, "italic"))
lab.grid(column=0, row=0)

b = Button(text='CLick me', command=cb)
b.grid(column=1, row=1)

inp = Entry(width=10)
inp.grid(column=3, row=2)

bn = Button(text='new button', command=cb)
bn.grid(column=2, row=0)

# area = Text(height=5, width=20)
# area.pack()

win.mainloop()

# def add(*args):
#     _sum = sum(args)
#     print(_sum)
#     return _sum
#
#
# def cal(n, **kwargs):
#     print(kwargs)
#
#
# total = add(1, 2, 3, 4, 5)
#
# cal(1, char='a', bool=True)
