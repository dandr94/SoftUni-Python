def get_magic_triangle(rows):
    triangle = [[1], [1, 1]]

    row = [1, 1]

    for _ in range(2, rows):
        row = [1] + [sum(column) for column in zip(row[1:], row)] + [1]
        triangle.append(row)

    return triangle


print(get_magic_triangle(5))

