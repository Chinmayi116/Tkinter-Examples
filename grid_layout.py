from tkinter import *
window=Tk()
window.title("Grid layout-Basic Demo")
window.geometry("300x400")

#Buttton placed using row and column
Button (window,text="Button1").grid(row=0,column=0)
Button (window,text="Button2").grid(row=0,column=1)
Button (window,text="Button3").grid(row=1,column=0)
Button (window,text="Button4").grid(row=1,column=1)
window.mainloop()