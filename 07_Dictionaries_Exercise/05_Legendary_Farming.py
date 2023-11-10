items = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split()
obtained = False

while not obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            legendary_item = "Shadowmourne"
            # print(f"Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            legendary_item = "Valanyr"
            # print(f"Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            legendary_item = "Dragonwrath"
            # print(f"Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break

    current_items = input().split()
print(f"{legendary_item} obtained!")
for material, quantity in items.items():
    print(f"{material}: {quantity}")
