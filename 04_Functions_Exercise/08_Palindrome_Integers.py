def is_palindrome(some_number: str) -> bool:
    return  some_number == some_number[::-1]


numbers = input().split(', ')

for numbers in numbers:
    print(is_palindrome(numbers))
