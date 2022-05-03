n = int(input())

record = set()

for i in range(n):
    way, plate = input().split(', ')

    if way == 'IN':
        record.add(plate)
    elif way == 'OUT':
        record.remove(plate)

if record:
    for plates in record:
        print(plates)
else:
    print('Parking Lot is Empty')