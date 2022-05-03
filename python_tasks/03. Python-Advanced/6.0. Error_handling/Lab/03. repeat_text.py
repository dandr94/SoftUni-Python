text = input()

try:
    times_to_repeat_the_input = int(input())
    for _ in range(times_to_repeat_the_input):
        print(text, end='')
except ValueError:
    print('Variable times must be an integer')
