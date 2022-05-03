money_needed_for_vacation = float(input())
current_money = float(input())

count_spend = 0
days_passed = 0

while current_money < money_needed_for_vacation and count_spend < 5:
    action = input()
    money = float(input())
    days_passed += 1
    if action == 'spend':
        count_spend += 1
        current_money -= money
        if current_money < 0:
            current_money = 0
    else:
        current_money += money
        count_spend = 0

if count_spend == 5:
    print(f"You can't save the money.")
    print(f'{days_passed}')

if current_money >= money_needed_for_vacation:
    print(f'You saved the money for {days_passed} days.')

