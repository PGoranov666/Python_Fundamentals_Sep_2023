number_of_lines = int(input())
water_count = 0
tank_capacity = 255

for line in range(number_of_lines):
    liters = int(input())
    if tank_capacity - liters < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters
    water_count += liters
print(water_count)
