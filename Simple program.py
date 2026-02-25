import tkinter as tk

def on_button_click():
    """Event handler for the button click."""
    label.config(text="Hello, Tkinter! Button Clicked!")

# 1. Create the main application window
root = tk.Tk()
root.title("Simple Tkinter Example")
root.geometry("300x200") # Set the window size

# 2. Add widgets to the window

# Create a Label widget
label = tk.Label(root, text="Click the button below", font=("Helvetica", 12))
label.pack(pady=20) # Place the label in the window with padding

# Create a Button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10) # Place the button in the window with padding

# 3. Enter the main event loop
# This keeps the window open and responsive to user actions
root.mainloop()
