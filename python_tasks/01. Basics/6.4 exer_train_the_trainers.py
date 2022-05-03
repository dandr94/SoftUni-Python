n = int(input())

name = input()
grade_sum = 0
final_sum = 0
count = 0

while name != 'Finish':
    count += 1
    for i in range(1, n + 1):
        grade = float(input())
        grade_sum += grade

    print(f'{name} - {grade_sum / n:.2f}.')
    final_sum += grade_sum / n
    grade_sum = 0
    name = input()

print(f"Student's final assessment is {final_sum / count:.2f}.")