from tkinter import *
from tkinter import messagebox

def check_even_odd():
    try:
        num = int(entry.get())
        if num % 2 == 0:
            messagebox.showinfo("Result", f"{num} is an EVEN number")
        else:
            messagebox.showinfo("Result", f"{num} is an ODD number")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

# Create window
window = Tk()
window.title("Even or Odd Checker")
window.geometry("400x250")

# Widgets
Label(window, text="Enter a Number:", font=("Arial", 14)).pack(pady=20)
entry = Entry(window, font=("Arial", 14))
entry.pack(pady=10)

Button(window, text="Check", font=("Arial", 12), command=check_even_odd).pack(pady=20)

# Run app
window.mainloop()
