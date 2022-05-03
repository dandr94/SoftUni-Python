n = int(input())

unique = set()

for i in range(n):
    [unique.add(x) for x in input().split()]

[print(x) for x in unique]

