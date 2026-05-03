#Write a Python program to count number of even numbers and odd numbers in a given set of n numbers.

n = int(input("Enter the number of elements: "))

even_count = 0
odd_count = 0

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)