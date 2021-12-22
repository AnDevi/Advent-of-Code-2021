#!/usr/bin/python3

from pathlib import Path

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day1/day1.txt'), "r")
numbers = [int(line) for line in file.read().splitlines()]
file.close()

result = 0
for x1, x2 in zip(numbers, numbers[1:]):
	if x2 > x1:
		result += 1

print(f'Part 1: {result}')

result = 0
for x1, x2, x3, x4 in zip(numbers, numbers[1:], numbers[2:], numbers[3:]):
	if x4 + x3 + x2 > x3 + x2 + x1:
		result += 1

print(f'Part 2: {result}')
				