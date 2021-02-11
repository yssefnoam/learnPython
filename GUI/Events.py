#!/usr/bin/python

from tkinter import *
from tkinter import ttk
root = Tk()


def key_press(event):
    print("type {}".format(event.type))
    print("ctrl+C")

root.bind('<Control-c>', key_press)
root.mainloop()
