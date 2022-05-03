from collections import deque

queue = deque()

while True:
    txt = input()

    if txt == 'End':
        break
    elif txt == 'Paid':
        for i in range(len(queue)):
            print(queue.popleft())
        continue

    queue.append(txt)

print(f'{len(queue)} people remaining.')


