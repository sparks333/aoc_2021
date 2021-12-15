
from os import pathsep
import numpy as np
import heapq

#hazard = np.genfromtxt('input.txt', delimiter=1, dtype=int)
#dist = np.zeros_like(hazard)
#for y in range(dist.shape[0]):
#    for x in range(dist.shape[1]):
#        dist[y, x] = x + y
#dist = np.flip(dist)

#hazard + dist

#paths = []
#heapq.heappush(paths, (dist[0,0], 0, [[0, 0]]))

#visited = np.zeros_like(hazard)

#while(True):
#    best_path = heapq.heappop(paths)
#    g = best_path[1]
#    history = best_path[2]
#    x = history[-1][1]
#    y = history[-1][0]
#    visited[y, x] = 1

#    if(y == hazard.shape[0]-1 and x == hazard.shape[1]-1):
#        print('Part 1: ' + str(g))
#        break

#    if x-1 >= 0 and visited[y, x-1] == 0:
#        f = g + hazard[y, x-1] + dist[y, x-1]
#        heapq.heappush(paths, (f, g + hazard[y, x-1], history + [[y, x-1]]))
#    if x+1 < hazard.shape[1] and visited[y, x+1] == 0:
#        f = g + hazard[y, x+1] + dist[y, x+1]
#        heapq.heappush(paths, (f, g + hazard[y, x+1], history + [[y, x+1]]))
#    if y-1 >= 0 and visited[y-1, x] == 0:
#        f = g + hazard[y-1, x] + dist[y-1, x]
#        heapq.heappush(paths, (f, g + hazard[y-1, x], history + [[y-1, x]]))
#    if y+1 < hazard.shape[0] and visited[y+1, x] == 0:
#        f = g + hazard[y+1, x] + dist[y+1, x]
#        heapq.heappush(paths, (f, g + hazard[y+1, x], history + [[y+1, x]]))

small_hazard = np.genfromtxt('input.txt', delimiter=1, dtype=int)

hazard = np.zeros([small_hazard.shape[0]*5, small_hazard.shape[1]*5])
for i in range(5):
    for j in range(5):
        hazard[i*small_hazard.shape[0]:(i+1)*small_hazard.shape[0], j*small_hazard.shape[1]:(j+1)*small_hazard.shape[1]] = np.mod(small_hazard + i + j - 1, 9) + 1

dist = np.zeros_like(hazard)
for y in range(dist.shape[0]):
    for x in range(dist.shape[1]):
        dist[y, x] = x + y
dist = np.flip(dist)

paths = []
heapq.heappush(paths, (dist[0,0], 0, [0, 0]))

visited = np.zeros_like(hazard)

while(True):
    best_path = heapq.heappop(paths)
    g = best_path[1]
    coords = best_path[2]
    x = coords[1]
    y = coords[0]
    visited[y, x] = 1

    if(y == hazard.shape[0]-1 and x == hazard.shape[1]-1):
        print('Part 2: ' + str(g))
        break

    if x-1 >= 0 and visited[y, x-1] == 0:
        f = g + hazard[y, x-1] + dist[y, x-1]
        new_key = (f, g + hazard[y, x-1], [y, x-1])
        if new_key not in paths:
            heapq.heappush(paths, new_key)
    if x+1 < hazard.shape[1] and visited[y, x+1] == 0:
        f = g + hazard[y, x+1] + dist[y, x+1]
        new_key = (f, g + hazard[y, x+1], [y, x+1])
        if new_key not in paths:
            heapq.heappush(paths, new_key)
    if y-1 >= 0 and visited[y-1, x] == 0:
        f = g + hazard[y-1, x] + dist[y-1, x]
        new_key = (f, g + hazard[y-1, x], [y-1, x])
        if new_key not in paths:
            heapq.heappush(paths, new_key)
    if y+1 < hazard.shape[0] and visited[y+1, x] == 0:
        f = g + hazard[y+1, x] + dist[y+1, x]
        new_key = (f, g + hazard[y+1, x], [y+1, x])
        if new_key not in paths:
            heapq.heappush(paths, new_key)