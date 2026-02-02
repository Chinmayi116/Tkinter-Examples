from tkinter import *

def compute():
    b = float(e1.get())
    a = float(e2.get())
    d = float(e3.get())
    gross = b + a - d
    result_label.config(text="Gross Salary : ₹ " + str(gross))

windows = Tk()
windows.title("Gross Salary Calculator")
windows.geometry("300x250")

Label(windows, text="Basic Salary").grid(row=0, column=0, padx=10, pady=5)
Label(windows, text="Allowances").grid(row=1, column=0, padx=10, pady=5)
Label(windows, text="Deductions").grid(row=2, column=0, padx=10, pady=5)

e1 = Entry(windows)
e2 = Entry(windows)
e3 = Entry(windows)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(windows, text="Compute Gross Salary", command=compute).grid(
    row=3, column=0, columnspan=2, pady=10
)

result_label = Label(windows, text="", font=("Arial", 10, "bold"))
result_label.grid(row=4, column=0, columnspan=2)

windows.mainloop()
