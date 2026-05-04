#Write a python program to reverse a number and also find the sum of the digits of that number.

num = int(input("Enter a number: "))

org = num
rev= 0
sum = 0

while (num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
    sum = sum + rem

print("Reversed number:", rev)
print("Sum of digits:", sum)