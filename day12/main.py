#!/usr/bin/python3

from pathlib import Path
from collections import defaultdict

def count_paths(caves, start, visited, lower_twice=False):
    if start == "end":
        return 1
    res = 0
    for next_cave in caves[start]:
        if next_cave not in visited:        
            tmp = {next_cave} if next_cave == next_cave.lower() else set()
            res += count_paths(caves, next_cave, visited | tmp, lower_twice)
        elif lower_twice and next_cave != 'start':
            res += count_paths(caves, next_cave, visited)

    return res

caves = defaultdict(set)
file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day12/day12.txt'), "r")
for line in [line.strip() for line in file.readlines()]:
    start, end = line.split('-')
    caves[start].add(end)
    caves[end].add(start)
file.close()

part1 = count_paths(caves, 'start', {'start'})
print(f'Part1 : {part1}')
part2 = count_paths(caves, 'start', {'start'}, True)
print(f'Part2 : {part2}')
