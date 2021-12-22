#!/usr/bin/python3

from pathlib import Path
from collections import deque

dir_x = [1, -1, 0,  0]
dir_y = [0,  0, -1, 1]

def grid_print(grid):
	w, h = len(grid[0]), len(grid)
	for y in range(h):
		print(''.join([str(grid[y][x]) for x in range(w)]))
	print()

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day9/day9.txt'), "r")
grid = [[int(x) for x in list(line.strip())] for line in file]
file.close()
h = len(grid)
w = len(grid[0])

minimums = []
for y in range(0, h):
    for x in range(0, w):
        isMin = True
        for dx, dy in zip(dir_x, dir_y):
            cx = x + dx
            cy = y + dy
            if cx < 0 or cy < 0 or cx >= w or cy >= h:
                continue
            if grid[cy][cx] <= grid[y][x]:
                isMin = False
                break
        if isMin:
            minimums.append(grid[y][x])

part1 = sum(minimums) + len(minimums)
print(f'Part1 : {part1}')

basin_sizes = []
seen = set()
for y in range(0, h):
    for x in range(0, w):
        if (x, y) not in seen and grid[y][x] != 9:
            size = 0
            q = deque()
            q.append((x, y))
            while q:
                (x, y) = q.popleft()
                if (x, y) in seen:
                    continue

                size += 1
                seen.add((x, y))

                for dx, dy in zip(dir_x, dir_y):
                    cx = x + dx
                    cy = y + dy

                    if 0 <= cx < w and 0 <= cy < h and grid[cy][cx] != 9:
                        q.append((cx, cy))              
        
            basin_sizes.append(size)

basin_sizes = sorted(basin_sizes)
part2 = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
print(f'Part2 : {part2}')
