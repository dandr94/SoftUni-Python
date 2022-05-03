petrol = input()
litres = int(input())

if petrol == 'Diesel':
    if litres >= 25:
        print(f'You have enough {str.lower(petrol)}.')
    else:
        print(f'Fill your tank with {str.lower(petrol)}!')

elif petrol == 'Gasoline':
    if litres >= 25:
        print(f'You have enough {str.lower(petrol)}.')
    else:
        print(f'Fill your tank with {str.lower(petrol)}!')

elif petrol == 'Gas':
    if litres >= 25:
        print(f'You have enough {str.lower(petrol)}.')
    else:
        print(f'Fill your tank with {str.lower(petrol)}!')

else:
    print('Invalid fuel!')