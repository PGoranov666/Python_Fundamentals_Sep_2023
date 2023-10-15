sequence = input()
numbers = sequence.split()
absolute_values = [abs(float(num)) for num in numbers]

print(absolute_values)
