from collections import deque

que = deque(input().split()[::-1])

while que:
    print(que.popleft(), end=' ')
