unsatisfactory_assessments = int(input())


count = 0
sum = 0
bad_grade = False
last_problem = ''
number_of_problems = 0
problem_name = input()

while problem_name != 'Enough':
    grade = float(input())
    sum += grade
    last_problem = problem_name
    number_of_problems += 1
    if grade <= 4:
        count += 1
        if count == unsatisfactory_assessments:
            bad_grade = True
            break
    problem_name = input()
if bad_grade:
    print(f'You need a break, {count} poor grades.')
else:
    print(f'Average score: {sum / number_of_problems:.2f}')
    print(f'Number of problems: {number_of_problems}')
    print(f'Last problem: {last_problem}')

