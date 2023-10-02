total_price = 0

number_of_orders = int(input())

for orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if (0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000):

        order_price = capsules_per_day * price_per_capsule * days

        total_price += order_price

        print(f"The price for the coffee is: ${order_price :.2f}")

print(f"Total: ${total_price :.2f}")
