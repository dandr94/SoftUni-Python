from collections import deque

n = int(input())

stack = deque()

for i in range(n):
    queries = input().split()
    cmd = queries[0]

    if cmd == '1':
        num = int(queries[1])
        stack.append(num)

    elif cmd == '2':
        if stack:
            stack.pop()

    elif cmd == '3':
        if stack:
            print(max(stack))

    elif cmd == '4':
        if stack:
            print(min(stack))


while stack:
    if len(stack) == 1:
        print(stack.pop())
    else:
        print(stack.pop(), end=', ')