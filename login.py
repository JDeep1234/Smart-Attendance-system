import tkinter as tk
from tkinter import messagebox
import subprocess

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        open_main_page()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_main_page():
    subprocess.run(["python", "main.py"])  # Execute main.py using subprocess

# Create the main window
window = tk.Tk()
window.title("Login Page")

# Create and place widgets
username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(window, text="Login", command=check_login)
login_button.grid(row=2, columnspan=2, padx=10, pady=5)

# Start the GUI event loop
window.mainloop()
