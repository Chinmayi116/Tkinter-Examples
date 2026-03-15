from tkinter import *

# Create window
root = Tk()
root.title("Employee Registration Form")
root.geometry("400x400")

# Labels
Label(root, text="Employee Registration Form", font=("Arial",14)).grid(row=0, column=1)

Label(root, text="Employee ID").grid(row=1, column=0)
Label(root, text="Name").grid(row=2, column=0)
Label(root, text="Address").grid(row=3, column=0)
Label(root, text="Phone").grid(row=4, column=0)
Label(root, text="Department").grid(row=5, column=0)

# Entry boxes
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

# Function
def submit():
    empid = e1.get()
    name = e2.get()
    address = e3.get()
    phone = e4.get()
    dept = e5.get()

    print("Employee ID:", empid)
    print("Name:", name)
    print("Address:", address)
    print("Phone:", phone)
    print("Department:", dept)

# Button
Button(root, text="Submit", command=submit).grid(row=6, column=1)

# Run window
root.mainloop()
