def armstrong_sum(n):
    if n == 0:
        return 0
    r = n % 10
    return (r * r * r) + armstrong_sum(n // 10)


n = int(input("Enter a number: "))
c = n

s = armstrong_sum(n)

if s == c:
    print(f"{s} is an Armstrong number")
else:
    print(f"{s} is not an Armstrong number")
