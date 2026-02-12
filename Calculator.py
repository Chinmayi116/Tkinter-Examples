import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Mini Calculator")
root.geometry("260x320")

entry = tk.Entry(root, font=("Arial", 18), bd=5, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.X, padx=10, pady=10)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0
for btn in buttons:
    action = lambda x=btn: calculate() if x == '=' else click(x)
    tk.Button(frame, text=btn, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Clear", width=20, height=2, command=clear).pack(pady=10)

root.mainloop()
