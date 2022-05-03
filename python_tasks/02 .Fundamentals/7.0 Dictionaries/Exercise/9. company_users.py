cmd = input()

my_dict = {}

while cmd != 'End':
    cmd_split = cmd.split(' -> ')
    company_name = cmd_split[0]
    employee_id = cmd_split[1]

    if company_name not in my_dict:
        my_dict[company_name] = []

    if employee_id not in my_dict[company_name]:
        my_dict[company_name].append(employee_id)

    cmd = input()

for key, value in sorted(my_dict.items(), key=lambda x:x[0]):
    print(f'{key}')
    for i in value:
        print(f'-- {i}')
