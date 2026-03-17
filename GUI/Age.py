import tkinter as tk
from datetime import date

def calculate_age():
    y = int(year.get())
    m = int(month.get())
    d = int(day.get())

    today = date.today()
    age = today.year - y
    result.config(text="Age: "+str(age))

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root,text="Year").grid(row=0,column=0)
tk.Label(root,text="Month").grid(row=0,column=1)
tk.Label(root,text="Day").grid(row=0,column=2)

year = tk.Entry(root)
month = tk.Entry(root)
day = tk.Entry(root)

year.grid(row=1,column=0)
month.grid(row=1,column=1)
day.grid(row=1,column=2)

tk.Button(root,text="Calculate Age",command=calculate_age).grid(row=2,column=1)

result = tk.Label(root,text="")
result.grid(row=3,column=1)

root.mainloop()