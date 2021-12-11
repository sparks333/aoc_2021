import numpy as np

octo = np.genfromtxt('input.txt', delimiter=1, dtype=int)

n_steps = 100

flashes = 0

for i in range(n_steps):
    octo += 1
    flashing = octo > 9
    flashed = np.zeros([10, 10])
    while np.sum(flashing) != 0:
        flashes += np.sum(flashing)
        np.logical_or(flashed, flashing, flashed)
        flash_matrix = np.zeros([12, 12], dtype='int32')
        flash_matrix[0:10, 0:10] += flashing
        flash_matrix[1:11, 0:10] += flashing
        flash_matrix[2:12, 0:10] += flashing
        flash_matrix[0:10, 1:11] += flashing
        flash_matrix[2:12, 1:11] += flashing
        flash_matrix[0:10, 2:12] += flashing
        flash_matrix[1:11, 2:12] += flashing
        flash_matrix[2:12, 2:12] += flashing
        octo += flash_matrix[1:11,1:11]
        octo[flashed == 1] = 0
        flashing = octo > 9

print('Part 1: ' + str(flashes))

octo = np.genfromtxt('input.txt', delimiter=1, dtype=int)

all_flash = 0
steps = 0

while all_flash == 0:
    octo += 1
    flashing = octo > 9
    flashed = np.zeros([10, 10])
    while np.sum(flashing) != 0:
        flashes += np.sum(flashing)
        np.logical_or(flashed, flashing, flashed)
        flash_matrix = np.zeros([12, 12], dtype='int32')
        flash_matrix[0:10, 0:10] += flashing
        flash_matrix[1:11, 0:10] += flashing
        flash_matrix[2:12, 0:10] += flashing
        flash_matrix[0:10, 1:11] += flashing
        flash_matrix[2:12, 1:11] += flashing
        flash_matrix[0:10, 2:12] += flashing
        flash_matrix[1:11, 2:12] += flashing
        flash_matrix[2:12, 2:12] += flashing
        octo += flash_matrix[1:11,1:11]
        octo[flashed == 1] = 0
        flashing = octo > 9
    all_flash = np.sum(flashed) == 100
    steps += 1

print('Part 2: ' + str(steps))



