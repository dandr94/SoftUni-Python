string_of_numbers = input().split(', ')
numbers_to_int = list(map(int, string_of_numbers))

positive = [str(element) for element in numbers_to_int if element >= 0]
negative = [str(element) for element in numbers_to_int if element < 0]
even = [str(element) for element in numbers_to_int if element % 2 == 0]
odd = [str(element) for element in numbers_to_int if element % 2 != 0]

positive = ', '.join(positive)
negative = ', '.join(negative)
even = ', '.join(even)
odd = ', '.join(odd)

print(f'Positive: {positive}')
print(f'Negative: {negative}')
print(f'Even: {even}')
print(f'Odd: {odd}')