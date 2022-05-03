w = int(input())
l = int(input())
h = int(input())

free_space = w * l * h
sum = 0

box = input()

while box != 'Done':
    box = int(box)
    sum += box
    if free_space < sum:
        diff = sum - free_space
        print(f'No more free space! You need {diff} Cubic meters more.')
        quit()
    box = input()
    if box == 'Done':
        diff = free_space - sum
        print(f'{diff} Cubic meters left.')
