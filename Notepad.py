import tkinter as tk
from tkinter import filedialog

def open_file():
    file = filedialog.askopenfile(mode='r')
    if file:
        text.delete(1.0, tk.END)
        text.insert(tk.END, file.read())

def save_file():
    file = filedialog.asksaveasfile(mode='w')
    if file:
        file.write(text.get(1.0, tk.END))

root = tk.Tk()
root.title("Notepad")

text = tk.Text(root)
text.pack()

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

root.mainloop()
