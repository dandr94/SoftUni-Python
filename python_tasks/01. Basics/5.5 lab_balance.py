
money = input()
sum = 0

while money != 'NoMoreMoney':
    money = float(money)
    if money < 0:
        print(f'Invalid operation!')
        break
    sum += money
    print(f'Increase: {money:.2f}')
    money = input()



print(f'Total: {sum:.2f}')
