def vowel_filter(function):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

    def wrapper():
        result = function()
        filtered = [x for x in result if x.lower() in vowels]
        return filtered

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
