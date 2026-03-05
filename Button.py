from tkinter import *

def click():
    label.config(text="Button Clicked!")

root = Tk()
root.title("Button Example")
root.geometry("300x200")

label = Label(root, text="Click the button")
label.pack()

btn = Button(root, text="Click Me", command=click)
btn.pack()

root.mainloop()
