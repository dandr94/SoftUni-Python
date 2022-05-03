length = int(input())
width = int(input())
height = int(input())
percent = float(input())

area = length * width * height
litres = area * 0.001
percent_taken = percent * 0.01
litres_needed = litres * (1 - percent_taken)
print(litres_needed)