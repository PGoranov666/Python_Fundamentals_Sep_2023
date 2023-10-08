collection_of_items = input().split('|')
budget = float(input())
ticket_price = 150
items_new_prices = []
profit = 0
current_budget = budget
sum_new_prices = 0
for input_items in collection_of_items:
    # Разделете входа на име и стойност
    item_type, item_price = input_items.split("->")
    item_price = float(item_price)

    current_price = item_price
    if item_type == "Clothes":
        if current_price <= 50.00 and current_budget >= current_price:
            current_budget -= current_price
            sell_price = (current_price * 0.40) + current_price
            sum_new_prices += sell_price
            profit += sell_price - current_price
            items_new_prices.append(sell_price)
    if item_type == "Shoes":
        if current_price <= 35.00 and current_budget >= current_price:
            current_budget -= current_price
            sell_price = (current_price * 0.40) + current_price
            sum_new_prices += sell_price
            profit += sell_price - current_price
            items_new_prices.append(sell_price)
    if item_type == "Accessories":
        if current_price <= 20.50 and current_budget >= current_price:
            current_budget -= current_price
            sell_price = (current_price * 0.40) + current_price
            sum_new_prices += sell_price
            profit += sell_price - current_price
            items_new_prices.append(sell_price)

formatted_prices = ""
for price in items_new_prices:
    formatted_prices += f"{price:.2f} "
formatted_prices = formatted_prices.strip()

print(formatted_prices)
print(f"Profit: {profit:.2f}")

if sum_new_prices + current_budget > ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
