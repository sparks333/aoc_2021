
import numpy as np

pos = np.loadtxt('input.txt',delimiter=',')

ideal_pos = np.median(pos)

total_fuel = np.sum(np.abs(pos - ideal_pos))

print('Part 1: ' + str(total_fuel))

pos = np.loadtxt('input.txt',delimiter=',')

ideal_pos = np.floor(np.mean(pos))

dist = np.abs(pos - ideal_pos)

total_fuel = np.sum((dist/2)*(dist+1))

print('Part 2: ' + str(total_fuel))
