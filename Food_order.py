from tkinter import *

root = Tk()
root.title("Food Order")

pizza = IntVar()
burger = IntVar()
pasta = IntVar()

Checkbutton(root, text="Pizza", variable=pizza).pack()
Checkbutton(root, text="Burger", variable=burger).pack()
Checkbutton(root, text="Pasta", variable=pasta).pack()

def order():
    order = "Your Order:\n"
    if pizza.get() == 1:
        order += "Pizza\n"
    if burger.get() == 1:
        order += "Burger\n"
    if pasta.get() == 1:
        order += "Pasta\n"
    Label(root, text=order).pack()

Button(root, text="Place Order", command=order).pack()

root.mainloop()
