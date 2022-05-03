n = int(input())

longest_intersection = []

for i in range(n):
    first, second = input().split('-')
    first_start, first_end = [int(x) for x in first.split(',')]
    second_start, second_end = [int(x) for x in second.split(',')]
    part_one = set(range(first_start, first_end + 1))
    part_two = set(range(second_start, second_end + 1))
    final = part_one & part_two

    if len(longest_intersection) < len(final):
        longest_intersection.clear()
        [longest_intersection.append(str(x)) for x in final]

print(f'Longest intersection is [{", ".join(longest_intersection)}] with length {len(longest_intersection)}')


