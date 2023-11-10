products = {}

while True:
    input_data = input()
    if input_data == "buy":
        break

    name, price, quantity = input_data.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        products[name]["quantity"] += quantity
        if products[name]["price"] != price:
            products[name]["price"] = price
    else:
        products[name] = {"price": price, "quantity": quantity}

for product, data in products.items():
    total_price = data["price"] * data["quantity"]
    print(f"{product} -> {total_price:.2f}")
