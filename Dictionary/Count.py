#Count characters using dictionary

string = input("Enter a string: ")
count_dict = {}

for ch in string:
    if ch in count_dict:
        count_dict[ch] += 1
    else:
        count_dict[ch] = 1

print("Character count:", count_dict)