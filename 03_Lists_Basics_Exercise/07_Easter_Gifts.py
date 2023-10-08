gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    command_args = command.split()
    action = command_args[0]

    if action == "OutOfStock":
        gift_to_remove = command_args[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_remove:
                gifts[i] = "None"
    elif action == "Required":
        gift_to_replace = command_args[1]
        index = int(command_args[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_to_replace
    elif action == "JustInCase":
        gifts[-1] = command_args[1]

filtered_gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(filtered_gifts))
