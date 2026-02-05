'''Python program to reverse a number and find sum of digits'''

num = int(input("Enter a number: "))
s = 0
sum = 0
temp = num

while temp > 0:
    r = temp % 10
    s = s * 10 + r
    sum += r
    temp //= 10

print("Reversed number:", s)
print("Sum of digits:", sum)
