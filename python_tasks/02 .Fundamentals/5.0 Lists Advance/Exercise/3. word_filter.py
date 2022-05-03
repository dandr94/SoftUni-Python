string_of_words = input().split()


x = [element for element in string_of_words if len(element) % 2 == 0]

print('\n'.join(x))