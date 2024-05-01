#Scientific Calci
import math
import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_entry():
    entry.delete(0, tk.END)

def insert_text(text):
    entry.insert(tk.END, text)

def calculate_trig(func):
    try:
        value = float(entry.get())
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def calculate_log():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def configure_fonts():
    # Calculate font size based on window width
    font_size = max(10, int(root.winfo_width() / 35))
    entry.configure(font=("Arial", font_size))
    for button in buttons:
        button[0].configure(font=("Arial", font_size))

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = []
button_texts = [
    ("sin", lambda: calculate_trig("sin")),
    ("cos", lambda: calculate_trig("cos")),
    ("tan", lambda: calculate_trig("tan")),
    ("^", lambda: insert_text("**")),
    (".", lambda: insert_text(".")),
    ("9", lambda: insert_text("9")),
    ("8", lambda: insert_text("8")),
    ("7", lambda: insert_text("7")),
    ("6", lambda: insert_text("6")),
    ("5", lambda: insert_text("5")),
    ("4", lambda: insert_text("4")),
    ("3", lambda: insert_text("3")),
    ("2", lambda: insert_text("2")),
    ("1", lambda: insert_text("1")),
    ("0", lambda: insert_text("0")),
    ("/", lambda: insert_text("/")),
    ("*", lambda: insert_text("*")),
    ("-", lambda: insert_text("-")),
    ("+", lambda: insert_text("+")),
    ("=", evaluate_expression),
    ("C", clear_entry),
    ("log", calculate_log)
]

row = 1
col = 0
for button_text, command in button_texts:
    button = tk.Button(root, text=button_text, padx=20, pady=10, command=command)
    button.grid(row=row, column=col, sticky="nsew")
    buttons.append((button, command))
    col += 1
    if col == 5:
        col = 0
        row += 1

# Configure column widths to be proportional to window width
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

# Configure row heights to be proportional to window height
for i in range(row + 1):
    root.grid_rowconfigure(i, weight=1)

# Bind configure_fonts function to window resize event
root.bind("<Configure>", lambda event: configure_fonts())

root.mainloop()
