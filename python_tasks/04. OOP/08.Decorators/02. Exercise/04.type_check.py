def type_check(my_type):
    def decorator(function):
        def wrapper(some_type):
            if type(some_type) != my_type:
                return 'Bad Type'

            return function(some_type)

        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

