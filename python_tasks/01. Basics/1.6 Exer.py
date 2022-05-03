days_in_campaign = int(input())
count_bakers = int(input())
count_cakes = int(input())
count_waffles = int(input())
count_pancakes = int(input())

sum_for_baker = (count_cakes * 45) + (count_waffles * 5.80) + (count_pancakes * 3.20)
sum_for_one_day = sum_for_baker * count_bakers
sum_for_campaign = sum_for_one_day * days_in_campaign
costs = sum_for_campaign - sum_for_campaign / 8
print(costs)