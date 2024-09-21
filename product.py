import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_text.delete(1.0, tk.END)  # Clear previous text
        result_text.insert(tk.END, f"Product: {product:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")


root = tk.Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")
root.configure(bg="#f0f0f0")  


description_label = tk.Label(root, text="This application calculates the product of two numbers.", bg="#f0f0f0", fg="#333")
description_label.pack(pady=10)


label1 = tk.Label(root, text="Enter first number:", bg="#f0f0f0", fg="#333")
label1.pack(pady=5)

entry1 = tk.Entry(root, bg="#ffffff", fg="#000000")
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter second number:", bg="#f0f0f0", fg="#333")
label2.pack(pady=5)

entry2 = tk.Entry(root, bg="#ffffff", fg="#000000")
entry2.pack(pady=5)


calculate_button = tk.Button(root, text="Calculate Product", command=calculate_product, bg="#4CAF50", fg="#ffffff")
calculate_button.pack(pady=20)


result_text = tk.Text(root, height=1, width=30, bg="#f0f0f0", fg="#333")
result_text.pack(pady=10)


root.mainloop()
