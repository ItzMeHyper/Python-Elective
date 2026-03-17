#GUI program for Rupees <-> Euro conversion

import tkinter as tk

rate = 0.011

def r_to_e():
    r = float(rupee.get())
    euro.delete(0,tk.END)
    euro.insert(0,str(r*rate))

def e_to_r():
    e = float(euro.get())
    rupee.delete(0,tk.END)
    rupee.insert(0,str(e/rate))

root = tk.Tk()

tk.Label(root,text="Rupees").grid(row=0,column=0)
tk.Label(root,text="Euro").grid(row=0,column=1)

rupee = tk.Entry(root)
euro = tk.Entry(root)

rupee.grid(row=1,column=0)
euro.grid(row=1,column=1)

rupee.insert(0,"0.0")
euro.insert(0,"0.0")

tk.Button(root,text="R->E",command=r_to_e).grid(row=2,column=0)
tk.Button(root,text="E->R",command=e_to_r).grid(row=2,column=1)

root.mainloop()