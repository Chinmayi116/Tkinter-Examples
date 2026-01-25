from tkinter import *

# Create window
root = Tk()
root.title("My First Tkinter App")
root.geometry("300x200")

# Function for button click
def say_hello():
    name = entry.get()
    label_result.config(text="Hello " + name)

# Label
label = Label(root, text="Enter your name:")
label.pack(pady=10)

# Entry box
entry = Entry(root)
entry.pack(pady=5)

# Button
button = Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)

# Result Label
label_result = Label(root, text="")
label_result.pack(pady=10)

# Run the app
root.mainloop()
