#!/usr/bin/python3

from collections import Counter
from pathlib import Path

STEPS_PART1 = 10
STEPS_PART2 = 40

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day14/day14.txt'), "r")
code, keys_string = file.read().split('\n\n')
file.close()

code = code.strip()

dictionary = {}
for key, value in [line.split(' -> ') for line in keys_string.splitlines()]:
    dictionary[key] = [key[0] + value, value + key[1]]

counter_pairs = Counter()
for first, second in zip(code, code[1:]):
    pair = first + second
    counter_pairs[pair] +=1

counter_signs = Counter(code)

for s in range(STEPS_PART2):
    if s == STEPS_PART1:
        mostCommon = counter_signs.most_common()
        print(f'Part1: {mostCommon[0][1] - mostCommon[-1][1]}')
        
    tmp = Counter()
    for pair, count in counter_pairs.items():
        if pair in dictionary:
            added_sign = dictionary[pair][0][1]
            counter_signs[added_sign] += count
            for new_pair in dictionary[pair]:
                tmp[new_pair] += count
    counter_pairs = tmp

mostCommon = counter_signs.most_common()
print(f'Part2: {mostCommon[0][1] - mostCommon[-1][1]}')