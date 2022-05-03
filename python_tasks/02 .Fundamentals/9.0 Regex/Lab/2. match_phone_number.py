import re

phone_number = input()

# use ^
pattern = r'\+359([\s-])2(\1)\d{3}(\1)\d{4}\b'

result = re.finditer(pattern, phone_number)

print(', '.join([x.group() for x in result]))