persons = int(input())
capacity = int(input())

courses = persons // capacity
if persons % capacity != 0:
    courses += 1

print(courses)
# from math import ceil
#
# persons = int(input())
# capacity = int(input())
# courses = ceil(persons / capacity)
#
# print(courses)
