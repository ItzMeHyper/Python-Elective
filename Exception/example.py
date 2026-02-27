def add():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(a + b)
    except ValueError:
        print("Invalid input")
    finally:
        print("Addition completed")

add()   