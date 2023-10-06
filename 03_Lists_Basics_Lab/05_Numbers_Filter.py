# n = int(input())
# numbers_list = []
#
# for _ in range(n):
#     number = int(input())
#     numbers_list.append(number)
#
# command = input()
# filtered_list = []
#
# if command == 'even':
#     for num in numbers_list:
#         if num % 2 == 0:
#             filtered_list.append(num)
#
# if command == 'odd':
#     for num in numbers_list:
#         if num % 2 != 0:
#             filtered_list.append(num)
#
# if command == 'positive':
#     for num in numbers_list:
#         if num >= 0:
#             filtered_list.append(num)
#
# if command == 'negative':
#     for num in numbers_list:
#         if num < 0:
#             filtered_list.append(num)
#
# print(filtered_list)

# ADVANCED LEVEL DECISION

n = int(input())

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"

numbers_list = [int(input()) for i in range(n)]

filtered_list = []

command = input()
for num in numbers_list:
    filtered_command = ((command == COMMAND_EVEN and num % 2 == 0) or
                        (command == COMMAND_ODD and num % 2 != 0) or
                        (command == COMMAND_POSITIVE and num >= 0) or
                        (command == COMMAND_NEGATIVE and num < 0))

    if filtered_command:
        filtered_list.append(num)

print(filtered_list)
