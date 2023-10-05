# fights_count = int(input())

lost_fights_count = float(input())
helmet_repair_price = float(input())
sword_repair_price = float(input())
shield_repair_price = float(input())
armor_repair_price = float(input())

total_helmet_repairs = lost_fights_count // 2
total_sword_repairs = lost_fights_count // 3
total_shield_repairs = lost_fights_count // (2 * 3)
total_armor_repairs = total_shield_repairs // 2

expenses = total_helmet_repairs * helmet_repair_price \
        + total_sword_repairs * sword_repair_price \
        + total_shield_repairs * shield_repair_price \
        +total_armor_repairs * armor_repair_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
