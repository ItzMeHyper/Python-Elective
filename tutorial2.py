'''Create a function min_max() that takes n numbers as list argument and return the smallest and largest numbers.'''
def min_max(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

list = input("Enter numbers separated by spaces: ").split()

print("Smallest and largest numbers are:", min_max(list))
