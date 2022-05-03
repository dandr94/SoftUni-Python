exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

# началния час на изпита в минути
time_of_exam = (exam_hour * 60) + exam_minutes
# началния час на пристигане в минути
time_of_arrival = (arrival_hour * 60) + arrival_minutes
# разликата
minute_difference_total = time_of_arrival - time_of_exam

student_arrival = 'Late'
if minute_difference_total < -30:
    student_arrival = 'Early'
elif minute_difference_total <= 0:
    student_arrival = 'On time'


result = ''
if minute_difference_total != 0:
    hours_difference = abs(minute_difference_total) // 60
    minute_difference = abs(minute_difference_total) % 60

    if hours_difference > 0:
        result = f'{hours_difference}:{minute_difference:02} hours'
    else:
        result = f'{minute_difference} minutes'

    if minute_difference_total < 0:
        result += ' before the start'
    else:
        result += ' after the start'

print(student_arrival)
if result:
    print(result)