try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print("Result:", a/b)

except ZeroDivisionError:
    print("Division by zero not allowed")

except ValueError:
    print("Invalid input")

finally:
    print("Program finished")