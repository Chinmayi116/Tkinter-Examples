from tkinter import *
from tkinter import messagebox

def cal_marks():
    m1 = int(e1.get())
    m2 = int(e2.get())
    m3 = int(e3.get())

    total = m1 + m2 + m3
    percentage = total / 3

    messagebox.showinfo("Result", f"Total Marks = {total}\nPercentage = {percentage:.2f}%")

window = Tk()
window.geometry("500x300")
window.title("Student Marks Percentage")

Label(window, text="Student Marks Calculation", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

Label(window, text="1st Subject Marks").grid(row=1, column=0, padx=10, pady=5)
Label(window, text="2nd Subject Marks").grid(row=2, column=0, padx=10, pady=5)
Label(window, text="3rd Subject Marks").grid(row=3, column=0, padx=10, pady=5)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)

e1.grid(row=1, column=1, padx=10, pady=5)
e2.grid(row=2, column=1, padx=10, pady=5)
e3.grid(row=3, column=1, padx=10, pady=5)

Button(window, text="Calculate Percentage", command=cal_marks).grid(row=4, column=0, columnspan=2, pady=15)

window.mainloop()
