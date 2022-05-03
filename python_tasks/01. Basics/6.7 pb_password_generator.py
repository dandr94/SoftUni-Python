num_1 = int(input())
num_2 = int(input())
maximum_passwords = int(input())

for max in range(1, maximum_passwords + 1):
    for symbol_1 in range(35, 55 + 1):
        for symbol_2 in range(64, 96 + 1):
            for symbol_3 in range(1, num_1 + 1):
                for symbol_4 in range(1, num_2 + 1):
                    print(f'{chr(symbol_1)}{chr(symbol_2)}{symbol_3}'
                          f'{symbol_4}{chr(symbol_2)}{chr(symbol_1)}', end='|')
                    max += 1
                    symbol_1 += 1
                    symbol_2 += 1
                    if symbol_1 == 56:
                        symbol_1 = 35
                    if symbol_2 == 97:
                        symbol_2 = 64

                    if max > maximum_passwords or symbol_3 == num_1 and symbol_4 == num_2:
                        quit()



