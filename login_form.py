
import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Login Form")
root.geometry("620x700")
root.configure(bg="#0B3D2E")
root.resizable(False, False)

# Main Login Box - Gold Border
login_frame = tk.Frame(
    root,
    bg="#C9A227",
    width=475,
    height=580
)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

# Green Header
header_frame = tk.Frame(
    login_frame,
    bg="#0B3D2E",
    width=471,
    height=168
)
header_frame.place(x=2, y=2)

# User Login Title
title_label = tk.Label(
    header_frame,
    text="USER LOGIN",
    font=("Times New Roman", 36, "bold"),
    bg="#0B3D2E",
    fg="white"
)
title_label.place(relx=0.5, y=98, anchor="center")

# White Form Section
white_frame = tk.Frame(
    login_frame,
    bg="white",
    width=471,
    height=406
)
white_frame.place(x=2, y=170)

# Username
username_label = tk.Label(
    white_frame,
    text="Username",
    font=("Times New Roman", 16, "bold"),
    bg="white",
    fg="#0B3D2E"
)
username_label.place(x=55, y=25)

username_entry = tk.Entry(
    white_frame,
    font=("Times New Roman", 16),
    bg="#F5F5F0",
    fg="#0B3D2E",
    relief="solid",
    bd=1
)
username_entry.place(x=53, y=59, width=365, height=54)

# Password
password_label = tk.Label(
    white_frame,
    text="Password",
    font=("Times New Roman", 16, "bold"),
    bg="white",
    fg="#0B3D2E"
)
password_label.place(x=55, y=142)

password_entry = tk.Entry(
    white_frame,
    font=("Times New Roman", 16),
    bg="#F5F5F0",
    fg="#0B3D2E",
    relief="solid",
    bd=1,
    show="*"
)
password_entry.place(x=53, y=176, width=365, height=54)

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "12345":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid Username and Password!"
        )

# Login Button
login_button = tk.Button(
    white_frame,
    text="LOG IN",
    font=("Times New Roman", 18, "bold"),
    bg="#C9A227",
    fg="#0B3D2E",
    activebackground="#0B3D2E",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=login
)
login_button.place(x=93, y=254, width=288, height=65)

# Run Application
root.mainloop()
