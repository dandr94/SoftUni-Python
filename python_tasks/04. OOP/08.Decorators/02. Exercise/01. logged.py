def logged(function):
    def wrapper(*args):
        result = f'you called {function.__name__}{args}'
        result_2 = function(*args)
        return result + '\n' + f'it returned {result_2}'

    return wrapper




@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

