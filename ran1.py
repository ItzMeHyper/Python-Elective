for i in range(100, 1000):
    a = i//100
    b = (i//10)%10
    c = i % 10
    
    if (a + b + c) % 2 == 0 and i % 9 == 0:
        print(i)