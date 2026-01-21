from tkinter import *
window=Tk()
window.title("My first Button widget")

Button=Button(window,text="Click me",command="Button_click")
Button.pack()
window.mainloop()