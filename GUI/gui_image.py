#Display an image in Python GUI

from tkinter import *
from PIL import Image, ImageTk

root = Tk()

img = Image.open("iron_man.jpg")
photo = ImageTk.PhotoImage(img)

label = Label(root, image=photo)
label.pack()

root.mainloop()