n = int(input())
salary = int(input())


for i in range(1, n + 1):
    site = input()
    if site == 'Facebook':
        salary -= 150
    elif site == 'Instagram':
        salary -= 100
    elif site == 'Reddit':
        salary -= 50
    if salary == 0:
        print('You have lost your salary.')
        break

if salary:
    print(salary)