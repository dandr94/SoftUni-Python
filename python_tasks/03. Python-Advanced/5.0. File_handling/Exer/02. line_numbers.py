# with open('line_numbers_input.txt', 'w') as line_txt:
#     line_txt.write("-I was quick to judge him, but it wasn't his fault.\n"
#                    "-Is this some kind of joke?! Is it?\n"
#                    "-Quick, hide here. It is safer.")
import re

with open('line_numbers_input.txt', 'r') as line_numbers:
    line = [line.strip() for line in line_numbers.readlines()]

with open('line_numbers_output.txt', 'w') as output:
    pattern_punctuation = r"[!\"',-.:;?_]"
    pattern_letter = r'[a-zA-Z]'

    for index, sentence in enumerate(line):
        find_punctuations = re.findall(pattern_punctuation, sentence)
        find_letters = re.findall(pattern_letter, sentence)
        output.write(f'Line {index + 1}: {sentence} ({len(find_letters)})({len(find_punctuations)})\n')

