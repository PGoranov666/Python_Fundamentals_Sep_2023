import re

names = input()
valid_names = []

regex_pattern = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'
matches = re.findall(regex_pattern, names)

# print(' '.join(matches)) or:
for name in matches:
    print(name, end=' ')
