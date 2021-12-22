#!/usr/bin/python3

from pathlib import Path
import copy

SIZE = 10
DAY = 100

dir_x = [1, -1,  0,  0,  1, 1, -1, -1]
dir_y = [0,  0,  1, -1, -1, 1,  1, -1]

def grid_print(grid):
	w, h = len(grid[0]), len(grid)
	for y in range(h):
		print(''.join([grid[y][x] for x in range(w)]))
	print()

def did_add(flashed, p):
    prevSize = len(flashed)
    flashed.add(p)
    return True if prevSize != len(flashed) else False

def flash(grid, x, y, flashed):
	for dx, dy in zip(dir_x, dir_y):
		cx, cy = x + dx, y + dy

		if cx < 0 or cy < 0 or cx >= SIZE or cy >= SIZE:
			continue

		grid[cy][cx] += 1
		if grid[cy][cx] > 9:
			if did_add(flashed, (cx, cy)):
				flash(grid, cx, cy, flashed)		

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day11/day11.txt'), "r")
grid = [[int(num) for num in line.strip()] for line in file.readlines()]
file.close()
flashes = 0

grid_part1 = copy.deepcopy(grid)
for d in range(0, DAY):
	flashed = set()
	for i in range(0, SIZE):
		for j in range(0, SIZE): 
			grid_part1[i][j] += 1
	for i in range(0, SIZE):
		for j in range(0, SIZE): 
			if grid_part1[i][j] > 9:
				if did_add(flashed, (j, i)):
					flash(grid_part1, j, i, flashed)
	for i in range(0, SIZE):
		for j in range(0, SIZE): 
			if grid_part1[i][j] > 9:
				flashes += 1
				grid_part1[i][j] = 0

print(f'Part1 : {flashes}')

grid_part2 = copy.deepcopy(grid)
day_part2 = 0
while True:
	day_part2  += 1
	flashed = set()
	for i in range(0, SIZE):
		for j in range(0, SIZE): 
			grid_part2[i][j] += 1
	for i in range(0, SIZE):
		for j in range(0, SIZE): 
			if grid_part2[i][j] > 9:
				if did_add(flashed, (j, i)):
					flash(grid_part2, j, i, flashed)
	single_day_flashed = 0
	for i in range(0, SIZE):
		for j in range(0, SIZE): 
			if grid_part2[i][j] > 9:
				flashes += 1
				single_day_flashed += 1
				grid_part2[i][j] = 0
	if single_day_flashed == 100:
		break

print(f'Part2 : {day_part2}')
