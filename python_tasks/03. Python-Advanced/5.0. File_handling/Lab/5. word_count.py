# with open('words.txt', 'w') as words:
#     words.write('quick is fault')
#
# with open('text.txt', 'w') as text:
#     text.write("-I was quick to judge him, but it wasn't his fault.")
#     text.write("\n-Is this some kind of joke?! Is it?")
#     text.write('\n-Quick, hide here…It is safer.')

import re

with open('words.txt') as wrds:
    words = wrds.read().split()

words_dict = {}

with open('text.txt') as txt:
    text_file = txt.read().lower()

    for word in words:
        pattern = rf'\b{word}\b'
        result = re.findall(pattern, text_file)
        if result:
            if word not in words_dict:
                words_dict[word] = 0

            words_dict[word] = len(result)

with open('output.txt', 'w') as output:
    for word, amount in sorted(words_dict.items(), key=lambda x: -x[1]):
        output.write(f'{word} - {amount}\n')
