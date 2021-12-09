import numpy as np

m = np.genfromtxt('input.txt', delimiter=1, dtype=int)

m_pad = np.pad(m, 1, mode='constant', constant_values=9)

hazard = 0

for i in range(1, m_pad.shape[0]-1):
    for j in range(1, m_pad.shape[1]-1):
        c = m_pad[i][j]
        u = m_pad[i-1][j]
        d = m_pad[i+1][j]
        l = m_pad[i][j-1]
        r = m_pad[i][j+1]

        if c < u and c < d and c < l and c < r:
            hazard += c+1

print("Part 1: " + str(hazard))

def basin_finder(m_pad, counted, i, j):
    if i < 0 or i >= m_pad.shape[0] or j < 0 or j >= m_pad.shape[1]:
        return counted

    if m_pad[i][j] != 9:
        counted[i][j] = 1
        if counted[i][j-1] == 0:
            counted |= basin_finder(m_pad, counted, i, j-1)
        if counted[i][j+1] == 0:
            counted |= basin_finder(m_pad, counted, i, j+1)
        if counted[i-1][j] == 0:
            counted |= basin_finder(m_pad, counted, i-1, j)
        if counted[i+1][j] == 0:
            counted |= basin_finder(m_pad, counted, i+1, j)

    return np.array(counted)

m = np.genfromtxt('input.txt', delimiter=1, dtype=int)
m_pad = np.pad(m, 1, mode='constant', constant_values=9)
basins = []

for i in range(1, m_pad.shape[0]-1):
    for j in range(1, m_pad.shape[1]-1):
        c = m_pad[i][j]
        u = m_pad[i-1][j]
        d = m_pad[i+1][j]
        l = m_pad[i][j-1]
        r = m_pad[i][j+1]

        if c < u and c < d and c < l and c < r:
            counted = basin_finder(m_pad, np.zeros_like(m_pad), i, j)
            basins.append(np.sum(counted))

basins.sort()
print("Part 2: " + str(basins[-1] * basins[-2] * basins[-3]))