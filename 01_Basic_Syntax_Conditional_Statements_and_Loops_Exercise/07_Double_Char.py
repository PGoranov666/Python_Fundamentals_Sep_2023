command = input()

while command != "End":
    if command != "SoftUni":
        output = ""
        for i in command:
            output += i * 2
        print(output)

    command = input()
