import tkinter as tk
from tkinter import messagebox
from password import check_password_easy, check_password_hard, check_password_evil
import base64

# Encrypt and decrypt helpers
def encrypt_password(password):
    return base64.b64encode(password.encode()).decode()

def decrypt_password(encrypted):
    return base64.b64decode(encrypted.encode()).decode()

# Store login credentials globally for re-login
stored_user = ""
stored_pass = ""

# Call correct password checker based on selected mode
def validate_password_by_difficulty(password, mode):
    if mode == "Easy":
        return check_password_easy(password)
    elif mode == "Hard":
        return check_password_hard(password)
    elif mode == "Evil":
        return check_password_evil(password)
    return "Invalid mode selected."

# Validate first login
def validate_login():
    global stored_user, stored_pass

    userid = username_entry.get()
    password = password_entry.get()
    mode = difficulty_var.get()

    result = validate_password_by_difficulty(password, mode)

    if result is True:
        stored_user = userid
        stored_pass = password

        with open("user_credentials.txt", "w") as file:
            encrypted = encrypt_password(password)
            file.write(f"Username: {userid}\nPassword: {encrypted}")

        messagebox.showinfo("Login Successful", f"Welcome, {userid}! Please log in again. Hope you remember your password!")
        parent.withdraw()
        show_relogin_window(mode)
    else:
        messagebox.showerror("Login Failed", result)

# Validate second login
def validate_relogin():
    userid = username_entry2.get()
    password = password_entry2.get()

    if userid == stored_user and password == stored_pass:
        messagebox.showinfo("Re-login Successful", f"Completed {level_mode} mode")
        relogin_window.destroy()
        parent.destroy()
    else:
        messagebox.showerror("Login Failed", "Username or password incorrect.")

# Toggle password visibility
def toggle_password_visibility(entry, var):
    entry.config(show="" if var.get() else "*")

# Show the second login window
def show_relogin_window(mode):
    global relogin_window, username_entry2, password_entry2, level_mode

    level_mode = mode

    relogin_window = tk.Toplevel()
    relogin_window.title("Re-login")
    relogin_window.geometry("300x300")

    tk.Label(relogin_window, text="Userid:").pack()
    username_entry2 = tk.Entry(relogin_window)
    username_entry2.pack()

    tk.Label(relogin_window, text="Password:").pack()
    password_entry2 = tk.Entry(relogin_window, show="*")
    password_entry2.pack()

    show_var2 = tk.BooleanVar()
    show_button2 = tk.Checkbutton(relogin_window, text="Show Password", variable=show_var2,
                                  command=lambda: toggle_password_visibility(password_entry2, show_var2))
    show_button2.pack()

    login_button2 = tk.Button(relogin_window, text="Re-login", command=validate_relogin)
    login_button2.pack()

# Main login window
parent = tk.Tk()
parent.title("Login Form")
parent.geometry("300x300")

tk.Label(parent, text="Username:").pack()
username_entry = tk.Entry(parent)
username_entry.pack()

tk.Label(parent, text="Password:").pack()
password_entry = tk.Entry(parent, show="*")
password_entry.pack()

show_var = tk.BooleanVar()
show_button = tk.Checkbutton(parent, text="Show Password", variable=show_var,
                             command=lambda: toggle_password_visibility(password_entry, show_var))
show_button.pack()

tk.Label(parent, text="Select Difficulty:").pack()
difficulty_var = tk.StringVar(value="Easy")
difficulty_menu = tk.OptionMenu(parent, difficulty_var, "Easy", "Hard", "Evil")
difficulty_menu.pack()

login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

parent.mainloop()
