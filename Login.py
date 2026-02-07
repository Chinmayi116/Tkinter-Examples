import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Form")
root.geometry("350x250")

# Function to check login
def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome, " + username)
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Title
tk.Label(root, text="Login Form", font=("Arial", 14, "bold")).pack(pady=10)

# Username
tk.Label(root, text="Username:").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

# Password
tk.Label(root, text="Password:").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

# Login Button
tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()
