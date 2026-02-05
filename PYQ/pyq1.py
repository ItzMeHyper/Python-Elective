'''Write a Python program to check whether a given number is an Armstrong number or not.'''

n = int(input("Enter a number: "))

c = n
s = 0

while n > 0:
    r = n % 10
    s = (r * r * r) + s
    n = n // 10

if s == c:
    print(f"{s} is an Armstrong number")
else:
    print(f"{s} is not an Armstrong number")
