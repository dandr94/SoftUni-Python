last_sector = input()
rows_in_first_sector = int(input())
quantity_of_places_on_odd_row = int(input())

count = 0

for sectors in range(65, ord(last_sector) + 1):
    for rows in range(1, rows_in_first_sector + 1):
        if rows % 2 != 0:
            for places_in_odd in range(97, 97 + quantity_of_places_on_odd_row):
                print(f'{chr(sectors)}{rows}{chr(places_in_odd)}')
                count += 1
        elif rows % 2 == 0:
            for places_in_even in range(97,  97 + quantity_of_places_on_odd_row  + 2):
                print(f'{chr(sectors)}{rows}{chr(places_in_even)}')
                count += 1
    rows_in_first_sector += 1

print(count)