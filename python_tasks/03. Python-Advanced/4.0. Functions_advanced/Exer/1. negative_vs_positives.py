def negative_vs_positives(*args):
    negatives = 0
    positives = 0

    for i in args:
        for b in i:
            if b > 0:
                positives += b
            else:
                negatives += b

    if abs(negatives) > positives:
        return f'{negatives}\n{positives}\nThe negatives are stronger than the positives'

    return f'{negatives}\n{positives}\nThe positives are stronger than the negatives'


numbers = [int(x) for x in input().split()]
print(negative_vs_positives(numbers))