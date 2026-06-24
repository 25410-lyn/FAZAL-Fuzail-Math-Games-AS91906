# ===== Importing modules =====

import tkinter as tk
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both username and password")
        return

    print("Logged in:", username)


def launch_start_window():
    start = tk.Tk()
    start.title("Welcome")
    start.geometry("1600x900")
    start.configure(bg="#d9d9d9")

    main_frame = tk.Frame(
        start,
        bg="white",
        relief="solid",
        borderwidth=1,
        width=600,
        height=500
    )

    main_frame.place(relx=0.5, rely=0.5, anchor="center")
    

    welcome_label = tk.Label(
        main_frame,
        text="Welcome",
        font=("Helvetica", 24, "bold"),
        bg="white"
    )
    welcome_label.pack(pady=(40, 60))

    login_frame = tk.Frame(main_frame, bg="white")
    login_frame.pack()

    tk.Label(
        login_frame,
        text="Username: ",
        font=("Helvetica", 12),
        bg="white"
    ).grid(row=0, column=0, sticky="w", pady=5)

    global username_entry
    username_entry = tk.Entry(login_frame, width=30)
    username_entry.grid(row=0, column=1, pady=5)

    tk.Label(
        login_frame,
        text="Password: ",
        font=("Helvetica", 12),
        bg="white"
    ).grid(row=1, column=0, sticky="w", pady=5)

    global password_entry
    password_entry = tk.Entry(login_frame, width=30, show="*")
    password_entry.grid(row=1, column=1, pady=5)

    tk.Button(
        main_frame,
        text="Login",
        width=20,
        command=login,
        bg="green").pack(pady=30)

    bottom_frame = tk.Frame(main_frame, bg="white")
    bottom_frame.pack(side="bottom", pady=30)

    tk.Button(
        bottom_frame,
        text="Create New Account",
        width=18,
        bg="yellow"
    ).grid(row=0, column=0, padx=15)

    tk.Button(
        bottom_frame,
        text="Forgot Password",
        width=18,
        bg="red"
    ).grid(row=0, column=1, padx=15)

    start.mainloop()


launch_start_window()