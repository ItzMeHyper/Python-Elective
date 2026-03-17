import tkinter as tk

def area():
    l = float(length.get())
    w = float(width.get())
    result.config(text="Area = "+str(l*w))

root = tk.Tk()

tk.Label(root,text="Length").grid(row=0,column=0)
tk.Label(root,text="Width").grid(row=1,column=0)

length = tk.Entry(root)
width = tk.Entry(root)

length.grid(row=0,column=1)
width.grid(row=1,column=1)

tk.Button(root,text="Calculate",command=area).grid(row=2,column=0)

result = tk.Label(root,text="")
result.grid(row=2,column=1)

root.mainloop()