petrol = input()
quantity_petrol = float(input())
club_card = input()


gasoline_price = 0
diesel_price = 0
gas_price = 0

if petrol == 'Gasoline':
    gasoline_price = quantity_petrol * 2.22
    if club_card == 'Yes':
        gasoline_price = (quantity_petrol * 2.22) - (quantity_petrol * 0.18)
    if quantity_petrol >= 20 and quantity_petrol <= 25:
        discount = gasoline_price * 0.08
        gasoline_price = gasoline_price - discount
    elif quantity_petrol > 25:
        discount = gasoline_price * 0.10
        gasoline_price = gasoline_price - discount
    print(f'{gasoline_price:.2f} lv.')

elif petrol == 'Diesel':
    diesel_price = quantity_petrol * 2.33
    if club_card == 'Yes':
        diesel_price = quantity_petrol * 2.33 - (quantity_petrol * 0.12)
    if quantity_petrol >= 20 and quantity_petrol <= 25:
        discount = diesel_price * 0.08
        diesel_price = diesel_price - discount
    elif quantity_petrol > 25:
        discount = diesel_price * 0.10
        diesel_price = diesel_price - discount
    print(f'{diesel_price:.2f} lv.')

elif petrol == 'Gas':
    gas_price = quantity_petrol * 0.93
    if club_card == 'Yes':
        gas_price = quantity_petrol * 0.93 - (quantity_petrol * 0.08)
    if quantity_petrol >= 20 and quantity_petrol <= 25:
        discount = gas_price * 0.08
        gas_price = gas_price - discount
    elif quantity_petrol > 25:
        discount = gas_price * 0.10
        gas_price = gas_price - discount
    print(f'{gas_price:.2f} lv.')



