season = input()
group_type = input()
students = int(input())
nights = int(input())

sum = 0
type = ''
if season == 'Winter':
    if group_type == 'boys' :
        sum += nights * 9.60 * students
        type = 'Judo'
    elif group_type == 'girls':
        sum += nights * 9.60 * students
        type = 'Gymnastics'
    else:
        sum += nights * 10 * students
        type = 'Ski'

elif season == 'Spring':
    if group_type == 'boys':
        sum += nights * 7.20 * students
        type = 'Tennis'
    elif group_type == 'girls':
        sum += nights * 7.20 * students
        type = 'Athletics'
    else:
        sum += nights * 9.50 * students
        type = 'Cycling'

elif season == 'Summer':
    if group_type == 'boys':
        sum += nights * 15 * students
        type = 'Football'
    elif group_type == 'girls':
        sum += nights * 15 * students
        type = 'Volleyball'
    else:
        sum += nights * 20 * students
        type = 'Swimming'

if students >= 50:
    sum -= sum * 0.50
elif students >= 20 and students < 50:
    sum -= sum * 0.15
elif students >= 10 and students < 20:
    sum -= sum * 0.05

print(f'{type} {sum:.2f} lv.')