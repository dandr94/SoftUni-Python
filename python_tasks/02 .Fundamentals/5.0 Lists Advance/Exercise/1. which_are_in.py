string_of_words_needed = input().split(', ')
string_of_words = input().split(', ')


new_list = []


for i in string_of_words_needed:
    for b in string_of_words:
        if i in b:
            new_list.append(i)
            break

print(new_list)


