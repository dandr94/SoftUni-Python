n = int(input())

number = ''
count = 0

for i in range(1111, 9999 + 1):
    for position, num in enumerate(str(i)):
        if int(num) == 0:
            break
        if n % int(num) == 0:
            number += str(num)
            count += 1
            if count == 4:
                print(f'{number}', end=' ')
    number = ''
    count = 0


# second solution

number = int(input())
for current_number in range(1111, 9999 + 1):
    is_special = True
    current_number_as_str = str(current_number)
    for current_digit in current_number_as_str:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            is_special = False
            break
    if is_special:
        print(current_number, end=' ')
