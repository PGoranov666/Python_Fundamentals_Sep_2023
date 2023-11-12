import re

def process_string(s):
    total_sum = 0
    parts = s.split()

    for part in parts:
        match = re.match(r"([a-zA-Z]+)(\d+)", part)
        letter, number_str = match.groups()
        number = int(number_str)

        if letter.isupper():
            total_sum += number / (ord(letter) - ord('A') + 1)
        else:
            total_sum += number * (ord(letter) - ord('a') + 1)

        if part[-1].isupper():
            total_sum -= ord(part[-1]) - ord('A') + 1
        else:
            total_sum += ord(part[-1]) - ord('a') + 1

    return total_sum

input_string = input()
result = process_string(input_string)
print(f"{result:.2f}")
