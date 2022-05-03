number_of_guests = int(input())

vip = set()
regular = set()

for i in range(number_of_guests):
    reservation_codes = input()

    if len(reservation_codes) != 8:
        continue

    if reservation_codes[0].isdigit():
        vip.add(reservation_codes)
    elif reservation_codes[0].isalpha():
        regular.add(reservation_codes)


while True:
    guests = input()

    if guests == 'END':
        break
    if guests in vip:
        vip.remove(guests)
    elif guests in regular:
        regular.remove(guests)

print(f"{len(regular) + len(vip)}")

for key in sorted(vip):
    print(key)
for key in sorted(regular):
    print(key)



