#!/usr/bin/python3

import functools

players = [4, 8]
scores = [0, 0]
rolled_times = 0
curr_dice = 0
end = False

def roll_dice():
    global curr_dice
    global rolled_times
    rolled_times += 1
    curr_dice = curr_dice % 100 + 1
    return curr_dice 

while not end:
    for idx in range(2):
        dice_rolls = 0
        for _ in range(3):
            dice_rolls += roll_dice()
        players[idx] = (players[idx] + dice_rolls - 1) % 10 + 1
        scores[idx] += players[idx]
        if scores[idx] >= 1000:   
            end = True

part1 = rolled_times * min(scores)
print(f'Part 1: {part1}') 

players = [1, 2]
scores = [0, 0]

@functools.lru_cache(maxsize=None)
def roll(round, p0, p1, score0, score1):
    players = [p0, p1]
    scores = [score0, score1]
    curr_player = round % 2
    if scores[0] >= 21:
        return [1, 0]
    elif scores[1] >= 21:
        return [0, 1]
    answer = [0, 0]
    for r1 in [1,2,3]:
        for r2 in [1,2,3]:
            for r3 in [1,2,3]:
                players[curr_player] = (players[curr_player]+r1+r2+r3-1) %10 + 1
                scores[curr_player] += players[curr_player]
                new_answer = roll(round + 1, players[0], players[1], scores[0], scores[1])
                answer[0] += new_answer[0]
                answer[1] += new_answer[1]
                players[0], players[1] = p0, p1
                scores[0], scores[1] = score0, score1

    return answer

part2 = max(roll(0, players[0], players[1], scores[0], scores[1]))
print(f'Part 2: {part2}')
