#!/usr/bin/python3

from pathlib import Path
import re

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day2/day2.txt'), "r")
directions = [line.split() for line in file.read().splitlines()]
file.close()

depth, pos = 0, 0
for dir, value in directions:
	value = int(value)
	if dir == "forward":
		pos += value
	if dir == "up":
		depth -= value
	elif dir == "down":
		depth += value

result1 = depth * pos
print(f'Part 1 result: {result1}.')

depth, pos, aim = 0, 0, 0
for dir, value in directions:
	value = int(value)
	if dir == "forward":
		pos += value
		depth += value * aim
	if dir == "up":
		aim -= value
	elif dir == "down":
		aim += value

result2 = depth * pos
print(f'Part 2 result: {result2}')
