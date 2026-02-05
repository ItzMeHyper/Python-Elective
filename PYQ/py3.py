'''Write a Python program to display the sum of odd numbers between a programmer specified upper and lower limit.'''

# Read limits
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

sum_odd = 0

# Loop through the range
for i in range(lower, upper + 1):
    if i % 2 != 0:
        sum_odd += i

# Display result
print("Sum of odd numbers between", lower, "and", upper, "is:", sum_odd)
