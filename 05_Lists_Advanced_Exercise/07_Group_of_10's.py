numbers = [int(num) for num in input().split(',')]
current_group = 10
while numbers:
    filtered_numbers_current_group = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_current_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in filtered_numbers_current_group]
