number = int(input())
magic_word = input()

my_list = []

for i in range(number):
    current_word = input()
    my_list.append(current_word)
print(my_list)

for i in range(len(my_list) -1, -1,-1):
    element = my_list[i]
    if magic_word not in element:
        my_list.remove(element)
print(my_list)

# number = int(input())
# magic_word = input()
#
# my_list = []
#
# for i in range(number):
#     current_string = input()
#     my_list.append(current_string)
# print(my_list)
#
# filtered_list = []
# for current_string in my_list:
#     if magic_word in current_string:
#         filtered_list.append(current_string)
# print(filtered_list)
