file = open('numbers.txt')
lines = file.readlines()
print(sum([int(el) for el in lines]))
