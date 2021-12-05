
import numpy as np
from parse import parse

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
    print('Part 1:')
    print(np.sum(map > 1))

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
            while(x1 != x2):
                map[x1, y1] += 1
                if(x2 > x1):
                    x1 += 1
                else:
                    x1 -= 1
                if(y2 > y1):
                    y1 +=1
                else:
                    y1 -= 1
            map[x2, y2] += 1
    print('Part 2:')
    print(np.sum(map > 1))



