import itertools
import numpy as np

player1_score = 0
player2_score = 0

player1_pos = 4-1
player2_pos = 8-1

dice_rolls = 0

player1_turn = True

while player1_score < 1000 and player2_score < 1000:

    if player1_turn:
        player1_pos = (player1_pos + (dice_rolls+1) + (dice_rolls+2) + (dice_rolls+3)) % 10
        player1_score += (player1_pos+1)
        player1_turn = False

    else:
        player2_pos = (player2_pos + (dice_rolls+1) + (dice_rolls+2) + (dice_rolls+3)) % 10
        player2_score += (player2_pos+1)
        player1_turn = True

    dice_rolls += 3

if(player1_score >= 1000):
    print('Part 1: ' + str(player2_score * dice_rolls))
else:
    print('Part 1: ' + str(player1_score * dice_rolls))
    
def n_turns(pos, score, turn):

    dice = [[3, 1], [4, 3], [5, 6], [6, 7], [7, 6], [8, 3], [9, 1]]

    if score >= 21:
        ret_array = np.zeros(15, dtype='int64')
        ret_array[turn] = 1
        return ret_array
    else:
        ret_array = np.zeros(15, dtype='int64')
        for i in dice:
            tmp_pos = (pos + i[0]) % 10
            tmp_score = score + tmp_pos + 1
            ret_array += i[1] * n_turns(tmp_pos, tmp_score, turn+1)
    return ret_array


p1_comb = n_turns(10-1, 0, 0)
p2_comb = n_turns(4-1, 0, 0)

p1_wins = 0
p2_wins = 0

p1_not_comb = np.zeros_like(p1_comb)
p2_not_comb = np.zeros_like(p2_comb)

p1_not_comb[0] = 1
p2_not_comb[0] = 1

for i in range(1, len(p1_not_comb)):
    p1_not_comb[i] = 27*p1_not_comb[i-1] - p1_comb[i]
    p2_not_comb[i] = 27*p2_not_comb[i-1] - p2_comb[i]

for i in range(1, len(p1_comb)):
    p1_wins += (p1_comb[i]*p2_not_comb[i-1])
    p2_wins += (p2_comb[i]*p1_not_comb[i])

print('Part 2: ' + str(max(p1_wins, p2_wins)))