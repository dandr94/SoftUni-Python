input_character_1 = input()
input_character_2 = input()


def ascii_range(char1, char2):
    result = ''

    for i in range(ord(input_character_1) + 1, ord(input_character_2)):
        result += chr(i) + ' '

    return result


print(f'{ascii_range(input_character_1, input_character_2)}')
