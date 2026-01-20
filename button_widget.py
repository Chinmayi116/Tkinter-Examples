from tkinter import *

window = Tk()
window.title("Tkinter pack() demo")
window.geometry("400x300")

# Top button
btn_top = Button(window, text="Top", bg="lightblue")
btn_top.pack(side="top")

# Bottom button
btn_bottom = Button(window, text="Bottom", bg="lightgreen")
btn_bottom.pack(side="bottom")

# Left button
btn_left = Button(window, text="Left", bg="red")
btn_left.pack(side="left")

# Right button
btn_right = Button(window, text="Right", bg="yellow")
btn_right.pack(side="right")

window.mainloop()
