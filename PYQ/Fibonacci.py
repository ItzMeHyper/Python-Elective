num = int(input("Enter a number: "))

x = 0
y = 1

for i in range(num):
    print(x, end=" ")
    z = x + y
    x = y
    y = z