
import numpy as np

input = np.loadtxt('input.txt')

greater = input[1:] > input[0:-1]

print("Part 1:")
print(greater.sum())

conv = np.convolve(input, np.array([1, 1, 1]), 'valid')

greater = conv[1:] > conv[0:-1]

print("Part 2:")
print(greater.sum())