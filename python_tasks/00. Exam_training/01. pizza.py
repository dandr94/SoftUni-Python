from collections import deque

orders = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]

pizzas_made = 0

completed = False

while employees and orders:
    current_order = orders.popleft()
    if current_order <= 0:
        continue
    elif current_order > 10:
        continue

    current_employee = employees.pop()

    if current_order <= current_employee:
        pizzas_made += current_order

    elif current_order > current_employee:
        left_over = current_order - current_employee
        pizzas_made += current_employee
        orders.appendleft(left_over)

if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    print(f'Employees: {", ".join([str(x) for x in employees])}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in orders])}')
