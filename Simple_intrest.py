entry_t.delete(0, END)
entry_si.delete(0, END)

# Labels
Label(root, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=5)
Label(root, text="Rate of Interest:").grid(row=1, column=0, padx=10, pady=5)
Label(root, text="Duration (Years):").grid(row=2, column=0, padx=10, pady=5)
Label(root, text="Simple Interest:").grid(row=4, column=0, padx=10, pady=5)

# Entry boxes
entry_p = Entry(root)
entry_r = Entry(root)
