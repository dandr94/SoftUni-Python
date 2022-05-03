import math
w = float(input())
h = float(input())

metres_to_cm_width = w * 100
metres_to_cm_height = h * 100

height = metres_to_cm_height - 100

desk = height / 70

lines = metres_to_cm_width / 120

places = math.floor(lines) * math.floor(desk) - 3

print(places)