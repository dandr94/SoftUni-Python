from collections import deque
import sys


quantity_of_food = int(input())

que_of_orders = deque(input().split())

max_order = -sys.maxsize

for i in que_of_orders:
    if int(i) > max_order:
        max_order = int(i)

print(max_order)

count = 0

for b in que_of_orders:
    if int(b) <= quantity_of_food:
        quantity_of_food -= int(b)
        count += 1
    else:
        break

while count:
    que_of_orders.popleft()
    count -= 1

if que_of_orders:
    print(f'Orders left: {" ".join(que_of_orders)}')
else:
    print('Orders complete')
