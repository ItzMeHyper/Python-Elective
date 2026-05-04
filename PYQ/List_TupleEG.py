from functools import reduce

words = ["250","-31","25","1"]

print(words)
words = list(map(int, words))
print(words)


nums = [1, 2, 3, 4]
print(nums)
squares = list(map(lambda x: x**2, nums))
print(squares)

squares1 = list(filter(lambda x: x%2==0, nums))
print(squares1)

def add(x,y):
    return x+y

sum = reduce(add, nums)
print(sum)


lst = [1,2,3,4,5,6,7,8,9]
for i in lst:
    print(i, end=" ")
print()

lst[4] = 4
print(lst)

lst.append(10)
print(lst)

#List Comprehension
common = [x for x in lst if x in nums]
print(common)
###############################################

both = words + lst
print(both)
both.sort()
print(both)


L = [10,20,30,40]
print("List = ", L)

T = (50,60,70,80)
print("Tuple = ", T)

T1 = tuple(L)
print(T1)

L1= list(T)
print(L1)

n = int(input("Enter the number of elements: "))

l = []
t = ()

for i in range(n):
    x = int(input("Enter the elements: "))
    l.append(x)
    t = t + (x,)

print("List:", l)
print("Tuple:", t)