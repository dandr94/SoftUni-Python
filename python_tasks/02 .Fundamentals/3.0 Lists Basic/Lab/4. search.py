n = int(input())
word = input()

word_list = []


for i in range(n):
    some_strings = input()

    word_list.append(some_strings)

print(word_list)

for b in range(len(word_list) - 1, -1, -1):
    element = word_list[b]
    if word not in word_list[b]:
        word_list.remove(element)

print(word_list)
