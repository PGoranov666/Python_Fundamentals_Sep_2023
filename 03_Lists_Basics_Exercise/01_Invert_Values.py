numbers_list = input().split()
opposite_numbers = []

for i in numbers_list:
    current_number = -int(i)
    opposite_numbers.append(current_number)
print(opposite_numbers)
