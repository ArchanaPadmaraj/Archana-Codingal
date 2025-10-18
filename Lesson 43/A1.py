from tkinter import *
from tkinter import messagebox

root = Tk()
root.title =("first window")
root.geometry = ("200x200")

def msg():
    messagebox.showwarning("Alert!Virus Detected")

button = Button(root,text="Scan for Virus",command=msg)
button.place(x=40, y=80)

root.mainloop()