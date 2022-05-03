from collections import deque

txt = deque(input().split())

main_colors = {'red', 'blue', 'yellow'}
secondary_colors = {'orange', 'purple', 'green'}

my_colors = []

while txt:
    left_part = txt.popleft()
    right_part = txt.pop() if txt else ''

    color = left_part + right_part

    if color in main_colors or color in secondary_colors:
        my_colors.append(color)
        continue

    color = right_part + left_part

    if color in main_colors or color in secondary_colors:
        my_colors.append(color)
    else:
        middle = len(txt) // 2

        left_final = left_part[:-1]
        right_final = right_part[:-1]

        if left_final:
            txt.insert(middle, left_final)
        if right_final:
            txt.insert(middle, right_final)

if 'orange' in my_colors and 'red' not in my_colors or \
        'orange' in my_colors and 'yellow' not in my_colors:
    my_colors.remove('orange')
if 'purple' in my_colors and 'red' not in my_colors or \
        'purple' in my_colors and 'blue' not in my_colors:
    my_colors.remove('purple')
if 'green' in my_colors and 'yellow' not in my_colors or \
        'green' in my_colors and 'blue' not in my_colors:
    my_colors.remove('green')

print(my_colors)