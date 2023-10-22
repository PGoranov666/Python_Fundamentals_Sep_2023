# def return_the_smallest(num1, num2, num3):
#     if num1 < num2 and num1 < num3:
#         return num1
#     elif num2 < num1 and num2 < num3:
#         return num2
#     elif num3 < num1 and num3 < num2:
#         return num3
#
#
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
#
# print(return_the_smallest(num1, num2, num3))

def return_the_smallest(some_numbers: list) -> int:
    return min(some_numbers)

number1 = int(input())
number2 = int(input())
number3 = int(input())

smallest_element = return_the_smallest([number1, number2, number3])
print(smallest_element)
