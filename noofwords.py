s = input("Enter a string: ")
w = input("Enter a word to search: ")

words = s.split()

print("Number of words in the string:", len(words))

count = 0
for ch in s:
    if ch == w:
        count += 1

print(f"The word '{w}' occurs {count} times in the string.")