# def calculate_result(operator, num1, num2):
#     if operator == 'multiply':
#         return num1 * num2
#     elif operator == 'divide':
#         return int(num1 / num2)
#     elif operator == 'add':
#         return num1 + num2
#     elif operator == 'subtract':
#         return num1 - num2
#
# operator = input()
# num1 = int(input())
# num2 = int(input())
#
# result = calculate_result(operator, num1, num2)
# print(result)


def calculate_result(operator, num1, num2):
    return {
        "multiply": num1 * num2,
        "divide": int(num1 / num2),
        "add": num1 + num2,
        "subtract": num1 - num2,
    }.get(operator)

operator = input()
num1 = int(input())
num2 = int(input())

result = calculate_result(operator, num1, num2)
print(result)