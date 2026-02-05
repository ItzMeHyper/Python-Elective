lst = [1,-2,3,-4]
pos = []
neg = []

for i in lst:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
print("Positive numbers:", pos)
print("Negative numbers:", neg)