some_string = input().split()

new_string = ''

for i in range(len(some_string)):
    new_string += some_string[i] * len(some_string[i])

print(new_string)