
import numpy as np
import time
from parse import parse

t_start = time.time()
map = np.zeros([1000, 1000])
with open('input.txt') as file:
    for line in file:
        extracted_vals = parse('{},{}->{},{}', line)
        x1 = int(extracted_vals[0])
        y1 = int(extracted_vals[1])
        x2 = int(extracted_vals[2])
        y2 = int(extracted_vals[3])

        if(x1 == x2):
            map[x1, min(y1, y2):max(y1, y2)+1] += 1
        elif(y1 == y2):
            map[min(x1, x2):max(x1, x2)+1, y1] += 1
    t_end = time.time()
    print('Part 1: ' + str(np.sum(map > 1)) + ', Elapsed Time: ' + str(t_end-t_start))

t_start = time.time()
map = np.zeros([1000, 1000])
with open('input.txt') as file:
    for line in file:
        extracted_vals = parse('{},{}->{},{}', line)
        x1 = int(extracted_vals[0])
        y1 = int(extracted_vals[1])
        x2 = int(extracted_vals[2])
        y2 = int(extracted_vals[3])

        if(x1 == x2):
            map[x1, min(y1, y2):max(y1, y2)+1] += 1
        elif(y1 == y2):
            map[min(x1, x2):max(x1, x2)+1, y1] += 1
        else:
            diag_x = np.arange(x1, x2) if x2 > x1 else np.arange(x1, x2, -1)
            diag_y = np.arange(y1, y2) if y2 > y1 else np.arange(y1, y2, -1)
            map[diag_x, diag_y] += 1
            map[x2, y2] += 1
    t_end = time.time()
    print('Part 2: ' + str(np.sum(map > 1)) + ', Elapsed Time: ' + str(t_end-t_start))



