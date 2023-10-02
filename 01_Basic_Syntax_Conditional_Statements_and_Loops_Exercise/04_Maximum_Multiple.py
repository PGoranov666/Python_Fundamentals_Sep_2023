# divisor = int(input())
# boundary = int(input())
#
# N = (boundary // divisor) * divisor
#
# print(N)

divisor = int(input())
boundary = int(input())

for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        break
print(number)
