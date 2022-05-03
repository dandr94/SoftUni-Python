string_of_people = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())


for i in range(len(string_of_people)):
    if string_of_people[i] < minimum_wealth:
        result = minimum_wealth - string_of_people[i]
        richest = string_of_people.index(max(string_of_people))
        string_of_people[richest] -= result
        string_of_people[i] += result

is_not_distributed = [False for element in string_of_people if element < minimum_wealth]

if is_not_distributed:
    print('No equal distribution possible')
else:
    print(string_of_people)


