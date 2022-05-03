junior_bikers = int(input())
senior_bikers = int(input())
trace = input()

junior_tax = 0
senior_tax = 0
sum_tax = 0

if trace == 'trail':
    junior_tax = junior_bikers * 5.50
    senior_tax = senior_bikers * 7

elif trace == 'cross-country':
    junior_tax = junior_bikers * 8
    senior_tax = senior_bikers * 9.50
    sum_of_people = junior_bikers + senior_bikers
    if sum_of_people >= 50:
        sum_tax = junior_tax + senior_tax
        sum_tax -= sum_tax * 0.25
        junior_tax = 0
        senior_tax = 0

elif trace == 'downhill':
    junior_tax = junior_bikers * 12.25
    senior_tax = senior_bikers * 13.75

elif trace == 'road':
    junior_tax = junior_bikers * 20.
    senior_tax = senior_bikers * 21.50


sum = junior_tax + senior_tax + sum_tax

sum -= sum * 0.05

print(f'{sum:.2f}')