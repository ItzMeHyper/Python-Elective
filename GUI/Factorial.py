import tkinter as tk

def factorial():
    n = int(num.get())
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    result.config(text="Factorial = " + str(fact))

root = tk.Tk()
root.title("Factorial Calculator")

tk.Label(root, text="Enter the number: ").grid(row=0, column=1)

num = tk.Entry(root)
num.grid(row=0, column=2)

tk.Button(root, text="Calculate", command=factorial).grid(row=3, column=2)

result = tk.Label(root, text="")
result.grid(row=4, column=2)

root.mainloop()