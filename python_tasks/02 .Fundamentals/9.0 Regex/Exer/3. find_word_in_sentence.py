import re

txt = input()
word = input()

pattern = rf'\b{word}\b'

print(len(re.findall(pattern, txt, flags=re.IGNORECASE)))