def min_max(numbers):
    result = []
    numbers.sort()
    result.append(numbers[0])
    result.append(numbers[-1])
    return result

numbers = [1,2,3,4,5,6,7,8,9,10]
result = min_max(numbers)
print(f"Smallest number is: {result[0]}")
print(f"Largest number is: {result[-1]}")