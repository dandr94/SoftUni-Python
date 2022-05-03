lost_fight_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
cost = 0
count = 0

for i in range(1, lost_fight_count + 1):
    if i % 2 == 0:
        cost += helmet_price

    if i % 3 == 0:
        cost += sword_price

        if i % 2 == 0:
            cost += shield_price
            count += 1
            if count == 2:
                cost += armor_price
                count = 0

print(f"Gladiator expenses: {cost:.2f} aureus")

