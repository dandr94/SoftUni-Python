version = input().split('.')
version_to_int = list(map(int, version))


for i in range(len(version_to_int) -1, -1, -1):
    if version_to_int[i] >= 9:
        version_to_int[i] = 0
    else:
        version_to_int[i] += 1
        break

print('.'.join(map(str, version_to_int)))
