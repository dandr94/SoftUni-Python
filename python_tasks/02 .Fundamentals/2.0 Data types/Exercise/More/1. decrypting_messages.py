key = int(input())
n = int(input())

for i in range(1, n +1):
    letter = input()
    letter_ord = ord(letter) + key
    print(f'{chr(letter_ord)}', end='')
