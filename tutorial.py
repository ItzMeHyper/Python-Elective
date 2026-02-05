'''Define a function named even. This function expects a number as an argument and returns True if the number is divisible by 2,
   or it returns False otherwise.(Hint: A number is evenly divisible by 2 if the remainder is .'''

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Enter a number: "))
if(even(num)):
    print("Even")
else:
    print("Not Even")