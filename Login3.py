import tkinter as tk
from tkinter import messagebox

def login():
    if username.get() == "admin" and password.get() == "1234":
        messagebox.showinfo("Login", "Success")
    else:
        messagebox.showerror("Login", "Invalid Details")

root = tk.Tk()
root.title("Login")

username = tk.StringVar()
password = tk.StringVar()

tk.Label(root, text="Username").pack()
tk.Entry(root, textvariable=username).pack()

tk.Label(root, text="Password").pack()
tk.Entry(root, textvariable=password, show="*").pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()
