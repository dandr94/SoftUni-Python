days = int(input())
type_room = input()
grade = input()


nights = days - 1

sum = 0

if type_room == 'room for one person':
    sum = nights * 18.00

elif type_room == 'apartment':
    sum = nights * 25.00

    if days < 10:
        discount = sum * 0.30
        sum = sum - discount

    elif days >= 10 and days <= 15:
        discount = sum * 0.35
        sum = sum - discount

    else:
        discount = sum * 0.50
        sum = sum - discount
elif type_room == 'president apartment':
    sum = nights * 35.00
    if days < 10:
        discount = sum * 0.10
        sum = sum - discount
    elif days >= 10 and days <= 15:
        discount = sum * 0.15
        sum = sum - discount
    else:
        discount = sum * 0.20
        sum = sum - discount

if grade == 'positive':
    discount = sum * 0.25
    sum = sum + discount
else:
    discount = sum * 0.10
    sum = sum - discount

print(f'{sum:.2f}')

