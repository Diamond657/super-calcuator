import tkinter as tk

# Define button colors
BUTTON_BG = "#2c3e50"        # Dark blue
BUTTON_FG = "#ffffff"
BUTTON_HIGHLIGHT = "#3498db" # Light blue
BUTTON_EQUAL = "#f39c12"     # Orange/yellow
BUTTON_CLEAR = "#39FF14" #Laser Green

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x500")
root.minsize(300, 400)

# Configure grid for responsiveness
for row in range(6):
    root.rowconfigure(row, weight=1)
for col in range(4):
    root.columnconfigure(col, weight=1)

# Display entry field
entry = tk.Entry(root, font=("Arial", 30), justify="right", bd=5)
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
    elif value == "CE":
        current = entry.get()
        updated = current[:-1]
        entry.delete(0, tk.END)
        entry.insert(0, updated)
    else:
        entry.insert(tk.END, value)

# Button layout
buttons = [
    [("C", BUTTON_HIGHLIGHT), ("CE", BUTTON_CLEAR), ("/", BUTTON_BG), ("%", BUTTON_BG)],
    [("7", BUTTON_BG), ("8", BUTTON_BG), ("9", BUTTON_BG), ("*", BUTTON_BG)],
    [("4", BUTTON_BG), ("5", BUTTON_BG), ("6", BUTTON_BG), ("-", BUTTON_BG)],
    [("1", BUTTON_BG), ("2", BUTTON_BG), ("3", BUTTON_BG), ("+", BUTTON_BG)],
    [("0", BUTTON_BG), ("00", BUTTON_BG), (".", BUTTON_BG), ("=", BUTTON_EQUAL)],
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
        btn.grid(row=r+1, column=c, sticky="nsew", padx=5, pady=5)

root.mainloop()