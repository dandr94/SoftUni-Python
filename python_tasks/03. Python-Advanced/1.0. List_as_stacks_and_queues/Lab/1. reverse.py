txt = input()

stack = []

for i in txt:
    stack.append(i)

while stack:
    element = stack.pop()
    print(element, end='')

# print(input()[::-1)
