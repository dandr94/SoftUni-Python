import re

txt = input()

pattern = r'\b\_(?P<name>[A-Za-z0-9]+)\b'

result = re.finditer(pattern, txt)

print(','.join([x.group('name') for x in result]))