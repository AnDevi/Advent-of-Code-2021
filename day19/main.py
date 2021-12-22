#!/usr/bin/python3

from pathlib import Path
import itertools

rotations = list(itertools.product((1,-1),(1,-1),(1,-1)))
coords = list(itertools.permutations([0, 1, 2]))
orientations = [rot + coord for coord in coords for rot in rotations]

class Scanner():
	def __init__(self, beacons, id): 
		self.id = id
		self.beacons = beacons
		self.pos = None

	@staticmethod
	def subtract(b1, b2):
		return (b1[0]-b2[0],b1[1]-b2[1],b1[2]-b2[2])
	@staticmethod
	def add(b1, b2):
		return (b1[0]+b2[0],b1[1]+b2[1],b1[2]+b2[2])
	@staticmethod
	def get_inner_scanner_diffs(beacons):
		diffs_dict = dict()
		for b1 in beacons:
			diffs_dict[b1] = {Scanner.subtract(b1, b2) for b2 in beacons}
		return diffs_dict

	def manhatan_dist(self, pos):
		return abs(self.pos[0]-pos[0])+abs(self.pos[1]-pos[1])+abs(self.pos[2]-pos[2])

	def rotate(self, a, b, c, i, j, k):
		return[(a * beacon[i], b * beacon[j], c * beacon[k]) for beacon in self.beacons]

	def find_position(self, pos_scanners):
		for scanner in pos_scanners:
			scanner_diffs = Scanner.get_inner_scanner_diffs(scanner.beacons)
			for o in orientations:
				rotated_beacons = self.rotate(*o)
				rotated_diffs = Scanner.get_inner_scanner_diffs(rotated_beacons)

				for scanner_beacon in scanner.beacons:
					for rotated_beacon in rotated_beacons:
						if len(scanner_diffs[scanner_beacon] & rotated_diffs[rotated_beacon]) >= 12:
							diff = Scanner.subtract(scanner_beacon, rotated_beacon)
							self.pos = diff
							self.beacons = [Scanner.add(b, diff) for b in rotated_beacons]
							return True
		return False


file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day19/day19.txt'), "r")
scanners_data = file.read().split('\n\n')
scanners = []
positioned_scanners = []
for data in scanners_data:
	beacons = []
	for x,y,z in [points.split(',') for points in data.split('\n') if 'scanner' not in points]:
		beacons.append((int(x),int(y),int(z)))
	scanners.append(Scanner(beacons, len(scanners)))

file.close()
scanners[0].pos = (0,0,0)
positioned_scanners.append(scanners[0])
scanners = scanners[1:]

while len(scanners):
	for idx, scanner in enumerate(scanners):
		if scanner.find_position(positioned_scanners):
			positioned_scanners.append(scanner)
			scanners = scanners[:idx] + scanners[idx+1:]
			break

all_beacons = set()
for scanner in positioned_scanners:
	for b in scanner.beacons:
		all_beacons.add(b)

part1 = len(all_beacons)
print(f'Part 1: {part1}')

part2 = 0
for s1 in positioned_scanners:
	for s2 in positioned_scanners:
		if s1.pos != s2.pos:
			part2 = max(part2, s1.manhatan_dist(s2.pos))

print(f'Part 2: {part2}')
