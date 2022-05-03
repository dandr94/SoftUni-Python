import re

txt = input()

pattern = r'(?P<url>(?P<sub_domain>www)\.(?P<domain>[A-Za-z0-9]+(\-[A-Za-z0-9]+)*)(?P<domain_ext>\.[a-z]+)+)'

while txt:
    result = re.finditer(pattern, txt)

    for match in result:
        print(match.group())

    txt = input()