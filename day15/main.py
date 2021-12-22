#!/usr/bin/python3

from pathlib import Path
import heapq

dir_x = [1,  -1,  0,  0]
dir_y = [0,   0 , 1, -1]

def grid_print(grid):
	w, h = len(grid[0]), len(grid)
	for y in range(h):
		print(''.join([grid[y][x] for x in range(w)]))
	print()

def bfs(grid, grid_size):
	w, h = len(grid[0]), len(grid)
	risk_grid = [[None for _ in range(w * grid_size)] for _ in range(h * grid_size)]
	queue = [(0, 0, 0)]
	while queue:
		(x, y, risk) = heapq.heappop(queue)
		if x < 0 or x >= w * grid_size or y < 0 or y >= h * grid_size:
			continue
		
		curr_risk = grid[y%h][x%w] + x//w + y//h
		if curr_risk > 9:
			curr_risk -= 9
		new_risk = risk + curr_risk

		if risk_grid[y][x] == None or new_risk < risk_grid[y][x]:
			risk_grid[y][x] = new_risk
		else:
			continue

		if x == w * grid_size - 1 and y == h * grid_size - 1:
			break

		for dx, dy in zip(dir_x, dir_y):
			cx = x + dx
			cy = y + dy
			heapq.heappush(queue, (cx, cy, risk_grid[y][x]))

	return risk_grid[w * grid_size -1][h * grid_size-1] - risk_grid[0][0]


file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day15/day15.txt'), "r")
grid = [[int(x) for x in line.strip()] for line in file.readlines()]
file.close()

risk = bfs(grid, 1) 
print(f'Part 1: {risk}')

risk = bfs(grid, 5) 
print(f'Part 1: {risk}')
