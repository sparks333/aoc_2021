from os import linesep
import numpy as np

board_data = np.loadtxt('input.txt', skiprows=1, dtype='int32')
taken_data = np.zeros_like(board_data)

with open('input.txt') as file:

    call_string = file.readline()
    call_nums =[int(i) for i in call_string.split(',')]

n_boards = int(board_data.shape[0]/5)

for i in call_nums:
    taken_data[board_data == i] = 1
    for j in range(n_boards):
        for k in range(5):
            if(taken_data[(j*5):(j*5)+5, k].sum() == 5):
                winning_board_num = j
                final_number = i
                break
            if(taken_data[(j*5)+k, :].sum() == 5):
                winning_board_num = j
                final_number = i
                break
        else:
            continue
        break
    else:
        continue
    break

print('Part 1:')

winning_board = board_data[5*winning_board_num : 5*winning_board_num + 5, :]
winning_taken = taken_data[5*winning_board_num : 5*winning_board_num + 5, :]

unmarked = winning_board[winning_taken == 0]

print(str(unmarked.sum() * final_number))

num_wins = 0
winning_boards = []


for i in call_nums:
    taken_data[board_data == i] = 1
    for j in range(n_boards):
        if len(winning_boards) == n_boards:
            break
        if (not j in winning_boards):
            for k in range(5):
                if(taken_data[(j*5):(j*5)+5, k].sum() == 5):
                    winning_boards.append(j)
                    last_board = board_data[5*j : 5*j + 5, :]
                    last_taken = taken_data[5*j : 5*j + 5, :]
                    last_number = i
                    break
                elif(taken_data[(j*5)+k, :].sum() == 5):
                    winning_boards.append(j)
                    last_board = board_data[5*j : 5*j + 5, :]
                    last_taken = taken_data[5*j : 5*j + 5, :]
                    last_number = i
                    break
    else:
        continue
    break


unmarked = last_board[last_taken == 0]
print('Part 2:')
print(str(unmarked.sum() * last_number))