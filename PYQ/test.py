n = int(input("Enter number of elements: "))
even = odd = 0

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)

x = 'abcd'
for i in range(len(x)):
    print(i)

print(len)