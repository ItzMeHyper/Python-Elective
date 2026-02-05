'''write a python program to read n integers into a list and seperate the positive and negative numbers into two different lists'''
n = int(input("Enter the number of integers: "))
numbers = []
for i in range(n):
    num = int(input("Enter integer {}: ".format(i+1)))
    numbers.append(num)