money = float(input())
year = int(input())

age = 18
sum = 0

for i in range(1800, year + 1):
    if i % 2 == 0:
        sum += 12_000
    else:
        sum += 12_000 + 50 * age
    age += 1

if money >= sum:
    diff = money - sum
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    diff = sum - money
    print(f'He will need {diff:.2f} dollars to survive.')