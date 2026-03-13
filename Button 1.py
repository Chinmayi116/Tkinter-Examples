from tkinter import *

root = Tk()

def click():
    print("Button Clicked")

button = Button(root, text="Click Me", command=click)
button.pack()

root.mainloop()
