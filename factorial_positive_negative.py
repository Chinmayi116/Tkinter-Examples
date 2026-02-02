from tkinter import *

def factorial():
    n = int(t1.get())
    f = 1
    for i in range(1, n+1):
        f = f * i
    t2.delete(0, END)
    t2.insert(0, f)

def check():
    n = int(t1.get())
    if n > 0:
        result = "Positive"
    elif n < 0:
        result = "Negative"
    else:
        result = "Zero"
    t2.delete(0, END)
    t2.insert(0, result)

windows = Tk()
windows.title("Number Operations")
windows.geometry("400x350")

Label(windows, text="Enter Number").grid(row=0, column=0)
t1 = Entry(windows)
t1.grid(row=0, column=1)

Button(windows, text="Factorial", command=factorial).grid(row=1, column=0)
Button(windows, text="Check + / - / 0", command=check).grid(row=1, column=1)

Label(windows, text="Result").grid(row=2, column=0)
t2 = Entry(windows)
t2.grid(row=2, column=1)

windows.mainloop()