def odd_or_even(x, *args):
    sum_of_numbers = []

    for i in args:
        for b in i:
            if x == 'Odd':
                if b % 2 != 0:
                    sum_of_numbers.append(b)
            else:
                if b % 2 == 0:
                    sum_of_numbers.append(b)

    return sum(sum_of_numbers)


txt = input()
numbers = [int(x) for x in input().split()]
print(odd_or_even(txt, numbers) * len(numbers))

# Better Solution
# command = input()
# numbers = [int(x) for x in input().split()]
# parity = 0 if command == 'Even' else 1
# filtered_sum = sum(filter(lambda x: x % 2 == parity, numbers))
# print(filtered_sum * len(numbers))
