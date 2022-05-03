some_strings = input()

numbers = ''
letters = ''
other = ''

for i in some_strings:
    if i.isdigit():
        numbers += i
    elif i.isalpha():
        letters += i
    else:
        other += i

print(numbers)
print(letters)
print(other)
