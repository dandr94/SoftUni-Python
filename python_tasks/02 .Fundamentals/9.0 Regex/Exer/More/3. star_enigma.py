import re

pattern_star = r'[sStTaArR]'
pattern_planet = r'@(?P<planet>[A-Za-z]+)[^\@\-\!\:\>]*\:(?P<population>[0-9]+)[^\@\-\!\:\>]*\!(?P<attack>[AD])\![^\@\-\!\:\>]*\-\>(?P<count>[0-9]+)'
n = int(input())

attacked_planets = []
destructed_planets = []

for i in range(n):
    code = input()

    result = re.findall(pattern_star, code)

    count = len(result)

    new_str = ''

    for letter in code:
        ascii_num = ord(letter) - count
        new_str += chr(ascii_num)

    planets = re.finditer(pattern_planet, new_str)

    for final in planets:
        if final.group('attack') == 'A':
            attacked_planets.append(final.group('planet'))
        elif final.group('attack') == 'D':
            destructed_planets.append(final.group('planet'))


print(f'Attacked planets: {len(attacked_planets)}')
for attacked in sorted(attacked_planets):
    print(f'-> {attacked}')
print(f'Destroyed planets: {len(destructed_planets)}')
for destroyed in sorted(destructed_planets):
    print(f'-> {destroyed}')

