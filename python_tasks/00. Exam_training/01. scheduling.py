jobs = [int(x) for x in input().split(', ')]
idx = int(input())

sum_of = 0

while jobs:
    index = jobs.index(min(jobs))
    current = jobs.pop(index)
    jobs.insert(index, 999)

    sum_of += current

    if index == idx:
        break

print(sum_of)