party_size = int(input())
days_of_the_adventure = int(input())

earned_coins = 0

for i in range(1, days_of_the_adventure + 1):

    if i % 10 == 0:
        party_size -= 2

    if i % 15 == 0:
        party_size += 5

    earned_coins += 50 - party_size * 2

    if i % 3 == 0:
        earned_coins -= party_size * 3

    if i % 5 == 0:
        earned_coins += party_size * 20
        if i % 3 == 0:
            earned_coins -= party_size * 2


each_earned = int(earned_coins / party_size)
print(f"{party_size} companions received {each_earned} coins each.")