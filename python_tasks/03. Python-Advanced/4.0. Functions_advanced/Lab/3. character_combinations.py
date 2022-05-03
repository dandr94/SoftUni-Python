def char_combinations(string, index):
    if index >= len(string):
        print(''.join(string))
        return

    char_combinations(string, index + 1)
    for i in range(index + 1, len(string)):
        string[index], string[i] = string[i], string[index]
        char_combinations(string, index + 1)
        string[index], string[i] = string[i], string[index]


txt = list(input())
char_combinations(txt, 0)