cmd = input().split()
n = int(cmd[0])
m = int(cmd[1])

n_set = set()
m_set = set()

for i in range(n):
    num = input()

    n_set.add(num)

for b in range(m):
    num = input()

    m_set.add(num)

equal = n_set & m_set

for c in equal:
    print(c)
