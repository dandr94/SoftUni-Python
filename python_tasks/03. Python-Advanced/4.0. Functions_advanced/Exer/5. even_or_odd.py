def even_odd(*args):
    result = []
    cmd = args[-1]

    for i in args[:-1]:
        if cmd == 'even':
            if i % 2 == 0:
                result.append(i)
        else:
            if i % 2 != 0:
                result.append(i)

    return result


