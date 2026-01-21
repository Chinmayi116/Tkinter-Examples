from tkinter import *
window=Tk()
window.title("Entry widget")
def submit():
    value=Entry.get()
    print("User entered: ",value)
Entry=Entry(window)
Entry.pack()
submit_button=Button(window,text="Submit",command="Submit")
submit_button.pack()
window.mainloop()