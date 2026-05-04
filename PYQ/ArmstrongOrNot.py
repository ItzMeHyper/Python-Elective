num = int (input("Enter a number: "))

sum = 0
c = num

while (num > 0):
    rem = num % 10
    sum = sum + (rem * rem * rem)
    num = num // 10

if (c == sum):
    print(f"{c} is an Armstrong number")
else:
    print(f"{c} is not an Armstrong number")