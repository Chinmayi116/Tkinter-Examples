import tkinter as tk
from tkinter import messagebox

def check_answer():
    if answer.get() == "Python":
        messagebox.showinfo("Result", "Correct Answer!")
    else:
        messagebox.showerror("Result", "Wrong Answer!")

root = tk.Tk()
root.title("Quiz App")

question = tk.Label(root, text="Which language is used for AI?")
question.pack()

answer = tk.StringVar()

tk.Radiobutton(root, text="C", variable=answer, value="C").pack()
tk.Radiobutton(root, text="Java", variable=answer, value="Java").pack()
tk.Radiobutton(root, text="Python", variable=answer, value="Python").pack()

tk.Button(root, text="Submit", command=check_answer).pack()

root.mainloop()
