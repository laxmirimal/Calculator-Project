import tkinter as tk
from tkinter import messagebox
import time

# Function to perform arithmetic operations
def on_click(button):
    current_text = entry.get()
    if button == "=":
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            entry.delete(0, tk.END)
    elif button == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button)

# Function to add animation
def animate_button(button):
    button.config(bg="lightblue")
    time.sleep(0.1)
    button.config(bg="lightgray")

# Setting up main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")
root.config(bg="#333")

# Entry widget to display expression
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Buttons for calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, bg="lightgray",
                       command=lambda text=text: on_click(text))
    button.grid(row=row, column=col, padx=10, pady=10)
    button.bind("<Enter>", lambda e, b=button: animate_button(b))  # Animation on hover

# Main loop to run the application
root.mainloop()
