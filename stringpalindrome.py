str = input("Enter a string: ").lower()

if str == str[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")