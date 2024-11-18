import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def submit_form():
    name = name_entry.get()
    age = age_var.get()
    file = file_var.get()
    if not name or not age or not file:
        messagebox.showerror("Error", "All fields are required!")
        return
    print(f"Name: {name}, Age: {age}, File: {file}")
    messagebox.showinfo("Success", "Form submitted successfully!")

def upload_file():
    file_var.set(filedialog.askopenfilename())

root = tk.Tk()
root.title("Healthcare Dashboard")

# Name
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Age
tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=10)
age_var = tk.StringVar()
age_dropdown = ttk.Combobox(root, textvariable=age_var, values=list(range(1, 101)))
age_dropdown.grid(row=1, column=1, padx=10, pady=10)

# File Upload
tk.Label(root, text="File Upload").grid(row=2, column=0, padx=10, pady=10)
file_var = tk.StringVar()
tk.Button(root, text="Browse", command=upload_file).grid(row=2, column=1, padx=10, pady=10)

# Submit Button
tk.Button(root, text="Submit", command=submit_form).grid(row=3, columnspan=2, pady=20)

root.mainloop()
