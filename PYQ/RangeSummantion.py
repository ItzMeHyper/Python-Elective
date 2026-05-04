def summation(lower,upper):
    sum = 0
    while (lower<=upper):
        sum = sum + lower
        lower += 1
    return sum
    #print("Sum = ", sum)

print(summation(1,4))