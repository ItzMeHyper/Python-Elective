def divide(x, y):
    try:
        result = x // y
        print("The result is", result)
    except ZeroDivisionError:
        print("Sorry, you can't divide by zero.")

divide(3, 0)
divide(10, 2)