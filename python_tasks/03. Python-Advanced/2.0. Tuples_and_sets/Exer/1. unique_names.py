n = int(input())

unique_names = set()

for i in range(n):
    names = input()

    unique_names.add(names)


for name in unique_names:
    print(name)