import tkinter as tk

def action():
    val = entry.get()
    label.config(text="Content: " + val)

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Click", command=action)
btn.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()