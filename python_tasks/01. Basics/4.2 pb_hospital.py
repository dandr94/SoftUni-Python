period = int(input())

doctors = 7
left_overs = 0
treated = 0
day = 1

for i in range(1, period + 1):
    patients = int(input())
    if patients > doctors:
        left_overs += patients - doctors
        treated += doctors
    else:
        treated += patients
    day += 1
    if day == 3:
        if left_overs > doctors:
            doctors += 1
        day = 0

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {left_overs}.')