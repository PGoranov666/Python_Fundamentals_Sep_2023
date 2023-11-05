products_info = input().split()
stock_data = {}

for i in range(0, len(products_info), 2):
    food = products_info[i]
    quantity = products_info[i + 1]
    stock_data[food] = int(quantity)

search_products = input().split()
for current_product in search_products:
    if current_product in stock_data.keys():
        print(f"We have {stock_data[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")

