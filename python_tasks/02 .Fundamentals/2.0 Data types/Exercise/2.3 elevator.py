import math

number_of_people = int(input())
capacity = int(input())

result = math.ceil(number_of_people / capacity)
print(result)