n = int(input())

record = []

for i in range(n):
    record.append(input())

unique = {n for n in record}

for b in unique:
    print(b)