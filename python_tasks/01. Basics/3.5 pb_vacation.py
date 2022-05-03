budget = float(input())
season = input()

location = ''
type = ''
sum = 0

if budget <= 1000:
    type = 'Camp'
    if season == "Summer":
        location = 'Alaska'
        sum += budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        sum += budget * 0.45

elif budget > 1000 and budget <= 3000:
    type = 'Hut'
    if season == "Summer":
        location = 'Alaska'
        sum += budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        sum += budget * 0.60

else:
    type = 'Hotel'
    if season == "Summer":
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'
    sum += budget * 0.90

print(f'{location} - {type} - {sum:.2f}')