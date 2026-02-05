'''Program to implement addition of two numbers using recursion'''
def add(a,b):
    if b == 0:
        return a
    else:
        return add(a + 1, b - 1)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(f"The sum of {n1} and {n2} is {add(n1,n2)}")