
number = input()

prime_sum = 0
non_prime_sum = 0

while number != 'stop':
    num = int(number)
    if num >= 0:
        for i in range(2, num):
            if num % i == 0:
                non_prime_sum += num
                break
        else:
            prime_sum += num

    else:
        print('Number is negative.')

    number = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')

