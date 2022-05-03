import math

n = int(input())

odd = set()
even = set()

for i in range(1, n + 1):
    name = input()

    sum_of_ascii = 0

    for letter in name:
        sum_of_ascii += ord(letter)

    floor_divide = math.floor(sum_of_ascii / i)

    if floor_divide % 2 == 0:
        even.add(floor_divide)
    else:
        odd.add(floor_divide)


sum_odd = sum(odd)
sum_even = sum(even)

if sum_odd == sum_even:
    union = odd | even
    print(', '.join(str(x) for x in union))

elif sum_even > sum_odd:
    symmetric = odd ^ even
    print(', '.join(str(x) for x in symmetric))

elif sum_odd > sum_even:
    difference = odd - even
    print(', '.join(str(x) for x in difference))