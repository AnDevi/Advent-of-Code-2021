#!/usr/bin/python3

from pathlib import Path
import sys

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day7/day7.txt'), "r")
crabs = [int(numeric_string) for numeric_string in file.readline().split(',')]
file.close()
crab_min = min(crabs)
crab_max = max(crabs)

fuel_min = sys.maxsize
for n in range(crab_min, crab_max):
	fuel = 0
	for crab in crabs:
		fuel += abs(crab - n)
		if fuel > fuel_min:
			break
	fuel_min = fuel if fuel < fuel_min else fuel_min

print(f'Part1 : {fuel_min}')

fuel_min = sys.maxsize
fuel = 0
for n in range(crab_min, crab_max):
	fuel = 0
	for crab in crabs:
		diff = abs(crab - n)
		fuel +=  diff * (diff - 1) // 2
		if fuel > fuel_min:
			break
	fuel = fuel if fuel < fuel_min else fuel_min
	
print(f'Part2 : {fuel_min}')
