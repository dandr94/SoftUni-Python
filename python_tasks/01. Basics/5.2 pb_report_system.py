expected_sum = int(input())

object_price = input()

sum_money = 0
count_cs = 0
count_cc = 0
count = 1
count_cs_money = 0
count_cc_money = 0

while object_price != 'End':
    object_price_int = int(object_price)

    if count % 2 != 0 and object_price_int <= 100:
        count_cs += 1
        count_cs_money += object_price_int
        print(f'Product sold!')
        sum_money += object_price_int
    elif count % 2 == 0 and object_price_int >= 10:
        count_cc += 1
        count_cc_money += object_price_int
        print(f'Product sold!')
        sum_money += object_price_int
    else:
        print(f'Error in transaction!')
    count += 1
    if sum_money >= expected_sum:
        break

    object_price = input()

if sum_money >= expected_sum:
    print(f'Average CS: {count_cs_money / count_cs:.2f} ')
    print(f'Average CC: {count_cc_money / count_cc:.2f} ')
else:
    print(f'Failed to collect required money for charity.')
