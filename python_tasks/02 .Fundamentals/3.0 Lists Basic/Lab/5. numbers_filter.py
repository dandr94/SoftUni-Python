n = int(input())

numbers = []
filtered_numbers = []

for i in range(n):
    integers = int(input())
    numbers.append(integers)


command = input()

if command == 'even':
    for number in numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)

elif command == 'odd':
    for number in numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)
elif command == 'positive':
    for number in numbers:
        if number > - 1:
            filtered_numbers.append(number)
elif command == 'negative':
    for number in numbers:
        if number < 0:
            filtered_numbers.append(number)

print(filtered_numbers)