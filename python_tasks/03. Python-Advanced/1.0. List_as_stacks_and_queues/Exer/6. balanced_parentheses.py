txt = input()

stack = []
balanced_pairs = True
bracket_pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
}
for el in txt:
    if el in '{[(':
        stack.append(el)
    else:
        if not stack:
            balanced_pairs = False
            break
        last_bracket = stack.pop()
        if bracket_pairs[last_bracket] != el:
            balanced_pairs = False
            break

if balanced_pairs and not stack:
    return True
else:
    return False