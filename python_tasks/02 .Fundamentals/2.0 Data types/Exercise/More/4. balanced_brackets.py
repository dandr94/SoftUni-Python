n = int(input())


first_bracket = 0
second_bracket = 0

is_balanced = True

for i in range(1, n + 1):
    character = input()

    if character == '(':
        first_bracket += 1
        if (first_bracket - 1) != second_bracket:
            is_balanced = False
            break
    elif character == ')':
        second_bracket += 1
        if i % 2 == 0:
            if first_bracket != second_bracket:
                is_balanced = False
                break

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
