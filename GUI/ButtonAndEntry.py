#!/usr/bin/python

from tkinter import *
from tkinter import ttk
root = Tk()

entry1 = ttk.Entry(root, width=40)
entry1.pack()

image = PhotoImage(file="source.gif").subsample(6, 6)

bu1 = ttk.Button(root, text="Get Text")
bu1.pack()
bu1.config(image=image, compound=CENTER)


def button_click():
    var = entry1.get()
    if var != "":
        print(entry1.get())
        entry1.delete(0,END)

bu1.config(command=button_click)

root.mainloop()
