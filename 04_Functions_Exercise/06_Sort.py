sequence = input()
numbers_as_str = sequence.split()

numbers = [int(num) for num in numbers_as_str]
sorted_numbers = sorted(numbers)

print(sorted_numbers)
