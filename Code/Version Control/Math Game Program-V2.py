# ===== Importing modules =====

import tkinter as tk
from tkinter import messagebox
import os

TXT_FILE = "Login.txt"

root = None


# ===== File Handling =====

def file_exist():
    """Create the login file if it does not exist."""
    if not os.path.exists(TXT_FILE):
        with open(TXT_FILE, "w", encoding="utf-8") as f:
            f.write("student,student123\n")


def load_info():
    """Load usernames and passwords from the text file."""
    creds = {}

    with open(TXT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if "," in line:
                username, password = line.split(",", 1)
                creds[username.strip()] = password.strip()

    return creds


def save_info(username, password):
    """Save a new account."""
    with open(TXT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{password}\n")


# ===== Login =====

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showerror(
            "Error",
            "Please enter both username and password."
        )
        return

    creds = load_info()

    if username in creds and creds[username] == password:
        messagebox.showinfo(
            "Success",
            f"Welcome, {username}!"
        )
    else:
        messagebox.showerror(
            "Error",
            "Invalid username or password."
        )


# ===== Create Account =====

def create_acc():
    acc_window = tk.Toplevel(root)
    acc_window.title("Create Account")
    acc_window.geometry("400x250")
    acc_window.resizable(False, False)

    tk.Label(
        acc_window,
        text="Create New Account",
        font=("Helvetica", 16, "bold")
    ).pack(pady=15)

    tk.Label(acc_window, text="Username").pack()
    user_entry = tk.Entry(acc_window, width=30)
    user_entry.pack(pady=5)

    tk.Label(acc_window, text="Password").pack()
    pass_entry = tk.Entry(acc_window, width=30, show="*")
    pass_entry.pack(pady=5)

    def save():
        username = user_entry.get().strip()
        password = pass_entry.get().strip()

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "Please fill in all fields."
            )
            return

        creds = load_info()

        if username in creds:
            messagebox.showerror(
                "Error",
                "Username already exists."
            )
            return

        save_info(username, password)

        messagebox.showinfo(
            "Success",
            "Account created successfully."
        )

        acc_window.destroy()

    tk.Button(
        acc_window,
        text="Save",
        width=15,
        command=save
    ).pack(pady=20)


# ===== Forgot Password =====

def forgot_pass():
    pass_window = tk.Toplevel(root)
    pass_window.title("Forgot Password")
    pass_window.geometry("400x200")
    pass_window.resizable(False, False)

    tk.Label(
        pass_window,
        text="Forgot Password",
        font=("Helvetica", 16, "bold")
    ).pack(pady=15)

    tk.Label(pass_window, text="Username").pack()

    user_entry = tk.Entry(pass_window, width=30)
    user_entry.pack(pady=5)

    def find():
        username = user_entry.get().strip()

        creds = load_info()

        if username in creds:
            messagebox.showinfo(
                "Password Found",
                f"Password: {creds[username]}"
            )
        else:
            messagebox.showerror(
                "Error",
                "Username not found."
            )

    tk.Button(
        pass_window,
        text="Find Password",
        width=15,
        command=find
    ).pack(pady=20)


# ===== Main Login Window =====

def launch():
    global root
    global username_entry
    global password_entry

    root = tk.Tk()

    root.title("Flow Computing")
    root.geometry("600x450")
    root.resizable(False, False)
    root.configure(bg="#d9d9d9")

    main_frame = tk.Frame(
        root,
        bg="white",
        relief="solid",
        borderwidth=1,
        width=450,
        height=350
    )

    main_frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    #main_frame.pack_propagate(False)

    welcome_label = tk.Label(
        main_frame,
        text="Welcome",
        font=("Helvetica", 24, "bold"),
        bg="white"
    )

    welcome_label.pack(pady=(30, 40))

    login_frame = tk.Frame(
        main_frame,
        bg="white"
    )

    login_frame.pack(pady=10)

    tk.Label(
        login_frame,
        text="Username:",
        font=("Helvetica", 12),
        bg="white"
    ).grid(row=0, column=0, sticky="w", pady=10)

    username_entry = tk.Entry(
        login_frame,
        width=25
    )

    username_entry.grid(
        row=0,
        column=1,
        pady=10
    )

    tk.Label(
        login_frame,
        text="Password:",
        font=("Helvetica", 12),
        bg="white"
    ).grid(row=1, column=0, sticky="w", pady=10)

    password_entry = tk.Entry(
        login_frame,
        width=25,
        show="*"
    )

    password_entry.grid(
        row=1,
        column=1,
        pady=10
    )

    tk.Button(
        main_frame,
        text="Login",
        width=20,
        bg="green",
        fg="white",
        command=login
    ).pack(pady=25)

    bottom_frame = tk.Frame(
        main_frame,
        bg="white"
    )

    bottom_frame.pack(side="bottom", pady=25)

    tk.Button(
        bottom_frame,
        text="Create Account",
        width=16,
        command=create_acc
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        bottom_frame,
        text="Forgot Password",
        width=16,
        command=forgot_pass
    ).grid(row=0, column=1, padx=10)

    root.mainloop()


# ===== Start Program =====

file_exist()
launch()
