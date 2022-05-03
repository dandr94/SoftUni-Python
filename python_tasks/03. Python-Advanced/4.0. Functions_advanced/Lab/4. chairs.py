def chair_combinations(name, index, chair, comb):
    if len(comb) == chair:
        print(', '.join(comb))
        return

    for i in range(index, len(name)):
        comb.append(name[i])
        chair_combinations(name, i + 1, chair, comb)
        comb.pop()


names = input().split(', ')
chairs = int(input())

chair_combinations(names, 0, chairs, [])
