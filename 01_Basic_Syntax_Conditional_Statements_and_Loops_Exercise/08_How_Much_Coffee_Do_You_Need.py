event = input()

total_coffees = 0
while event != "END":

    if event.lower() == "coding" or event.lower() == "cat" or event.lower() == "dog" or event.lower() == "movie":
        if event.islower():
            total_coffees += 1
        else:
            total_coffees += 2
    event = input()
if total_coffees > 5:
    print(f"You need extra sleep")
else:
    print(total_coffees)
