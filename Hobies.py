import tkinter as tk

root = tk.Tk()
root.title("Checkbox & Radio Button Example")
root.geometry("350x300")

# Function to show selected values
def show_selection():
    hobbies = []
    if var1.get():
        hobbies.append("Music")
    if var2.get():
        hobbies.append("Reading")
    if var3.get():
        hobbies.append("Traveling")

    gender = gender_var.get()

    result = "Hobbies: " + ", ".join(hobbies) + "\nGender: " + gender
    label_result.config(text=result)

# Checkbox variables
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

# Radio button variable
gender_var = tk.StringVar(value="None")

# Labels
tk.Label(root, text="Select your hobbies:").pack(anchor="w", padx=20, pady=5)

# Checkboxes
tk.Checkbutton(root, text="Music", variable=var1).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Reading", variable=var2).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Traveling", variable=var3).pack(anchor="w", padx=40)

# Radio Buttons
tk.Label(root, text="Select your gender:").pack(anchor="w", padx=20, pady=10)

tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack(anchor="w", padx=40)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack(anchor="w", padx=40)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack(anchor="w", padx=40)

# Button
tk.Button(root, text="Show Selection", command=show_selection).pack(pady=15)

# Result Label
label_result = tk.Label(root, text="", fg="blue")
label_result.pack(pady=10)

root.mainloop()
