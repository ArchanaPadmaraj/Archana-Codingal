from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root = Tk()
root.title("Tkinter Basics")
root.geometry("400x400")

def show_img():
    img_window = Toplevel(root)
    img_window.title("Image Window")

    img = Image.open("images.jpg")
    img = img.resize((200,200))
    img_tk = ImageTk.PhotoImage(img)

    img_label = Label(img_window, image=img_tk)
    img_label.image = img_tk
    img_label.pack()

def show_message():
    messagebox.showinfo("Your img","Hello there!")

def open_top_window():
    top = Toplevel(root)
    top.title = ("Top Window")
    top.geometry = ("400x400")
    Label(top, text="New Top window!",font=("Arial",12).pack(pady=20))

button1 = Button(root, text = "show image", command=show_img)
button1.pack(pady= 10)

button2 = Button(root , text="show message box", command=show_message)
button2.pack(pady=10)

button3= Button(root, text="Open top window",command=open_top_window)
button3.pack(pady=10)

root.mainloop()