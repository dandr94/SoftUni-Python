import math

days = int(input())
left_food = int(input()) # kg
food_for_the_dog = float(input()) # kg
food_for_the_cat = float(input()) # kg
food_for_the_turtle = float(input()) # gr


dog = food_for_the_dog * days
cat = food_for_the_cat * days
turtle = (food_for_the_turtle * days) / 1000
sum = dog + cat + turtle

if sum <= left_food:
    diff = left_food - sum
    print(f'{math.floor(diff)} kilos of food left.')

else:
    diff = sum - left_food
    print(f'{math.ceil(diff)} more kilos of food are needed.')
