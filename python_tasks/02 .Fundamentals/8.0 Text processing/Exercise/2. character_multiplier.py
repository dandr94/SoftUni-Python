some_string = input().split()
word_1 = some_string[0]
word_2 = some_string[1]

total_sum = 0

shortest_word = min(len(word_1), len(word_2))

for i in range(shortest_word):
    first_chr = word_1[i]
    second_chr = word_2[i]

    total_sum += ord(first_chr) * ord(second_chr)

longest_word = max(len(word_1), len(word_2))

for i in range(shortest_word, longest_word):
    if len(word_1) > len(word_2):
        total_sum += ord(word_1[i])
    else:
        total_sum += ord(word_2[i])

print(total_sum)

