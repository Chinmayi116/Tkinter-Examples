import tkinter as tk
from tkinter import ttk, messagebox

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("850x500")

        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.dept_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.search_var = tk.StringVar()

        title = tk.Label(root, text="Student Management System", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        frame = tk.Frame(root, bd=3, relief=tk.RIDGE)
        frame.place(x=10, y=60, width=400, height=200)

        tk.Label(frame, text="Student ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(frame, textvariable=self.id_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Name").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(frame, textvariable=self.name_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Department").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(frame, textvariable=self.dept_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame, text="Phone").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(frame, textvariable=self.phone_var).grid(row=3, column=1, padx=10, pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.place(x=10, y=270, width=400, height=150)

        tk.Button(btn_frame, text="Add", width=12, command=self.add_student).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Update", width=12, command=self.update_student).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(btn_frame, text="Delete", width=12, command=self.delete_student).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Clear", width=12, command=self.clear_fields).grid(row=1, column=1, padx=10, pady=10)

        # Table
        table_frame = tk.Frame(root, bd=3, relief=tk.RIDGE)
        table_frame.place(x=420, y=60, width=420, height=360)

        self.tree = ttk.Treeview(table_frame, columns=("id","name","dept","phone"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("dept", text="Department")
        self.tree.heading("phone", text="Phone")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.bind("<ButtonRelease-1>", self.get_data)

    def add_student(self):
        if self.id_var.get()=="":
            messagebox.showerror("Error", "Student ID required")
            return
        self.tree.insert("", tk.END, values=(
            self.id_var.get(),
            self.name_var.get(),
            self.dept_var.get(),
            self.phone_var.get()
        ))
        self.clear_fields()

    def get_data(self, ev):
        selected = self.tree.focus()
        data = self.tree.item(selected, "values")
        if data:
            self.id_var.set(data[0])
            self.name_var.set(data[1])
            self.dept_var.set(data[2])
            self.phone_var.set(data[3])

    def update_student(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a student")
            return
        self.tree.item(selected, values=(
            self.id_var.get(),
            self.name_var.get(),
            self.dept_var.get(),
            self.phone_var.get()
        ))

    def delete_student(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a student")
            return
        self.tree.delete(selected)

    def clear_fields(self):
        self.id_var.set("")
        self.name_var.set("")
        self.dept_var.set("")
        self.phone_var.set("")


root = tk.Tk()
app = StudentApp(root)
root.mainloop()
