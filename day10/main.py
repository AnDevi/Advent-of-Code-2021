#!/usr/bin/python3

from pathlib import Path
from collections import deque

pairs = { '(' : ')', '[' : ']', '{' : '}', '<' : '>' }
part1_scores = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137 }
part2_scores = { ')' : 1, ']' : 2, '}' : 3, '>' : 4 }

class Parser():
	def __init__(self, data):
		self.data = data
		self.q = deque()
		self.idx = 0
		self.score_part1 = 0
		self.score_part2 = 0
		self.incorrect_sign = None
		self.unfinished = False
		
	def get_sign(self):
		self.idx += 1
		return self.data[self.idx - 1]

	def get_part1_score(self):
		if not self.unfinished and self.incorrect_sign is not None:
			return part1_scores[self.incorrect_sign]
		else: 
			return 0

	def get_part2_score(self):
		score = 0
		while self.q:
			score = 5 * score + part2_scores[pairs[self.q.pop()]]
		return score

	def check(self):
		if self.idx >= len(self.data):
			self.unfinished = True
			return

		curr_sign = self.get_sign()
		if curr_sign == '[' or curr_sign == '<' or curr_sign == '(' or curr_sign == '{':
			self.q.append(curr_sign)
			self.check()
		else:
			if curr_sign == pairs[self.q.pop()]:
				if self.q and self.idx:
					self.check()
			else:
				self.incorrect_sign = curr_sign

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day10/day10.txt'), "r")
lines = [line.strip() for line in file.readlines()]
file.close()

part1 = 0
part2 = []
for line in lines:
	parser = Parser(line)
	parser.check()
	part1 += parser.get_part1_score()
	if parser.unfinished:
		part2.append(parser.get_part2_score())

part2.sort()
print(f'Part1 : {part1}')
print(f'Part2 : {part2[int(len(part2) / 2)]}')
