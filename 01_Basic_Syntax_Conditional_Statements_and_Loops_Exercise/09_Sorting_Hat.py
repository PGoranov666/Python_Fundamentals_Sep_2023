command = input()
# is_true = True
while True:
    if command == "Voldemort":
        print("You must not speak of that name!")
        break
    if command == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    else:
        print(f"{command} goes to Hufflepuff.")

    command = input()
