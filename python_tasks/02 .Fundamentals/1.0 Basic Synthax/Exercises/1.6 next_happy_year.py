year = int(input())

magic_year = False

while not magic_year:
    year += 1
    length = len(str(year))
    if len(set(str(year))) == length:
        magic_year = True
        print(year)
        break
