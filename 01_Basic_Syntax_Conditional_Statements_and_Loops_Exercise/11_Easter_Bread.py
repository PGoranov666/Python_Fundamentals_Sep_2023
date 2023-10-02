budget = float(input())
price_per_kg_flour = float(input())

price_per_pack_eggs = 0.75 * price_per_kg_flour
price_per_liter_milk = 1.25 * price_per_kg_flour

loaves_made = 0
colored_eggs = 0

while budget >= price_per_kg_flour + price_per_pack_eggs + (0.25 * price_per_liter_milk):

    budget -= price_per_kg_flour + price_per_pack_eggs + (0.25 * price_per_liter_milk)
    loaves_made += 1
    colored_eggs += 3

    if loaves_made % 3 == 0:
        lost_eggs = loaves_made - 2
        colored_eggs -= lost_eggs

print(f"You made {loaves_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget :.2f}BGN left.")
