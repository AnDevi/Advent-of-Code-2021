#!/usr/bin/python3

from pathlib import Path
import copy

SIZE = 5

def grid_print(grid):
	w, h = len(grid[0]), len(grid)
	for y in range(h):
		print(''.join([str(grid[y][x]) for x in range(w)]))
	print()

def print_boards(grids):
    for num in range(0, len(grids)):
        print(f'BOARD {num}')
        grid_print(grids[num])
        print()

def count(grid):
    res = 0
    for sign in [grid[i][j] for j in range(SIZE) for i in range(SIZE)]:
        res += int(sign) if sign != 'X' else 0
    return res

def cross_number(boards, num):
    for board in boards:
        for i, j in [(j,i)  for j in range(SIZE) for i in range(SIZE)]:
            if board[i][j] == num:
                board[i][j] = 'X'

def did_add(winners, number):
    prevSize = len(winners)
    winners.add(number)
    return True if prevSize != len(winners) else False

def is_bingo(boards, new_winners):
    last_winner = 0
    for board_idx in range(0, len(boards)):
        curr_board = boards[board_idx]
        #check rows
        for y in range(0, SIZE):
            if curr_board[y][0] == 'X' and curr_board[y][1] == 'X'  and curr_board[y][2] == 'X'  and curr_board[y][3] == 'X'  and curr_board[y][4] == 'X':
                if did_add(new_winners, board_idx):
                    last_winner = board_idx
        #check cols
        for x in range(0, SIZE):
            if curr_board[0][x] == 'X' and curr_board[1][x] == 'X'  and curr_board[2][x] == 'X'  and curr_board[3][x] == 'X'  and curr_board[4][x] == 'X':
                if did_add(new_winners, board_idx):
                    last_winner = board_idx
    return last_winner

file = open(str(Path(Path.home()) / 'Documents/private/adventcode2021/python/day4/day4.txt'), "r")

numbers = [int(numeric_string) for numeric_string in file.readline().split(',')]
file.readline()
boards_string = file.read().split('\n\n')
boards = []
for board_string in boards_string:
    print(board_string)
    board = [[int(n) for n in line.split()] for line in board_string.splitlines()] 
    boards.append(board)
    
file.close()

grid_print(boards)

boards_part1 = copy.deepcopy(boards)
winning_board_idx, winning_number = 0, 0
winning_boards_set = set()

for n in numbers:
    cross_number(boards_part1, n)

    prevSize = len(winning_boards_set)
    winning_board_idx = is_bingo(boards_part1, winning_boards_set)
    if prevSize != len(winning_boards_set):
        winning_number = n
        break

print_boards(boards_part1)
board_sum = count(boards_part1[winning_board_idx])

print(f'Part1 : {board_sum * winning_number}')

boards_part2 = copy.deepcopy(boards)
last_winning_board_idx, winning_number = 0, 0
winning_boards_set = set()

for n in numbers:

    cross_number(boards_part2, n)
    prevSize = len(winning_boards_set)
    last_winning_board_idx = is_bingo(boards_part2, winning_boards_set)

    if len(winning_boards_set) == len(boards):
        winning_number = n
        break
    
board_sum = count(boards_part2[last_winning_board_idx])
print(f'Part2 : {board_sum * winning_number}')
