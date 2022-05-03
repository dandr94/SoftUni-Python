n_1 = set(int(x) for x in input().split())
n_2 = set(int(x) for x in input().split())

number_of_commands = int(input())

for i in range(number_of_commands):
    cmd = input()
    cmd_split = cmd.split()

    if 'Add First' in cmd:
        for num in cmd_split:
            if num.isdigit():
                n_1.add(int(num))

    elif 'Add Second' in cmd:
        for num in cmd_split:
            if num.isdigit():
                n_2.add(int(num))

    elif 'Remove First' in cmd:
        for num in cmd_split:
            if num.isdigit():
                if int(num) in n_1:
                    n_1.remove(int(num))

    elif 'Remove Second' in cmd:
        for num in cmd_split:
            if num.isdigit():
                if int(num) in n_2:
                    n_2.remove(int(num))

    elif 'Check Subset' in cmd:
        if n_1 > n_2:
            print('True')
        else:
            print('False')

print(', '.join(map(str, sorted(n_1))))
print(', '.join(map(str, sorted(n_2))))