import tkinter as tk

def calculate():
    total = int(m1.get()) + int(m2.get()) + int(m3.get())
    avg = total / 3
    
    result.set("Total: " + str(total) + " Avg: " + str(avg))

root = tk.Tk()
root.title("Result Calculator")

m1 = tk.StringVar()
m2 = tk.StringVar()
m3 = tk.StringVar()
result = tk.StringVar()

tk.Label(root, text="Subject 1").pack()
tk.Entry(root, textvariable=m1).pack()

tk.Label(root, text="Subject 2").pack()
tk.Entry(root, textvariable=m2).pack()

tk.Label(root, text="Subject 3").pack()
tk.Entry(root, textvariable=m3).pack()

tk.Button(root, text="Calculate", command=calculate).pack()

tk.Entry(root, textvariable=result).pack()

root.mainloop()p
