import tkinter as tk
from tkinter import messagebox

def check_fields():
    name = entry_name.get().strip()
    sid = entry_id.get().strip()
    pwd = entry_password.get().strip()

    if name and sid and pwd:
        submit_button.pack(pady=10)
    else:
        submit_button.pack_forget()

def login():
    name = entry_name.get().strip()
    sid = entry_id.get().strip()
    pwd = entry_password.get().strip()

    # You can add real validation here if needed
    messagebox.showinfo("Login Status", f"Login Successful!\nWelcome {name}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Student Information Form")
    root.geometry("350x250")

    tk.Label(root, text="Student Name").pack(pady=5)
    entry_name = tk.Entry(root)
    entry_name.pack()

    tk.Label(root, text="Student ID").pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack()

    tk.Label(root, text="Password").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    submit_button = tk.Button(root, text="Submit", command=login)
    submit_button.pack_forget()

    # Bind key events
    entry_name.bind("<KeyRelease>", lambda e: check_fields())
    entry_id.bind("<KeyRelease>", lambda e: check_fields())
    entry_password.bind("<KeyRelease>", lambda e: check_fields())

    root.mainloop()
