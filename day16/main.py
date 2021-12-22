#!/usr/bin/python3

from pathlib import Path
import numpy

class Parser():
	def __init__(self, hex_data):
		self.data = bin(int(hex_data, 16))[2:].zfill(4 * len(hex_data))
		self.versions = []
		self.idx = 0

	def read_data_chunk(self, n):
		self.idx += n
		return int(self.data[self.idx-n:self.idx], 2)

	def read_package(self):
		
		self.versions.append(self.read_data_chunk(3))
		id = self.read_data_chunk(3)
		if id == 4:
			return self.read_literal()
		else:
			return self.read_operator(id)

	def count_values(self, id, values):
		if id == 0:
			return sum(values)
		elif id == 1:
			return numpy.product(values)
		elif id == 2:
			return min(values)
		elif id == 3:
			return max(values)
		elif id == 5:
			return 1 if values[0] > values[1] else 0
		elif id == 6:
			return 1 if values[0] < values[1] else 0
		elif id == 7:
			return 1 if values[0] == values[1] else 0		

	def read_literal(self):
		bit = 1
		number = ""
		while bit != 0:
			bit = self.read_data_chunk(1)
			number +=  str(self.data[self.idx:self.idx+4])
			self.idx += 4
			
		return int(number, 2)

	def read_operator(self, id):
		subpackage_values = []
		num = self.read_data_chunk(1)
		if num == 0:
			length = self.read_data_chunk(15)
			total_length = self.idx + length
			while self.idx < total_length:
				subpackage_values.append(self.read_package())
		elif num == 1:
			packages = self.read_data_chunk(11)
			for _ in range(packages):
				subpackage_values.append(self.read_package())
		
		return self.count_values(id, subpackage_values)

	def get_versions(self):
		return sum(self.versions)

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day16/day16.txt'), "r")
parser = Parser(file.readline().strip())
file.close()

part2 = parser.read_package()
part1 = parser.get_versions()

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
