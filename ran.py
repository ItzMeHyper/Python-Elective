for i in range(1000, 10000):
    a = i//1000
    b = (i//100)%10
    c = (i//10)%10
    d = i % 10
    
    if (a + b) == (c + d) and i % 11 == 0:
        print(i)