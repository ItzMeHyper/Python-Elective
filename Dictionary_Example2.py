'''Create a python program that uses a ditionary to store the names and ages of people. Ask the user to enter a name , and the  program should 
display the age of that person'''

people = {'Ram': 25,
          'Alice': 30,
          'Bob': 22,
          'Diana': 28
         }

name = input("Enter a name: ")

if name in people:
    print(f"{name} is {people[name]} years old.")
else:
    print(f"Sorry, {name} is not in the dictionary.")