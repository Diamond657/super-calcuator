import tkinter as tk

# Define button colors
BUTTON_BG = "#2c3e50"        # Dark blue
BUTTON_FG = "#ffffff"
BUTTON_HIGHLIGHT = "#3498db" # Light blue
BUTTON_EQUAL = "#f39c12"     # Orange/yellow

# Create the main window
root = tk.Tk()
root.title("Styled Calculator")
root.geometry("350x500")
root.minsize(300, 400)

# Configure grid for responsiveness
for row in range(6):
    root.rowconfigure(row, weight=1)
for col in range(4):
    root.columnconfigure(col, weight=1)

# Display entry field
entry = tk.Entry(root, font=("Arial", 28), justify="right", bd=5)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Function for button clicks
def on_click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Button layout
buttons = [
    [("C", BUTTON_HIGHLIGHT), ("/", BUTTON_BG), ("%", BUTTON_BG), ("*", BUTTON_BG)],
    [("7", BUTTON_BG), ("8", BUTTON_BG), ("9", BUTTON_BG), ("-", BUTTON_BG)],
    [("4", BUTTON_BG), ("5", BUTTON_BG), ("6", BUTTON_BG), ("+", BUTTON_BG)],
    [("1", BUTTON_BG), ("2", BUTTON_BG), ("3", BUTTON_BG), ("=", BUTTON_EQUAL)],
    [("0", BUTTON_BG), ("00", BUTTON_BG), (".", BUTTON_BG)],
]

# Add all buttons
for r, row in enumerate(buttons):
    for c, (text, color) in enumerate(row):
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 20),
            bg=color,
            fg=BUTTON_FG,
            activebackground=color,
            activeforeground="white",
            bd=0,
            command=lambda val=text: on_click(val)
        )
        
        # Special handling for "=" to span 1 row
        if text == "=":
            btn.grid(row=r+1, column=c, sticky="nsew", padx=5, pady=5)
        else:
            btn.grid(row=r+1, column=c, sticky="nsew", padx=5, pady=5)

# Fill the last empty cell (bottom-right) so layout balances
tk.Label(root, bg="#dfe6e9").grid(row=5, column=3, sticky="nsew")

root.mainloop()