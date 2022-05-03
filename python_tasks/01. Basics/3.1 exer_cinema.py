projection = input()
r = int(input())
c = int(input())

full_cinema = r * c
sum = 0

if projection == 'Premiere':
    sum = full_cinema * 12.00

elif projection == 'Normal':
    sum = full_cinema * 7.50

else:
    sum = full_cinema * 5.00

print(f'{sum:.2f} leva')