from tkinter import *
from tkinter import messagebox

def cal_bill():
    q1 = int(e1.get())
    q2 = int(e2.get())
    q3 = int(e3.get())

    c1 = q1 * 500

    if q2 <= 50:
        c2 = q2 * 50
    else:
        c2 = q2 * 45

    if q3 < 10:
        messagebox.showwarning("Warning", "Cannot purchase anything below 10")
        c3 = 0
    else:
        c3 = q3 * 100

    total_bill = c1 + c2 + c3
    messagebox.showinfo("Billing Window", "Total bill is " + str(total_bill))


window = Tk()
window.geometry("500x300")
window.title("Product Billing System")

Label(window, text="Product 1").grid(row=0, column=0, padx=10, pady=10)
Label(window, text="Product 2").grid(row=1, column=0, padx=10, pady=10)
Label(window, text="Product 3").grid(row=2, column=0, padx=10, pady=10)

e1 = Entry(window)
e1.grid(row=0, column=1, padx=10, pady=10)

e2 = Entry(window)
e2.grid(row=1, column=1, padx=10, pady=10)

e3 = Entry(window)
e3.grid(row=2, column=1, padx=10, pady=10)

Button(window, text="Calculate Bill", command=cal_bill).grid(row=3, column=1, pady=20)

window.mainloop()
