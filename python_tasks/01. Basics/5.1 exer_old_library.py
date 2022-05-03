book_name = input()


book = input()
count = 0

while book != book_name:
    if book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {count} books.')
        quit()
    count += 1
    book = input()


print(f'You checked {count} books and found it.')

