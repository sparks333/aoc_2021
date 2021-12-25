import random
import numpy as np
import copy

def check_num(model_num, program):
    reg = {'w':int(0), 'x':int(0), 'y':int(0), 'z':int(0)}
    inp_indx = 0

    w_intermediate = []
    x_intermediate = []
    y_intermediate = []
    z_intermediate = []

    for coms in program:
        if coms[0] == 'inp':
            if inp_indx > 0:
                w_intermediate.append(reg['w'])
                x_intermediate.append(reg['x'])
                y_intermediate.append(reg['y'])
                z_intermediate.append(reg['z'])
            reg[coms[1]] = model_num[inp_indx]
            inp_indx += 1
        elif coms[0] == 'add':
            if coms[2].isalpha():
                operand = reg[coms[2]]
            else:
                operand = int(coms[2])
            reg[coms[1]] = reg[coms[1]] + operand
        elif coms[0] == 'mul':
            if coms[2].isalpha():
                operand = reg[coms[2]]
            else:
                operand = int(coms[2])
            reg[coms[1]] = reg[coms[1]] * operand
        elif coms[0] == 'div':
            if coms[2].isalpha():
                operand = reg[coms[1]]
            else:
                operand = int(coms[2])
            if operand == 0:
                return False
            reg[coms[1]] = int(reg[coms[1]] / operand)
        elif coms[0] == 'mod':
            if coms[2].isalpha():
                operand = reg[coms[2]]
            else:
                operand = int(coms[2])
            if reg[coms[1]] <0 or operand <= 0:
                return False
            reg[coms[1]] = reg[coms[1]] % operand
        elif coms[0] == 'eql':
            if coms[2].isalpha():
                operand = reg[coms[2]]
            else:
                operand = int(coms[2])
            if reg[coms[1]] == operand:
                reg[coms[1]] = 1
            else:
                reg[coms[1]] = 0
    w_intermediate.append(reg['w'])
    x_intermediate.append(reg['x'])
    y_intermediate.append(reg['y'])
    z_intermediate.append(reg['z'])

    return reg['z']

#model_num[0] = random.randrange(1,10) #13
#model_num[1] = random.randrange(1,10) #12
#model_num[2] = 0 #11
#model_num[3] = 9 #10
#model_num[4] = 1 #9
#model_num[5] = 0 #8
#model_num[6] = random.randrange(9,10) #7
#model_num[7] = model_num[6] - 6 #6
#model_num[8] = random.randrange(1,7) #5
#model_num[9] = model_num[8] + 3 #4
#model_num[10] = 0 #3
#model_num[11] = 0 #2
#model_num[12] = random.randrange(1,8) #1
#model_num[13] = model_num[12] + 2 #0

A = [15, 11, 10, 12, -11, 11, 14, -6, 10, -6, -6, -16, -4, -2]
B = [1, 1, 1, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26, 26]
C = [9, 1, 11, 3, 10, 5, 0, 7, 9, 15, 4, 10, 4, 9]

max_z = [8031810176, 8031810176, 8031810176, 8031810176, \
         8031810176, 308915776, 308915776, 308915776, \
         11881376, 11881376, 456976, 17576, 676, 26]

def stage(n, w, z):
    if (z % 26 + A[n]) == w:
        return np.fix(z / B[n])
    else:
        return 26 * np.fix(z / B[n]) + w + C[n]

def search(depth, z, solution):

    if depth == 14:
        if z == 0:
            print(solution)
        return
    elif z >= max_z[depth]:
        return

    for i in range(9, 0, -1):
        new_solution = copy.deepcopy(solution)
        new_solution[depth] = i
        search(depth + 1, stage(depth, i, z), new_solution)

model_num = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
search(0, 0, model_num)