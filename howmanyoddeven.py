'''accept a positive integer count how many odd and even numbers are present in that number'''

num = int(input("Enter a positive number: "))
odd_count = 0
evn_count = 0
if(num < 0):
    print("Please enter a positive number")
    exit()
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        evn_count += 1
    else:
        odd_count += 1
    num = num // 10

if(odd_count > evn_count):
    print("Odd numbers are more than even numbers")
elif(evn_count > odd_count):
    print("Even numbers are more than odd numbers")
else:
    print("Odd and even numbers are equal")

print("Number of even digits:", evn_count)
print("Number of odd digits:", odd_count)