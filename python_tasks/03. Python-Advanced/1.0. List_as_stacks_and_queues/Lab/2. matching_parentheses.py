txt = input()

stack = []

for i in range(len(txt)):
    if txt[i] == '(':
        stack.append(i)
    elif txt[i] == ')':
        start = stack.pop()
        print(txt[start: i + 1])