from tkinter import *
from tkinter import messagebox

def submitted():
    messagebox.showinfo("Success", f"Form Submitted!")

window = Tk()
window.geometry("600x400")
choice = IntVar()
window.title("Simple Registration Form")

Label(window, text="First Name", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
Label(window, text="Middle Name", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10)
Label(window, text="Last Name", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=10)
Label(window, text="Gender", font=("Arial", 14)).grid(row=3, column=0)

Radiobutton(window, text="Female", variable=choice, value=1, font=("Arial", 12)).grid(row=3, column=1)
Radiobutton(window, text="Male", variable=choice, value=2, font=("Arial", 12)).grid(row=3, column=2)

Label(window, text="Mobile No", font=("Arial", 14)).grid(row=4, column=0, padx=10, pady=10)
Label(window, text="Address", font=("Arial", 14)).grid(row=5, column=0, padx=10, pady=10)

e1 = Entry(window, font=("Arial", 12))
e1.grid(row=0, column=1, padx=10, pady=10)

e2 = Entry(window, font=("Arial", 12))
e2.grid(row=1, column=1, padx=10, pady=10)

e3 = Entry(window, font=("Arial", 12))
e3.grid(row=2, column=1, padx=10, pady=10)

e5 = Entry(window, font=("Arial", 12))
e5.grid(row=4, column=1, padx=10, pady=10)

e6 = Entry(window, font=("Arial", 12))
e6.grid(row=5, column=1, padx=10, pady=10)

Button(window, text="Submit", bg="skyblue", font=("Arial", 12, "bold"), command=submitted).grid(row=6, column=2, pady=20)

window.mainloop()
