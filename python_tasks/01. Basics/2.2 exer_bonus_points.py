num = int(input())

sum = 0
bonus = 0

if num <= 100:
    bonus += 5
    sum += num + bonus

elif num > 100 and num < 1000:
    bonus += num * 0.20
    sum += num + bonus

else:
    bonus += num * 0.10
    sum += num + bonus

if num % 2 == 0:
    bonus += 1
    sum += 1
elif num % 10 == 5:
    bonus += 2
    sum += 2

print(bonus)
print(sum)

