from collections import deque


def stock_availability(product_list, delivery_or_sell, *args):
    result = deque(product_list)

    if delivery_or_sell == 'delivery':
        for item in args:
            result.append(item)
    elif delivery_or_sell == 'sell':
        if args:
            for item in args:
                if str(item).isdigit():
                    sold = item

                    for i in range(sold):
                        if result:
                            result.popleft()
                else:
                    while item in result:
                        result.remove(item)
        else:
            if result:
                result.popleft()

    return list(result)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
