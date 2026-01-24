from tkinter import *
from tkinter import messagebox

def add_numbers():
    try:
        a = int(e1.get())
        b = int(e2.get())
        result = a + b
        lbl_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers")

window = Tk()
window.title("Add Two Numbers")
window.geometry("300x250")

Label(window, text="Enter First Number").pack()
e1 = Entry(window)
e1.pack()

Label(window, text="Enter Second Number").pack()
e2 = Entry(window)
e2.pack()

Button(window, text="Add", command=add_numbers).pack(pady=10)

lbl_result = Label(window, text="", font=("Arial", 12))
lbl_result.pack()

window.mainloop()
