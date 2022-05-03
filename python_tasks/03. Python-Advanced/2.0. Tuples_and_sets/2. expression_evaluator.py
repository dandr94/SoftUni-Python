from math import floor

expression = input().split()

numbers = []
operators = []


final_sum = 0

for i in expression:
    if i.isdigit():
        numbers.append(int(i))
    elif len(i) > 1:
        if i[0] == '-':
            numbers.append(-int(i[1:]))
    else:
        if len(numbers) > 2:
            remaining = numbers.pop(0)
            if i == '*':
                numbers = [remaining * numbers[0] * numbers[1]]
            elif i == '/':
                numbers = [floor(remaining / numbers[0] / numbers[1])]
            elif i == '+':
                numbers = [remaining + numbers[0] + numbers[1]]
            elif i == '-':
                numbers = [remaining - numbers[0] - numbers[1]]
        else:
            if i == '*':
                numbers = [numbers[0] * numbers[1]]
            elif i == '/':
                numbers = [floor(numbers[0] / numbers[1])]
            elif i == '+':
                numbers = [numbers[0] + numbers[1]]
            elif i == '-':
                numbers = [numbers[0] - numbers[1]]

print(''.join(map(str, numbers)))