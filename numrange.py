for num in range (1000, 10000):
    n = str(num)
    a,b,c,d = int(n[0]), int(n[1]), int(n[2]), int(n[3])

    if (a + b) == (c + d) and num % 11 == 0:
        print(num)