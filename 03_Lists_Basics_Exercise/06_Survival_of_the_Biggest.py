list_as_string = input().split()
numbers_to_remove = int(input())

list_as_integer = []

for element in list_as_string:
    list_as_integer.append(int(element))

for _ in range(numbers_to_remove):
    smallest_number = min(list_as_integer)
    list_as_integer.remove(smallest_number)

list_as_string = []
for x in list_as_integer:
    list_as_string.append(str(x))

print(", ".join(list_as_string))


# list_as_string = input().split()
# numbers_to_remove = int(input())
#
# list_as_integer = []
#
# for element in list_as_string:
#     list_as_integer.append(int(element))
#
# for _ in range(numbers_to_remove):
#     smallest_number = min(list_as_integer)
#     list_as_integer.remove(smallest_number)
#
# list_as_string = [str(x) for x in list_as_integer]
#
# print(", ".join(list_as_string))
