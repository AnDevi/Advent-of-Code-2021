#!/usr/bin/python3

from pathlib import Path
import math
import re

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __str__(self):
		return f'Point x {self.x} y {self.y}'
	def __repr__(self):
		return f'Point(x={self.x}, y={self.y})'

class Vec:
	def __init__(self, beg, end):
		self.beg = beg
		self.end = end
	def __str__(self):
		return f'Vec beg {self.beg} end {self.end}'
	def __repr__(self):
		return f'Vec(beg={self.beg}, end={self.end})'

def grid_print(grid):
	w, h = len(grid[0]), len(grid)
	for y in range(h):
		print(''.join([str(grid[y][x]) for x in range(w)]))
	print()

def count(grid):
	w, h, res = len(grid[0]), len(grid), 0 
	for j, i in [(j, i) for i in range(h) for j in range(w)]:
		res += 1 if grid[i][j] != '.' and grid[i][j] >= 2 else 0
	return res

def find_points(v, count_diag=False):
	points = []
	if not count_diag:
		if v.beg.x == v.end.x:
			beg, end = min(v.beg.y, v.end.y), max(v.beg.y, v.end.y)
			for n in range(beg, end + 1):
				points.append(Point(v.beg.x, n))
		elif v.beg.y == v.end.y:
			beg, end = min(v.beg.x, v.end.x), max(v.beg.x, v.end.x)
			for n in range(beg, end + 1):
				points.append(Point(n, v.beg.y))
	elif count_diag:
		degree = math.degrees(math.atan2(v.beg.y - v.end.y, v.beg.x - v.end.x))
		if (abs(degree) == 45 or abs(degree) == 135):
			beg, end = v.beg, v.end
			diff = 1
			#revert X
			if v.beg.x > v.end.x:
				beg = v.end
				end = v.beg
			#revert Y
			if beg.y > end.y:
				diff = -1
			beg_y = beg.y
			for x in range(beg.x, end.x + 1):
				points.append(Point(x, beg_y))
				beg_y += diff
	return points


LOG_RE = re.compile(r"^(\d+),(\d+) -> (\d+),(\d+)$")
file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day5/day5.txt'), "r")
vectors = []
for line in file:
	m = re.match(LOG_RE, line)
	vectors.append(Vec(Point(int(m.group(1)), int(m.group(2))), Point(int(m.group(3)), int(m.group(4)))))
file.close()
xmax = 0
ymax = 0
for v in vectors:
	if v.beg.x > xmax or v.end.x > xmax:
		xmax = max(v.beg.x, v.end.x)
	if v.beg.y > ymax or v.end.y > ymax:
		ymax = max(v.beg.y, v.end.y)

w, h = xmax + 1, ymax + 1
grid = [['.' for _ in range(w)] for _ in range(h)] 

for v in vectors:
	points = find_points(v)
	for p in points:
		if grid[p.y][p.x] == '.':
			grid[p.y][p.x] = 1
		else:
			grid[p.y][p.x] += 1

print(f'Part1 : {count(grid)}')

for v in vectors:
	points = find_points(v, True)
	for p in points:
		if grid[p.y][p.x] == '.':
			grid[p.y][p.x] = 1
		else:
			grid[p.y][p.x] += 1
		
print(f'Part2 : {count(grid)}')