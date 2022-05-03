one_leva_coins = int(input())
two_leva_coins = int(input())
five_leva_banknote = int(input())
money = int(input())


for one in range(0, one_leva_coins + 1):
    for two in range(0, two_leva_coins + 1):
        for five in range(0, five_leva_banknote + 1):
            if (one * 1) + (two * 2) + (five * 5) == money:
                print(f'{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {(one * 1) + (two * 2) + (five * 5)} lv.')