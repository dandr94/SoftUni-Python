n = int(input())

students_and_grades = {}

for i in range(1, n +1):
    student = input()
    grade = float(input())

    if student not in students_and_grades:
        students_and_grades[student] = []

    students_and_grades[student].append(grade)

x = {x[0]: x[1] for x in students_and_grades.items() if sum(x[1]) / len(x[1]) >= 4.50}
for key, value in x.items():
    x[key] = sum(value) / len(value)

for name, grade in sorted(x.items(), key=lambda x: x[1], reverse=True):
    print(f'{name} -> {grade:.2f}')