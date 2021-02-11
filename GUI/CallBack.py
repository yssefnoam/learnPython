#!/usr/bin/python

from tkinter import *
from tkinter import ttk
root = Tk()
button1 = ttk.Button(root, text="Click 1!")
button1.pack()
button2 = ttk.Button(root, text="Click 2!")
button2.pack()
button3 = ttk.Button(root, text="Click 3!")
button3.pack()


def button_click(x):
    print("Clicked{}".format(x))

button1.config(command=lambda: button_click(1))
button2.config(command=lambda: button_click(2))
button3.config(command=lambda: button_click(3))

root.mainloop()
