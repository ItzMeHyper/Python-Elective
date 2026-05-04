#Write a python program to create a list of squares for the numbers from O to 9

sq = []

for i in range(1, 9+1):
    squr = i ** 2

    sq.append(squr)

print(sq)