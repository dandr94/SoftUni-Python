first_letter = input()
second_letter = input()
third_letter = input()

winners = ''
count = 0
for symbol_1 in range(ord(first_letter), ord(second_letter) +1):
    for symbol_2 in range(ord(first_letter), ord(second_letter) + 1):
        for symbol_3 in range(ord(first_letter), ord(second_letter) + 1):
            if chr(symbol_1) != third_letter and chr(symbol_2) != third_letter and chr(symbol_3) != third_letter:
                count += 1
                winners += f'{chr(symbol_1)}{chr(symbol_2)}{chr(symbol_3)} '

print(f'{winners}{count}')