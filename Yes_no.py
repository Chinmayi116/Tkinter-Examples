from tkinter import *

root = Tk()
root.title("Agree")

agree = IntVar()

Checkbutton(root, text="I agree to the terms", variable=agree).pack()

def check():
    if agree.get() == 1:
        Label(root, text="You agreed").pack()
    else:
        Label(root, text="You did not agree").pack()

Button(root, text="Check", command=check).pack()

root.mainloop()
