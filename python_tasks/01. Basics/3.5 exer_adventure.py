budget = float(input())
season = input()

sum = 0
type = ''
if budget <= 100:
    if season == 'summer':
        type = 'Camp'
        sum += budget * 0.30
        print('Somewhere in Bulgaria')
        print(f'{type} - {sum:.2f}')
    else:
        type = 'Hotel'
        sum += budget * 0.70
        print('Somewhere in Bulgaria')
        print(f'{type} - {sum:.2f}')

elif budget > 100 and budget <= 1000:
    if season == 'summer':
        type = 'Camp'
        sum += budget * 0.40
        print('Somewhere in Balkans')
        print(f'{type} - {sum:.2f}')
    else:
        type = 'Hotel'
        sum += budget * 0.80
        print('Somewhere in Balkans')
        print(f'{type} - {sum:.2f}')

elif budget > 1000:
    type = 'Hotel'
    sum += budget * 0.90
    print('Somewhere in Europe')
    print(f'{type} - {sum:.2f}')