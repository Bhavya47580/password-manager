import tkinter as tk
from tkinter import messagebox
import random
import string

passwords = {}

# Load passwords from file
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            if ":" in line:
                site, pswd = line.strip().split(":", 1)
                passwords[site] = pswd
except FileNotFoundError:
    pass


# Generate password
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#%^&*"
    pswd = "".join(random.choice(chars) for _ in range(10))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, pswd)


# Save password
def save_password():
    site = website_entry.get().strip().lower()
    pswd = password_entry.get().strip()

    if site == "" or pswd == "":
        messagebox.showwarning("Error", "Fields cannot be empty!")
        return

    passwords[site] = pswd

    with open("passwords.txt", "w") as file:
        for s, p in passwords.items():
            file.write(f"{s}:{p}\n")

    messagebox.showinfo("Success", "Password Saved!")
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# Search password
def search_password():
    site = website_entry.get().strip().lower()

    if site in passwords:
        messagebox.showinfo("Result", f"Password: {passwords[site]}")
    else:
        messagebox.showerror("Error", "Website not found!")


# Delete password
def delete_password():
    site = website_entry.get().strip().lower()

    if site in passwords:
        del passwords[site]

        with open("passwords.txt", "w") as file:
            for s, p in passwords.items():
                file.write(f"{s}:{p}\n")

        messagebox.showinfo("Deleted", "Password deleted!")
    else:
        messagebox.showerror("Error", "Website not found!")


# GUI window
root = tk.Tk()
root.title("Password Manager")
root.geometry("350x250")
root.configure(bg = "black")


# Labels
tk.Label(root, text="Website").grid(row=0, column=0, padx=10, pady=10)
website_entry = tk.Entry(root, width=30,fg="black")
website_entry.grid(row=0, column=1, padx=5, pady=10)


tk.Label(root, text="Password").grid(row=1,column=0,padx=10,pady=10)
password_entry = tk.Entry(root, width=30,fg="black")
password_entry.grid(row=1,column=1,padx=5,pady=10)


# Buttons
tk.Button(root, text="Generate Password", command=generate_password).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(root, text="Save", command=save_password).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(root, text="Search", command=search_password).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="Delete", command=delete_password).grid(row=5, column=0, columnspan=2, pady=5)


root.mainloop()