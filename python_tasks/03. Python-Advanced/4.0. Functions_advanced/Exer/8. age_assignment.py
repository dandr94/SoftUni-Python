def age_assignment(*args, **kwargs):
    result = {}
    for key, value in kwargs.items():
        for i in args:
            if i[0] == key:
                result[i] = value

    # for name in args:
    # first_letter = name[0]
    # result[name] = kwargs[first_letter]

    # result = {x: kwargs[x[0]] for x in args}

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
