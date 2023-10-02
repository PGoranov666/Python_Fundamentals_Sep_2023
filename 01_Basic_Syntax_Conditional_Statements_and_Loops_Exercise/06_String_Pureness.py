string_number = int(input())

for current_string in range(string_number):
    command = input()
    if "," in command or "." in command or "_" in command:
        print(f"{command} is not pure!")
    else:
        print(f"{command} is pure.")
