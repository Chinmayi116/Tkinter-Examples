from tkinter import *

# Create window
root = Tk()
root.title("Employee Registration Form")
root.geometry("400x350")

# Heading
Label(root, text="Employee Registration Form", font=("Arial",14)).grid(row=0, column=1)

# Labels
Label(root, text="Employee ID").grid(row=1, column=0)
Label(root, text="Name").grid(row=2, column=0)
Label(root, text="Address").grid(row=3, column=0)
Label(root, text="Phone").grid(row=4, column=0)
Label(root, text="Department").grid(row=5, column=0)

# Entry fields
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)

# Save Function
def save():
    print("Employee ID:", e1.get())
    print("Name:", e2.get())
    print("Address:", e3.get())
    print("Phone:", e4.get())
    print("Department:", e5.get())
    print("----------------------")

# Clear Function
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

# Buttons
Button(root, text="Save", command=save, bg="lightgreen").grid(row=6, column=0)
Button(root, text="Clear", command=clear, bg="lightcoral").grid(row=6, column=1)

# Run window
root.mainloop()
