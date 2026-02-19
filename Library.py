import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x500")

        self.books = {}

        title = tk.Label(root, text="Library Management System",
                         font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Book Name
        tk.Label(root, text="Book Name").pack()
        self.book_entry = tk.Entry(root, width=30)
        self.book_entry.pack(pady=5)

        # Author Name
        tk.Label(root, text="Author Name").pack()
        self.author_entry = tk.Entry(root, width=30)
        self.author_entry.pack(pady=5)

        # Buttons
        tk.Button(root, text="Add Book", width=20,
                  command=self.add_book).pack(pady=5)

        tk.Button(root, text="Issue Book", width=20,
                  command=self.issue_book).pack(pady=5)

        tk.Button(root, text="Return Book", width=20,
                  command=self.return_book).pack(pady=5)

        tk.Button(root, text="View Books", width=20,
                  command=self.view_books).pack(pady=5)

        tk.Button(root, text="Exit", width=20,
                  command=root.quit).pack(pady=5)

        # Display Area
        self.display_area = tk.Text(root, height=10, width=50)
        self.display_area.pack(pady=10)

    def add_book(self):
        book = self.book_entry.get()
        author = self.author_entry.get()

        if book == "" or author == "":
            messagebox.showwarning("Warning", "Please enter book and author")
            return

        self.books[book] = {"author": author, "status": "Available"}
        messagebox.showinfo("Success", f"{book} added successfully")

        self.book_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)

    def issue_book(self):
        book = self.book_entry.get()

        if book in self.books:
            if self.books[book]["status"] == "Available":
                self.books[book]["status"] = "Issued"
                messagebox.showinfo("Success", f"{book} issued successfully")
            else:
                messagebox.showerror("Error", "Book already issued")
        else:
            messagebox.showerror("Error", "Book not found")

        self.book_entry.delete(0, tk.END)

    def return_book(self):
        book = self.book_entry.get()

        if book in self.books:
            if self.books[book]["status"] == "Issued":
                self.books[book]["status"] = "Available"
                messagebox.showinfo("Success", f"{book} returned successfully")
            else:
                messagebox.showwarning("Warning", "Book was not issued")
        else:
            messagebox.showerror("Error", "Book not found")

        self.book_entry.delete(0, tk.END)

    def view_books(self):
        self.display_area.delete(1.0, tk.END)

        if not self.books:
            self.display_area.insert(tk.END, "No books in library\n")
            return

        for book, details in self.books.items():
            self.display_area.insert(
                tk.END,
                f"Book: {book} | Author: {details['author']} | Status: {details['status']}\n"
            )


# Main Window
root = tk.Tk()
app = Library(root)
root.mainloop()
