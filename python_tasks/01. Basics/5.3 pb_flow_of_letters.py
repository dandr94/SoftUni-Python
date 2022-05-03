letter = input()

word = ''
global_count = 0
count_c = 0
count_o = 0
count_n = 0
while letter != "End":
    if letter == 'c':
        if count_c == 0:
            global_count += 1
        else:
            word += letter
        count_c += 1
    elif letter == 'o':
        if count_o == 0:
            global_count += 1
        else:
            word += letter
        count_o += 1
    elif letter == 'n':
        if count_n == 0:
            global_count += 1
        else:
            word += letter
        count_n += 1
    elif ord(letter) >= 65 and ord(letter) <= 90:
        word += letter
    elif ord(letter) >= 97 and ord(letter) <= 122:
        word += letter
    if global_count == 3:
        print(word, end=' ')
        word = ''
        global_count = 0
        count_c = 0
        count_n = 0
        count_o = 0
    letter = input()