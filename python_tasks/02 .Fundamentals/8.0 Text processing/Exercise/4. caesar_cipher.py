text = input()

for i in range(len(text)):
    ord_num = ord(text[i])
    print(f'{chr(ord_num + 3)}', end='')

# x = [chr(ord(ch) + 3) for ch in text]