n = int(input())

record = {}

for i in range(n):
    txt = tuple(input().split())
    name = txt[0]
    grade = txt[1]

    if name not in record:
        record[name] = []

    record[name].append(float(grade))

for key, value in record.items():
    avg = f'{sum(value) / len(value):.2f}'
    print(f'{key} ->', end=' ')
    for num in value:
        print(f'{num:.2f}', end=' ')
    else:
        print(f'(avg: {avg})')



    # print(f'{key} -> {" ".join([str(x) for x in value])} (avg: {avg})')
