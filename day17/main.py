#!/usr/bin/python3

from pathlib import Path
import re

LOG_RE = re.compile(r"target area: x=(\d+)..(\d+), y=(-?\d+)..(-?\d+)")

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day17/day17.txt'), "r")
m = re.match(LOG_RE, file.readline().strip())
target_x_min  = int(m.group(1))
target_x_max = int(m.group(2))
target_y_min = int(m.group(3))
target_y_max = int(m.group(4))

file.close()

part1, part2 = 0, 0
good_shots = set()

start_x = 0
while start_x*(start_x-1)//2 < target_x_min:
	start_x+=1
for VX in range(start_x - 1, target_x_max):
	for VY in range(target_y_min, -target_y_min):
		x, y = 0, 0
		shot_max_y = 0
		vx, vy = VX, VY
		while y > target_y_min and x < target_x_max:			
			x, y = x+vx, y+vy	
			vx = max(0, vx-1)
			vy = vy-1
			shot_max_y = max(shot_max_y, y)
			if target_x_min <= x <= target_x_max and target_y_min <= y <= target_y_max:
				good_shots.add((VX, VY))
				part1 = max(shot_max_y, part1)

part2 = len(good_shots)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
