n = int(input())


sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0
sum_all = 0

for i in range(1, n + 1):
    grade = float(input())
    sum_all += grade
    if grade <= 2.99:
        sum_1 += 1
    elif grade >= 3.00 and grade <= 3.99:
        sum_2 += 1
    elif grade >= 4.00 and grade <=4.99:
        sum_3 += 1
    else:
        sum_4 += 1

percent_sum_1 = sum_1 / n * 100
percent_sum_2 = sum_2 / n * 100
percent_sum_3 = sum_3 / n * 100
percent_sum_4 = sum_4 / n * 100
percent_sum = sum_all / n

print(f'Top students: {percent_sum_4:.2f}%')
print(f'Between 4.00 and 4.99: {percent_sum_3:.2f}%')
print(f'Between 3.00 and 3.99: {percent_sum_2:.2f}%')
print(f'Fail: {percent_sum_1:.2f}%')
print(f'Average: {percent_sum:.2f}')
