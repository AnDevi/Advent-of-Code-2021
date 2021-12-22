#!/usr/bin/python3

from pathlib import Path
from collections import Counter

def grid_print(grid,w, h):
	for y in range(h):
		print(''.join([grid[y][x] for x in range(w)]))
	print()

def count(grid):
	w, h = len(grid[0]), len(grid)
	return Counter([grid[i][j] for i in range(h) for j in range(w)])['#']

def fold(axis, fold_pos, grid, new_w, new_h):
	w, h = len(grid[0]), len(grid)
	if axis == 'x':
		new_w = (new_w - 1) // 2
		for i in range(0, h):
			for j in range(0, fold_pos):
				if grid[i][fold_pos + fold_pos - j] == '#':
					grid[i][j] = '#'
					grid[i][fold_pos + fold_pos - j] = '.'
	if axis == 'y':
		new_h = (new_h - 1) // 2
		for i in range(0, fold_pos):
			for j in range(0, w):
				if grid[fold_pos + fold_pos - i][j] == '#':
					grid[i][j] = '#'
					grid[fold_pos + fold_pos - i][j] = '.'
	return new_w, new_h

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day13/day13.txt'), "r")
points_string, folds_string = file.read().split('\n\n')
file.close()
fold_str = "fold along "
points = [(int(x), int(y)) for x, y in [line.strip().split(',') for line in points_string.splitlines()]]	
folds = [(axis, int(fold_pos)) for axis, fold_pos in  [line.strip()[len(fold_str):].split('=') for line in folds_string.split('\n')]]

max_x = max(x for x, _ in points)
max_y = max(y for _, y in points)
for axis, fold_pos in folds:
	if axis == 'x':
		max_x = 2 * fold_pos if 2 * fold_pos > max_x else max_x
	elif axis == 'y':
		max_y = 2 * fold_pos if 2 * fold_pos > max_y else max_y
w, h = max_x + 1, max_y + 1

grid = [['.' for _ in range(w)] for _ in range(h)]
for x, y in points:
	grid[y][x] = '#'

new_w, new_h = w, h
new_w, new_h = fold(folds[0][0], folds[0][1], grid, new_w, new_h)
part1 = count(grid)

print(f'Part 1: {part1}')	

for axis, fold_pos in folds[1:]:
	new_w, new_h = fold(axis, fold_pos, grid, new_w, new_h)

print("Part 2:")
grid_print(grid, new_w, new_h)
