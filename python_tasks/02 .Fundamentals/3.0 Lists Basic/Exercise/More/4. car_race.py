list_of_numbers = input().split(' ')

list_to_int = list(map(int, list_of_numbers))

middle = len(list_of_numbers) // 2

first_racer_time = 0
second_racer_time = 0

for first in range(0, middle):
    if list_to_int[first] == 0:
        first_racer_time -= first_racer_time * 0.20
    else:
        first_racer_time += list_to_int[first]

for second in range(len(list_to_int) - 1, middle, - 1):
    if list_to_int[second] == 0:
        second_racer_time -= second_racer_time * 0.20
    else:
        second_racer_time += list_to_int[second]

if first_racer_time < second_racer_time:
    print(f"The winner is left with total time: {first_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {second_racer_time:.1f}")