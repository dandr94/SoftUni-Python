def tags(my_tag):
    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            return f'<{my_tag}>{result}</{my_tag}>'

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))

