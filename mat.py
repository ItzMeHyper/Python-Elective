a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

f1 = (a+b) * (a+b)
f2 = (a*a + 2*a*b + b*b)

if f1 == f2:
    print("LHS = RHS \nie,", f1 ," = ", f2)