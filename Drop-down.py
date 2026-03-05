from tkinter import *

def submit():
    name = e1.get()
    usn = e2.get()
    course = course_var.get()
    phone = e3.get()

    result.config(text="Registered Successfully\nName: " + name + "\nCourse: " + course)

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

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=4, column=1)

# Dropdown menu for course
course_var = StringVar()
course_var.set("BCA")

courses = ["BCA", "BBA", "BCom", "BA", "BSc"]
drop = OptionMenu(root, course_var, *courses)
drop.grid(row=3, column=1)

Button(root, text="Submit", command=submit).grid(row=5, column=1)

result = Label(root, text="")
result.grid(row=6, column=1)

root.mainloop()
