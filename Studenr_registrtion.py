from tkinter import *

def submit():
    name = e1.get()
    usn = e2.get()
    course = e3.get()
    event = e4.get()
    mobile = e5.get()
    
    result_label.config(text="Registration Successful!\n\n"
                             f"Name   : {name}\n"
                             f"USN    : {usn}\n"
                             f"Course : {course}\n"
                             f"Event  : {event}\n"
                             f"Mobile : {mobile}")

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    result_label.config(text="")

windows = Tk()
windows.title("Student Event Registration Form")
windows.geometry("420x460")

Label(windows, text="Student Registration Form", 
      font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

Label(windows, text="Student Name").grid(row=1, column=0, padx=10, pady=5, sticky=W)
Label(windows, text="USN").grid(row=2, column=0, padx=10, pady=5, sticky=W)
Label(windows, text="Course").grid(row=3, column=0, padx=10, pady=5, sticky=W)
Label(windows, text="Event Name").grid(row=4, column=0, padx=10, pady=5, sticky=W)
Label(windows, text="Mobile No").grid(row=5, column=0, padx=10, pady=5, sticky=W)

e1 = Entry(windows, width=30)
e2 = Entry(windows, width=30)
e3 = Entry(windows, width=30)
e4 = Entry(windows, width=30)
e5 = Entry(windows, width=30)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)

Button(windows, text="Submit", width=12, command=submit).grid(row=6, column=0, pady=12)
Button(windows, text="Clear", width=12, command=clear).grid(row=6, column=1, pady=12)

result_label = Label(windows, text="", fg="green", font=("Arial", 10, "bold"), justify=LEFT)
result_label.grid(row=7, column=0, columnspan=2, pady=10)

windows.mainloop()
