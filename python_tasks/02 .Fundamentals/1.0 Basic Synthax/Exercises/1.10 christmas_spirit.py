quantity = int(input())
days_left = int(input())

budget = 0
christmas_spirit = 0

for i in range(1, days_left + 1):
    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        budget += 2 * quantity
        christmas_spirit += 5

    if i % 3 == 0:
        budget += 5 * quantity
        budget += 3 * quantity
        christmas_spirit += 13

    if i % 5 == 0:
        budget += 15 * quantity
        christmas_spirit += 17

        if i % 3 == 0:
            christmas_spirit += 30

    if i % 10 == 0:
        christmas_spirit -= 20
        budget += 5 + 3 + 15

    if i == days_left and days_left % 10 == 0:
        christmas_spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {christmas_spirit}')