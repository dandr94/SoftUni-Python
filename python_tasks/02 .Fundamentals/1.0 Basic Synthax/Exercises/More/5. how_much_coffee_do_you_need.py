action = input()
count_coffee = 0
need_sleep = False

list_of_words = ['coding', 'dog', 'cat', 'movie']

while action != 'END':

    if action.islower():
        for item in list_of_words:
            if action == item:
                count_coffee += 1

    elif action.isupper():
        for i in range(len(list_of_words)):
            upper_list = list_of_words[i].upper()
            if upper_list == action:
                count_coffee += 2

    if count_coffee > 5:
        need_sleep = True
        break

    action = input()

if need_sleep:
    print('You need extra sleep')
else:
    print(count_coffee)