#!/usr/bin/python3

from pathlib import Path

def grid_print(grid):
	w, h = len(grid[0]), len(grid)
	for y in range(h):
		print(''.join([grid[y][x] for x in range(w)]))
	print()

def find_common(grid, posX, h):
    c0, c1 = 0, 0
    for j in range(0, h):
        if int(grid[j][posX]) == 1:
            c1 += 1
        elif int(grid[j][posX]) == 0:
            c0 += 1
    return c0, c1

def find_grid(grid, posX, w, h, most_common):
    c0, c1 = find_common(grid, posX, h)
    new_height, val, line_idx = 0, 0, 0
    if most_common:
        if c1 > c0 or c1 == c0:
            val, new_height = 1, c1
        elif c1 < c0:
            val, new_height = 0, c0
    else:
        if c1 > c0 or c1 == c0:
            val, new_height = 0, c0
        elif c1 < c0:
            val, new_height = 1, c1

    new_grid = [['.' for _ in range(w)] for _ in range(new_height)]

    for i in range(h):
        if int(grid[i][posX]) == val:
            for j in range(0, w):
                new_grid[line_idx][j] = grid[i][j]
            line_idx += 1

    return new_grid, new_height

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day3/day3.txt'), "r")
lines = file.read().splitlines()
file.close()
h = len(lines)
w = len(lines[0])

grid = [['.' for _ in range(w)] for _ in range(h)]

for i, line in enumerate(lines):
	for j in range(0, w):
		grid[i][j] = line[j]

mcommon, lcommon = "", ""

for posX in range(0, w):
    c0, c1 = find_common(grid, posX, h)
    if c1 > c0:
        mcommon += "1"
        lcommon += "0"
    elif c1 < c0: 
        lcommon += "1"
        mcommon += "0"

print(f'Part1 : {int(mcommon, 2) * int(lcommon, 2)}')

grid_O2, grid_CO2 = grid, grid
height_O2, height_CO2 = h, h
for posX in range(0, w):
    if height_O2 > 1:
        grid_O2, height_O2 = find_grid(grid_O2, posX, w, height_O2, True)
    if height_CO2 > 1:
        grid_CO2, height_CO2 = find_grid(grid_CO2, posX, w, height_CO2, False)

final_O2, final_CO2 = "", ""
for idx in range(0, w):
    final_O2  += grid_O2[0][idx]
    final_CO2  += grid_CO2[0][idx]
    
print(f'Part2 : {int(final_O2, 2) * int(final_CO2, 2)}')
