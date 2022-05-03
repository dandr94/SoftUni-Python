my_items_quantity = {}
my_item_price = {}
my_dict_final = {}
cmd = input()
old_price = 0

while cmd != 'buy':
    cmd_split = cmd.split()
    name = cmd_split[0]
    price = float(cmd_split[1])
    quantity = int(cmd_split[2])

    if name not in my_items_quantity:
        my_items_quantity[name] = quantity
        my_item_price[name] = price
        my_dict_final[name] = my_item_price[name] * my_items_quantity[name]
    else:
        if my_item_price[name] != price:
            my_item_price[name] = price
            my_items_quantity[name] += quantity
            my_dict_final[name] = my_item_price[name] * my_items_quantity[name]
        else:
            my_items_quantity[name] += quantity
            my_dict_final[name] = my_item_price[name] * my_items_quantity[name]


    cmd = input()


for product, price in my_dict_final.items():
    print(f'{product} -> {price:.2f}')



