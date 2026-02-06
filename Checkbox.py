from tkinter import *

root = Tk()
root.title("Hobbies")

Label(root, text="Select your hobbies:").pack()

h1 = IntVar()
h2 = IntVar()
h3 = IntVar()

Checkbutton(root, text="Music", variable=h1).pack()
Checkbutton(root, text="Sports", variable=h2).pack()
Checkbutton(root, text="Reading", variable=h3).pack()

def show():
    result = "You selected:\n"
    if h1.get() == 1:
        result += "Music\n"
    if h2.get() == 1:
        result += "Sports\n"
    if h3.get() == 1:
        result += "Reading\n"
    Label(root, text=result).pack()

Button(root, text="Submit", command=show).pack()

root.mainloop()
