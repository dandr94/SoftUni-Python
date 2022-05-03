import re

text = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, text)

result = [x.group() for x in matches]

print(*result)