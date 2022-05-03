first_string = input()
second_string = input()

last_word = first_string

for i in range(len(first_string)):
    first_part = second_string[:i + 1]
    second_part = first_string[i + 1:]

    word = first_part + second_part

    if last_word == word:
        continue
    print(word)
    last_word = word

