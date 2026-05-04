"""
Enter number of rows: 6
A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F 
"""
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()