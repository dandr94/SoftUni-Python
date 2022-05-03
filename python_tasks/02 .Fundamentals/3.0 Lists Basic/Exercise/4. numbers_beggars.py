coins = input().split(", ")
beggars = int(input())
count = 0
beggars_list = [0] * beggars
for current_coin in coins:
    beggars_list[count] += int(current_coin)
    count += 1
    if count >= beggars:
        count = 0
print(beggars_list)



