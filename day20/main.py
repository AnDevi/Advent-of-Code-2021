#!/usr/bin/python3

from pathlib import Path

dir_x = [-1, 0,   1, -1, 0, 1, -1, 0, 1]
dir_y = [-1, -1, -1,  0, 0, 0,  1, 1, 1]

def grid_print(grid):
	w, h = len(grid[0]), len(grid)
	for y in range(h):
		print(''.join([grid[y][x] for x in range(w)]))
	print()

def count(grid):
	w, h, res = len(grid[0]), len(grid), 0
	for y in range(h):
		for x in range(w):
			res += 1 if grid[y][x] == '#' else 0
	return res

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day20/day20.txt'), "r")
enhancement_algorithm, grid_input = file.read().split('\n\n')
file.close()
grid_middle = [[sign for sign in line] for line in grid_input.split('\n')]
w, h = len(grid_middle[0]), len(grid_middle)
infinite = 50
infinite_w, infinite_h =  w + 2 * infinite, h + 2 * infinite
grid = [['.' for _ in range(infinite_w)] for _ in range(infinite_h)]
for y in range(infinite, infinite + h):
	for x in range(infinite, infinite + w):
		grid[y][x] = grid_middle[y - infinite][x - infinite]

ENHANCMENTS = 50
for enc in range(ENHANCMENTS):
	# Part1
	if enc == 2:
		part1 = count(grid)
		print(f'Part 1: {part1}')
	new_grid = [['.' for _ in range(infinite_w)] for _ in range(infinite_h)]
	for y in range(0, infinite_h):
		for x in range(0, infinite_w):
			number_string = ""
			for dx, dy in zip(dir_x, dir_y):
				cx, cy = x + dx, y + dy
				if cx < 0 or cy < 0 or cx >= infinite_w or cy >= infinite_h:
					number_string += '1' if grid[y][x] == '#' else '0'
					continue
				number_string += '1' if grid[cy][cx] == '#' else '0'
			number = int(number_string, 2)
			new_grid[y][x] = enhancement_algorithm[number]
	grid = new_grid

part2 = count(grid)
print(f'Part 2: {part2}')
