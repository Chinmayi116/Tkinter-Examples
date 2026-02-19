import tkinter as tk
from tkinter import messagebox


class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM System")
        self.root.geometry("400x350")

        self.balance = 0

        # Title Label
        self.title_label = tk.Label(root, text="Simple ATM Machine", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Amount Entry
        self.amount_label = tk.Label(root, text="Enter Amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack(pady=5)

        # Buttons
        self.deposit_btn = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_btn.pack(pady=5)

        self.withdraw_btn = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_btn.pack(pady=5)

        self.check_btn = tk.Button(root, text="Check Balance", command=self.check_balance)
        self.check_btn.pack(pady=5)

        self.exit_btn = tk.Button(root, text="Exit", command=root.quit)
        self.exit_btn.pack(pady=5)

    def deposit(self):
        try:
            amount = int(self.amount_entry.get())
            if amount > 0:
                self.balance += amount
                messagebox.showinfo("Success", f"Deposited ₹{amount}")
            else:
                messagebox.showwarning("Warning", "Enter valid amount")
        except:
            messagebox.showerror("Error", "Enter numbers only")

        self.amount_entry.delete(0, tk.END)

    def withdraw(self):
        try:
            amount = int(self.amount_entry.get())
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient Balance")
            elif amount <= 0:
                messagebox.showwarning("Warning", "Enter valid amount")
            else:
                self.balance -= amount
                messagebox.showinfo("Success", f"Withdrawn ₹{amount}")
        except:
            messagebox.showerror("Error", "Enter numbers only")

        self.amount_entry.delete(0, tk.END)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Current Balance: ₹{self.balance}")


# Main Window
root = tk.Tk()
app = ATM(root)
root.mainloop()
