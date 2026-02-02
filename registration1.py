from tkinter import *
from datetime import datetime

def check_eligibility():
    dob = entry_dob.get()   # format: YYYY
    year = int(dob)
    current_year = datetime.now().year
    age = current_year - year

    if age >= 18:
        result.set("Eligible for Voting")
    else:
        result.set("Not Eligible for Voting")

windows = Tk()
windows.title("Voter Eligibility Form")
windows.geometry("350x300")

Label(windows, text="Name").grid(row=0, column=0)
Label(windows, text="Address").grid(row=1, column=0)
Label(windows, text="Phone").grid(row=2, column=0)
Label(windows, text="Email").grid(row=3, column=0)
Label(windows, text="Year of Birth").grid(row=4, column=0)

entry_name = Entry(windows)
entry_address = Entry(windows)
entry_phone = Entry(windows)
entry_email = Entry(windows)
entry_dob = Entry(windows)

entry_name.grid(row=0, column=1)
entry_address.grid(row=1, column=1)
entry_phone.grid(row=2, column=1)
entry_email.grid(row=3, column=1)
entry_dob.grid(row=4, column=1)

Button(windows, text="Submit", command=check_eligibility).grid(row=5, column=0, columnspan=2, pady=10)

result = StringVar()
Label(windows, textvariable=result, fg="blue").grid(row=6, column=0, columnspan=2)

windows.mainloop()