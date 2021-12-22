#!/usr/bin/python3

from pathlib import Path
from collections import Counter
import copy

DAYS = 256
file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day6/day6.txt'), "r")
fish_list = [int(numeric_string) for numeric_string in file.readline().split(",")]
file.close()
fishes = Counter(fish_list)
fishes_tmp = Counter()

for day in range(0, DAYS):
	if fishes[0] > 0:
		fishes_tmp[6] = fishes[0]
		fishes_tmp[8] = fishes[0]
		fishes_tmp[0] = 0
	for val, cnt in fishes.items():
		if val != 0:
			fishes_tmp[val - 1] += fishes[val]			 
		
	fishes  = copy.deepcopy(fishes_tmp)
	fishes_tmp = Counter()

count = 0
for idx, val in enumerate(fishes):
	if idx <= 8:
		count += fishes[idx]

print(f'Part2 : {count}')
