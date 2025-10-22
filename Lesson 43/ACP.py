from tkinter import *
import random

root = Tk()
root.title=("Rock,Paper,Scissors!")
root.geometry("400x400")
root.config(bg="#f0f0f0")

choices = ("Rock","Paper","Scissors")

user_label = Label(root, text="My Turn!")
user_label.pack(pady=10)

result_label = Label(root, text="Let the games Begin")
result_label.pack(pady=10)

comp_label = Label(root,text="Your turn")
comp_label.pack(pady=10)

def play (user_choice):
    comp_choice = random.choice(choices)
    comp_label.config(text = f"I choose: {comp_choice}")

    if user_choice == comp_choice:
        result = "Its a draw!"
    
    elif (user_choice == "Rock" and comp_choice == "Paper") or \
         (user_choice == "Scissors" and comp_choice == "Rock") or \
         (user_choice == "Paper" and comp_choice == "Scissors") :
        result = "You win!"
    else:
        result = "I win! Better Luck next time!"
        result_label.config(text=result)

btn_frame = Frame(root)
btn_frame.pack(pady=20)

rock_btn = Button(btn_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = Button(btn_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = Button(btn_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

root.mainloop()
        
        
