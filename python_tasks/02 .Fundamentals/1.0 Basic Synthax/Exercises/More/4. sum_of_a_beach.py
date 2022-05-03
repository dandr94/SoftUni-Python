string_word = input().lower()

count = 0

list_of_needed_word = ['sand', 'fish', 'water', 'sun']

for words in list_of_needed_word:
    if words in string_word:
        count += string_word.count(words)

print(count)
