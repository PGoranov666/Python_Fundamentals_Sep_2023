fires_info = input().split("#")
water = int(input())
total_fire = 0

# inputs = ["High = 150", "Low = 55", "Medium = 86", "Low = 40", "High = 110", "Medium = 77"]
fire_range = False
fire_cells_list = []
# Итерация през всеки вход
for input_str in fires_info:
    # Разделете входа на име и стойност
    fire_type, value_str = input_str.split(" = ")
    fire_value = int(value_str)

    # Проверка на името на вида и проверка на стойността спрямо диапазона
    if fire_type == "High":
        current_value = fire_value
        if 81 <= current_value <= 125 and water >= current_value:
            fire_range = True
            water -= current_value
            total_fire += current_value
            fire_cells_list.append(fire_value)

    elif fire_type == "Medium":
        current_value = fire_value
        if 51 <= current_value <= 80 and water >= current_value:
            fire_range = True
            water -= current_value
            total_fire += current_value
            fire_cells_list.append(fire_value)

    elif fire_type == "Low":
        current_value = fire_value
        if 1 <= current_value <= 50 and water >= current_value:
            fire_range = True
            water -= current_value
            total_fire += current_value
            fire_cells_list.append(fire_value)

    else:
        fire_range = False


total_efforts = total_fire * 0.25

print("Cells:")
for cell in fire_cells_list:
    print(f" - {cell}")

print(f"Effort: {total_efforts:.2f}")
print(f"Total Fire: {total_fire}")
