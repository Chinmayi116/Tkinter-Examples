import tkinter as tk

# Functions
def add():
    result.set(int(num1.get()) + int(num2.get()))

def sub():
    result.set(int(num1.get()) - int(num2.get()))

def mul():
    result.set(int(num1.get()) * int(num2.get()))

def div():
    if int(num2.get()) != 0:
        result.set(int(num1.get()) / int(num2.get()))
    else:
        result.set("Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Variables
num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

# Labels and Entry
tk.Label(root, text="Enter First Number").pack()
tk.Entry(root, textvariable=num1).pack()

tk.Label(root, text="Enter Second Number").pack()
tk.Entry(root, textvariable=num2).pack()

# Buttons
tk.Button(root, text="Add", command=add).pack(pady=5)
tk.Button(root, text="Subtract", command=sub).pack(pady=5)
tk.Button(root, text="Multiply", command=mul).pack(pady=5)
tk.Button(root, text="Divide", command=div).pack(pady=5)

# Result
tk.Label(root, text="Result").pack()
tk.Entry(root, textvariable=result).pack()

# Run
root.mainloop()
