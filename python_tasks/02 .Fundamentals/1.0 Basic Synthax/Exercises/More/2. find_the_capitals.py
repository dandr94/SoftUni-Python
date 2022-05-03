
word = input()

capitals = []

for index, letter in enumerate(word):
    if letter.isupper():
        capitals.append(index)

print(capitals)