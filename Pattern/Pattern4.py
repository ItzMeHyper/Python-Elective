"""
0   1   2   3   4   
0   1   2   3   
0   1   2   
0   1   
0  
"""

for i in range(5, 0, -1):
    for j in range(i):
        print(j, end="   ")
    print()