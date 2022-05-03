txt = input()

freq = {}

for i in txt:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for letter, count in sorted(freq.items()):
    print(f'{letter}: {count} time/s')