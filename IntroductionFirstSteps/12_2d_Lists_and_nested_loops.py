number_grid = [
    [1, 3, 4, 5, 6],
    [2, 35, 44, 56, 66],
    [15, 3, 45, 55, 62]
]

print(number_grid[2][0])

for row in number_grid:
    print(row)

for row in number_grid:
    for column in row:
        print(column)
