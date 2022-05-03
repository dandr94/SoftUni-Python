budget = float(input())
price_for_one_kg_flour = float(input())

sum = 0

price_for_one_pack_eggs = price_for_one_kg_flour * 0.75
price_for_one_l_milk = price_for_one_kg_flour + (price_for_one_kg_flour * 0.25)
price_per_cozonacs = (price_for_one_l_milk / 4) + price_for_one_kg_flour + price_for_one_pack_eggs

count = 0
colored_eggs = 0
cozonacs_baked = 0

# while budget - price_per_cozonacs > 0: (better way)


while budget > 0:
    budget -= price_per_cozonacs
    if budget < 0:
        break
    cozonacs_baked += 1
    colored_eggs += 3
    count += 1
    if count == 3:
        colored_eggs -= cozonacs_baked - 2
        count = 0

print(f"You made {cozonacs_baked} cozonacs! Now you have {colored_eggs} eggs and {abs(budget + price_per_cozonacs):.2f}BGN left.")
