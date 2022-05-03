def shopping_list(budget: int, **kwargs):
    my_dict = {}

    if budget < 100:
        return 'You do not have enough budget.'
    if kwargs:
        for item, values in kwargs.items():
            sum_of_products = values[0] * values[1]
            if budget >= sum_of_products:
                if item not in my_dict:
                    my_dict[item] = sum_of_products
                else:
                    my_dict[item] += sum_of_products
                budget -= sum_of_products
            if len(my_dict) == 5:
                break

    output = ''
    for key, value in my_dict.items():
        output += f'You bought {key} for {value:.2f} leva.\n'

    return output


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
