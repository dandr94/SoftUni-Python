import re

txt = input()

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

result = re.findall(pattern, txt)

print(*result)