def math_operations(*args, **kwargs):
    x = [int(x) for x in args]

    while x:
        number = x.pop(0)

        kwargs['a'] += number

        if x:
            number = x.pop(0)
            kwargs['s'] -= number

        if x:
            number = x.pop(0)
            if number != 0:
                kwargs['d'] /= number

        if x:
            number = x.pop(0)
            kwargs['m'] *= number

    return kwargs
