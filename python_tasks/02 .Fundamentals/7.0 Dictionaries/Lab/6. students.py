x = input()

my_dict = {}

while ':' in x:
    x = x.split(':')
    name = x[0]
    student_id = x[1]
    course = x[2]
    if course not in my_dict:
        my_dict[course] = {}

    my_dict[course][name] = int(student_id)

    x = input()

if '_' in x:
    x = x.replace('_',' ')

if x in my_dict:
    for key, student_id in my_dict[x].items():
        print(f'{key} - {student_id}')