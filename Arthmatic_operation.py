from tkinter import *
from tkinter import messagebox

def calculate(op):
    try:
        a = float(e1.get())
        b = float(e2.get())

        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            if b == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = a / b

        lbl_result.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300")

Label(window, text="First Number").grid(row=0, column=0, padx=10, pady=10)
Label(window, text="Second Number").grid(row=1, column=0, padx=10, pady=10)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1, padx=10, pady=10)
e2.grid(row=1, column=1, padx=10, pady=10)

Button(window, text="Add", width=10, command=lambda: calculate("add")).grid(row=2, column=0, pady=10)
Button(window, text="Subtract", width=10, command=lambda: calculate("sub")).grid(row=2, column=1, pady=10)
Button(window, text="Multiply", width=10, command=lambda: calculate("mul")).grid(row=3, column=0, pady=10)
Button(window, text="Divide", width=10, command=lambda: calculate("div")).grid(row=3, column=1, pady=10)

lbl_result = Label(window, text="Result:", font=("Arial", 12))
lbl_result.grid(row=4, column=0, columnspan=2, pady=20)

window.mainloop()
