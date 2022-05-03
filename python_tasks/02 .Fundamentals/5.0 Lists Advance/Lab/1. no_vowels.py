def remove_vowels_from_word(word: str):

    vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

    remove_vowels = ''.join([letters for letters in word if letters not in vowels])

    return remove_vowels


input_word = input()

print(remove_vowels_from_word(input_word))


