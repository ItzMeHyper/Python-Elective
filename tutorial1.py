'''Define a function named summation. This function expects a number as an  '''

def summation(low, high):
    sum=0
    for i in range(low,high+1):
        sum = sum+i
    return sum
print(summation(3,9))

