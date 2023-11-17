# Sumbitted By:
#     Muhammad Saim Sajid
# Roll no:
#     F21BSEEN1E02025
# Project:
#     Login Page In Tkinter
# Semester:
#     5th 
# Section:
#     E1
# Sumbitted To:
#     Sir Nauman


import tkinter as tk
from tkinter import messagebox

def check_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == "user" and entered_password == "password":
        messagebox.showinfo("Login Successful", "Welcome, {}".format(entered_username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


root = tk.Tk()
root.title("Login Program")


tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")  

username_entry.grid(row=0, column=1, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=check_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
