s = input("Enter a string: ")
w = input ("Enter a word to search: ")
words = s.split()
print("Number of words in the string:", len(words))
for word in words:
    if word in w:
        count = words.count(word)
        print(f"The word '{w}' occurs {count} times in the string.")
        break