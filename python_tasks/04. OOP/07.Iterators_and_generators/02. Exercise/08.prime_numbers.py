def get_primes(integers: list):
    for num in integers:
        if num <= 1:
            continue
        for delim in range(2, num):
            if num % delim == 0:
                break
        else:
            yield num




print(list(get_primes([-2, 0, 0, 1, 1, 0])))
