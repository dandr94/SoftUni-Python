n = int(input())

sum_of_chars = 0

for i in range(1, n + 1):
    chars = input()

    sum_of_chars += ord(chars)

print(f'The sum equals: {sum_of_chars}')