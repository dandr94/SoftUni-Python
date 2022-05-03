bad_words = input()
sentence = input()


while bad_words in sentence:
    sentence = sentence.replace(bad_words, '')

print(sentence)