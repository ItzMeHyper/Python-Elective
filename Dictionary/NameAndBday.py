#Dictionary of names and birthdays

birthdays = {
    "Alice": "12-01-2000",
    "Bob": "05-07-1998",
    "Charlie": "23-09-2001"
}

name = input("Enter a name: ")

if name in birthdays:
    print(name, "birthday is", birthdays[name])
else:
    print("Name not found")