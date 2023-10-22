def sum_numbers(first, second):
    return first + second


def subtract(result, third):
    return result - third


def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result

number1 = int(input())
number2 = int(input())
number3 = int(input())

print(add_and_subtract(number1, number2, number3))
