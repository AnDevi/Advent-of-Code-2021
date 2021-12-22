#!/usr/bin/python3

from pathlib import Path
import re

INITIAL = 50

def count(grid):
	res = 0
	for z in range(-INITIAL, INITIAL):
		for y in range(-INITIAL, INITIAL):
			for x in range(-INITIAL, INITIAL):
				res += 1 if grid[z][y][x] else 0
	return res

LOG_RE = re.compile(r"(.+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)")
file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day22/day22.txt'), "r")
operations = []
converted_x,converted_y,converted_z = set(),set(),set()

for line in file.readlines():
	m = re.match(LOG_RE, line)
	status = True if m.group(1) == 'on' else False
	s_x = int(m.group(2)); e_x = int(m.group(3)) + 1
	s_y = int(m.group(4)); e_y = int(m.group(5)) + 1
	s_z = int(m.group(6)); e_z = int(m.group(7)) + 1
	operations.append((status,s_x,e_x,s_y,e_y,s_z,e_z))
	converted_x.add(s_x); converted_x.add(e_x)
	converted_y.add(s_y); converted_y.add(e_y)
	converted_z.add(s_z); converted_z.add(e_z)
file.close()

grid = [[[False for _ in range(-INITIAL, INITIAL)] for _ in range(-INITIAL, INITIAL)] for _ in range(-INITIAL, INITIAL)]
for status,s_x,e_x,s_y,e_y,s_z,e_z in operations:
	s_x = max(-INITIAL, s_x); e_x = min(INITIAL, e_x)
	s_y = max(-INITIAL, s_y); e_y = min(INITIAL, e_y)
	s_z = max(-INITIAL, s_z); e_z = min(INITIAL, e_z)
	for z in range(s_z, e_z):
		for y in range(s_y, e_y):
			for x in range(s_x, e_x):
				grid[z][y][x] = status

part1 = count(grid)
print(f'Part 1: {part1}')

converted_x=sorted(converted_x)
converted_y=sorted(converted_y)
converted_z=sorted(converted_z); 

converted_x_size = len(converted_x)
converted_y_size = len(converted_y)
converted_z_size = len(converted_z)
converted_grid = [[[False for _ in range(converted_x_size)] for _ in range(converted_y_size)] for _ in range(converted_z_size)]

for status,s_x,e_x,s_y,e_y,s_z,e_z in operations:
	conv_s_x = converted_x.index(s_x); conv_e_x = converted_x.index(e_x)
	conv_s_y = converted_y.index(s_y); conv_e_y = converted_y.index(e_y)
	conv_s_z = converted_z.index(s_z); conv_e_z = converted_z.index(e_z)

	for z in range(conv_s_z,conv_e_z):
		for y in range(conv_s_y,conv_e_y):
			for x in range(conv_s_x,conv_e_x):
				converted_grid[z][y][x]=status
			
part2 = 0
for z in range(converted_z_size):
	for y in range(converted_y_size):
		for x in range(converted_x_size):	
			if converted_grid[z][y][x]:
				part2 += (converted_x[x+1]-converted_x[x])*(converted_y[y+1]-converted_y[y])*(converted_z[z+1]-converted_z[z])

print(f'Part 2: {part2}')
