def reverse_word(given_word: str):
    return print(f'{given_word} = {given_word[::-1]}')


cmd = input()

while cmd != 'end':
    word = cmd
    reverse_word(word)

    cmd = input()
