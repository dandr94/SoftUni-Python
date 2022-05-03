exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())


time_of_exam = exam_hour * 60 + exam_minutes
time_of_arrival = arrival_hour * 60 + arrival_minutes

if time_of_arrival > time_of_exam:
    print('Late')
elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print('On time')
else:
    print('Early')

diff = abs(time_of_exam - time_of_arrival)
hours = diff // 60
minutes = diff % 60

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f'{diff} minutes before the start')

elif time_of_arrival <= time_of_exam - 60:
    print(f'{hours}:{minutes:02} hours before the start')

elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f'{diff} minutes after the start')

elif time_of_arrival >= time_of_exam + 60:
    print(f'{hours}:{minutes:02} hours after the start')
