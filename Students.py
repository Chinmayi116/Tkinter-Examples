from tkinter import *

def submit():
    name = e1.get()
    usn = e2.get()
    course = e3.get()
    phone = e4.get()

    result.config(text="Registration Successful\nName: "+name)

root = Tk()
root.title("Student Registration Form")
root.geometry("400x300")

Label(root, text="Student Registration Form", font=("Arial",16)).grid(row=0, column=1)

Label(root, text="Name").grid(row=1, column=0)
Label(root, text="USN").grid(row=2, column=0)
Label(root, text="Course").grid(row=3, column=0)
Label(root, text="Phone").grid(row=4, column=0)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)

Button(root, text="Submit", command=submit).grid(row=5, column=1)

result = Label(root, text="")
result.grid(row=6, column=1)

root.mainloop()
