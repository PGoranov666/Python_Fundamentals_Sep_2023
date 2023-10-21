def calculate_total_price(product, quantity):
    return {
        "coffee": quantity * 1.50,
        "coke" : quantity * 1.40,
        "water" : quantity * 1.00,
        "snacks": quantity * 2.00
    }.get(product, quantity)


product = input()
quantity = int(input())
result = calculate_total_price(product, quantity)
print(f"{result:.2f}")
