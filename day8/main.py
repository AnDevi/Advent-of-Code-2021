#!/usr/bin/python3

from pathlib import Path

def contais(code, number):
	if len(code) != len(number):
		return False
	for c in code:
		if (c not in number):
			return False
	return True

def count(code, number):
	cnt = 0
	for c in code:
		cnt += 1 if c in number else 0
	return cnt

def find_digit(code, num, founded):
	if num == 1 and len(code) == 2:
		founded[num] = code
	elif num == 4 and len(code) == 4:
		founded[num] = code
	elif num == 7 and len(code) == 3:
		founded[num] = code
	elif num == 8 and len(code) == 7:
		founded[num] = code
	elif num == 3 and len(code) == 5 and count(code, founded[7]) == 3:
		founded[num] = code
	elif num == 9 and len(code) == 6 and count(code, founded[4]) == 4:
		founded[num] = code
	elif num == 0 and len(code) == 6 and count(code, founded[1]) == 2 and not contais(code, founded[9]):
		founded[num] = code
	elif num == 6 and len(code) == 6 and not contais(code, founded[9]) and not contais(code, founded[0]):
		founded[num] = code
	elif num == 5 and len(code) == 5 and count(code, founded[6]) == 5:
		founded[num] = code
	elif num == 2 and len(code) == 5 and not contais(code, founded[3]) and not contais(code, founded[5]):
		founded[num] = code
		
def find_number(codes, nums):
	order = [1, 4, 7, 8, 3, 9, 0, 6, 5, 2]
	founded = dict()
	for x, code in [(x, code) for x in order for code in codes]:
		find_digit(code, x, founded)

	number = ""
	for num, digit, code in [(num, digit, code) for num in nums	for digit, code in founded.items()]:
		if contais(num, code):
			number += str(digit)
	return int(number)

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day8/day8.txt'), "r")
part1 = 0
part2 = 0
disired = [2, 3, 4, 7]
for line in file:
	codes, numbers = line.split(' | ')
	codes = codes.split()
	numbers = numbers.split()

	lens = [len(n) for n in numbers]
	for d in disired:
		part1 += lens.count(d)

	part2 += find_number(codes, numbers)

file.close()
print(f'Part1 : {part1}')
print(f'Part2 : {part2}')
