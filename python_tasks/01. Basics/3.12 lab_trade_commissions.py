city = input()
quantity_of_sells = float(input())


commission = 0

if city == 'Sofia':
    if quantity_of_sells <= 500  and quantity_of_sells >= 0:
        commission = quantity_of_sells * 0.05
    elif quantity_of_sells > 500 and quantity_of_sells <= 1000:
        commission = quantity_of_sells * 0.07
    elif quantity_of_sells > 1000 and quantity_of_sells <= 10_000:
        commission = quantity_of_sells * 0.08
    elif quantity_of_sells > 10_000:
        commission = quantity_of_sells * 0.12
    else:
        print('error')
        quit()

elif city == 'Varna':
    if quantity_of_sells <= 500  and quantity_of_sells >= 0:
        commission = quantity_of_sells * 0.045
    elif quantity_of_sells > 500 and quantity_of_sells <= 1000:
        commission = quantity_of_sells * 0.075
    elif quantity_of_sells > 1000 and quantity_of_sells <= 10_000:
        commission = quantity_of_sells * 0.10
    elif quantity_of_sells > 10_000:
        commission = quantity_of_sells * 0.13
    else:
        print('error')
        quit()

elif city == 'Plovdiv':
    if quantity_of_sells <= 500  and quantity_of_sells >= 0:
        commission = quantity_of_sells * 0.055
    elif quantity_of_sells > 500 and quantity_of_sells <= 1000:
        commission = quantity_of_sells * 0.08
    elif quantity_of_sells > 1000 and quantity_of_sells <= 10_000:
        commission = quantity_of_sells * 0.12
    elif quantity_of_sells > 10_000:
        commission = quantity_of_sells * 0.145
    else:
        print('error')
        quit()

else:
    print('error')
    quit()

print(f'{commission:.2f}')