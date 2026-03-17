import tkinter as tk

def show_coords(event):
    canvas.create_text(event.x,event.y,
                       text=f"({event.x},{event.y})")

root = tk.Tk()

canvas = tk.Canvas(root,width=400,height=400,bg="white")
canvas.pack()

canvas.bind("<Button-1>",show_coords)

root.mainloop()