import tkinter as tk

def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    label_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Addition Program")

tk.Label(root, text="Enter First Number").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter Second Number").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Add", command=add).grid(row=2, column=0, columnspan=2)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()
