import re

txt = input()

pattern = r'\s([A-Za-z0-9]+[A-Za-z0-9\.\-\_]*\@[A-Za-z]+[A-Za-z0-9\-]*(\.[A-Za-z0-9]+[A-Za-z\-]*)+)\b'

result = re.finditer(pattern, txt)

for matches in result:
    print(matches.group())