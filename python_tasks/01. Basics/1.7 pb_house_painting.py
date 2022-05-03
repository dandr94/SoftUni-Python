x = float(input())
y = float(input())
h = float(input())

# walls
side_wall = x * y
window = 1.5 * 1.5
both_walls = side_wall * 2 - window * 2
back_wall = x * x
front_door = 1.2 * 2
both_front_and_back = back_wall * 2 - front_door
walls_area =  both_walls + both_front_and_back

# roof
roof_rectangles = 2 * (x * y)
roof_triangles = 2 * (x * h / 2)
roof_area = roof_rectangles + roof_triangles

green_paint_needed = walls_area / 3.4
red_paint_needed = roof_area / 4.3

print(f'{green_paint_needed:.2f}')
print(f'{red_paint_needed:.2f}')
