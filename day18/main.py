#!/usr/bin/python3

from pathlib import Path
import re
import copy

class SnailfishNumber():
	def __init__(self, data):
		self.raw_data = data
		self.data = self.parse(data)
	
	def parse(self, data):
		signs = re.findall('\[|\]|\d+', data)
		return [int(c) if '0' <= c <= '9' else c for c in signs]

	def add(self, number):
		self.data = ['['] + self.data + number.data + [']']
		return self.reduct()

	def reduct(self):
		while self.explode() or self.split():
			pass
		return self

	def explode(self):
		nested = 0
		for idx in range(len(self.data) - 4):
			if nested >= 4 and self.data[idx] == '[' and self.data[idx+3] == ']':
				left_idx, right_idx = idx, idx+3 
				while left_idx != 0 and not isinstance(self.data[left_idx], int):
					left_idx -= 1
				while right_idx != len(self.data) and not isinstance(self.data[right_idx], int):
					right_idx += 1

				if left_idx != 0:
					self.data[left_idx] += self.data[idx+1]
				if right_idx != len(self.data):
					self.data[right_idx] += self.data[idx+2]
				self.data = self.data[:idx] + [0] + self.data[idx+4:]				
				return True

			elif self.data[idx] == '[':
				nested += 1
			elif self.data[idx] == ']':
				nested -= 1
		return False
	
	def split(self):
		for idx, d in enumerate(self.data):
			if isinstance(d, int) and d > 9:
				divided, mod = d // 2, d % 2
				left_right = (divided, divided)if not mod else (divided, divided + 1)
				self.data = self.data[:idx] + ['[', left_right[0], left_right[1], ']'] + self.data[idx+1:]
				return True
		return False

	def magnitude(self):
		magnitude_data = copy.deepcopy(self.data)
		while len(magnitude_data) > 3:
			for idx in range(len(self.data)):
				if isinstance(magnitude_data[idx], int) and isinstance(magnitude_data[idx+1], int):
					if magnitude_data[idx-1] == '[' and magnitude_data[idx+2] == ']':
						number = 3*magnitude_data[idx]+2*magnitude_data[idx+1]
						magnitude_data = magnitude_data[:idx-1] + [number] + magnitude_data[idx+3:]
						break

		return magnitude_data[0]

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day18/day18.txt'), "r")
numbers = [SnailfishNumber(str(line.strip())) for line in file.readlines()]

all_numbers = copy.deepcopy(numbers)
final_number = numbers[0]
numbers = numbers[1:]
for number in numbers:
	final_number = final_number.add(number)
part1 = final_number.magnitude()
print(f'Part 1: {part1}')

part2 = 0
for n1 in all_numbers:
	for n2 in all_numbers:
		if(n1.raw_data != n2.raw_data):
			left, right = copy.deepcopy(n1), copy.deepcopy(n2)
			left.add(right)
			part2 = max(part2, left.magnitude())

print(f'Part 2: {part2}')
