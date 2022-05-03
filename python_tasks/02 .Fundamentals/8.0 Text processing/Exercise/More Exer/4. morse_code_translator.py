morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..'
                   }

msg = input()


def decrypt(message):
    message += ' '

    decipher = ''
    code = ''
    for letter in message:
        if letter != ' ':
            if letter == '|':
                continue
            i = 0

            code += letter

        else:
            i += 1

            if i == 2:
                decipher += ' '

            else:
                decipher += list(morse_code_dict.keys())[list(morse_code_dict
                                                              .values()).index(code)]
                code = ''

    return decipher


print(decrypt(msg))
