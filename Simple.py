import tkinter as tk

def calculate():
    p = float(entry_p.get())
    r = float(entry_r.get())
    t = float(entry_t.get())
    
    si = (p * r * t) / 100
    label_result.config(text="Simple Interest: " + str(si))

root = tk.Tk()
root.title("Simple Interest Calculator")

tk.Label(root, text="Principal").grid(row=0, column=0)
entry_p = tk.Entry(root)
entry_p.grid(row=0, column=1)

tk.Label(root, text="Rate").grid(row=1, column=0)
entry_r = tk.Entry(root)
entry_r.grid(row=1, column=1)

tk.Label(root, text="Time").grid(row=2, column=0)
entry_t = tk.Entry(root)
entry_t.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
