import re

txt = input()

pattern = r'(?P<day>\d{2})(?P<separator>[-/\.])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b'

result = re.finditer(pattern,txt)

for match in result:
    date = match.groupdict()
    print(f'Day: {date["day"]}, Month: {date["month"]}, Year: {date["year"]}')
