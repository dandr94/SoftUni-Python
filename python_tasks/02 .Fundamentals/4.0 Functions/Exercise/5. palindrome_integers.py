list_of_numbers = input().split(', ')


def is_palindrome():

    for i in list_of_numbers:
        result = str(i) == str(i)[::-1]
        print(result)


is_palindrome()