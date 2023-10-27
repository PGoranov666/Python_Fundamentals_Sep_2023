def min_max_sum(some_numbers: str) -> int:
    numbers_str = input_numbers.split()
    numbers = [int(num) for num in numbers_str]

    minimum_number = min(numbers)
    maximum_number = max(numbers)
    sum_of_numbers = sum(numbers)

    print(f"The minimum number is {minimum_number}")
    print(f"The maximum number is {maximum_number}")
    print(f"The sum number is: {sum_of_numbers}")


input_numbers = input()
min_max_sum(input_numbers)
