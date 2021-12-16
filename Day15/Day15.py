
from os import pathsep
import numpy as np
import heapq

def pathfind(hazmap, goal):
    paths = []
    y_goal = goal[0]
    x_goal = goal[1]
    heapq.heappush(paths, ((y_goal + x_goal), 0, [0, 0]))
    visited = 10*(x_goal + y_goal) * np.ones_like(hazmap)
    visited[0, 0] = 0

    while(True):
        best_path = heapq.heappop(paths)
        g = best_path[1]
        x_y = best_path[2]
        x = x_y[1]
        y = x_y[0]

        if(y == y_goal and x == x_goal):
            return(g)

        if x-1 >= 0:
            f = g + hazmap[y, x-1] + abs((y - y_goal) + ((x-1)-x_goal))
            if visited[y, x-1] > f:
                heapq.heappush(paths, (f, g + hazmap[y, x-1], [y, x-1]))
                visited[y, x-1] = f

        if x+1 < hazmap.shape[1]:
            f = g + hazmap[y, x+1] + abs((y - y_goal) + ((x+1)-x_goal))
            if visited[y, x+1] > f:
                heapq.heappush(paths, (f, g + hazmap[y, x+1], [y, x+1]))
                visited[y, x+1] = f

        if y-1 >= 0:
            f = g + hazmap[y-1, x] + abs(((y-1) - y_goal) + (x-x_goal))
            if visited[y-1, x] > f:
                heapq.heappush(paths, (f, g + hazmap[y-1, x], [y-1, x]))
                visited[y-1, x] = f

        if y+1 < hazmap.shape[0]:
            f = g + hazmap[y+1, x] + abs(((y+1) - y_goal) + (x-x_goal))
            if visited[y+1, x] > f:
                heapq.heappush(paths, (f, g + hazmap[y+1, x], [y+1, x]))
                visited[y+1, x] = f



hazard = np.genfromtxt('input.txt', delimiter=1, dtype=int)

print('Part 1: ' + str(pathfind(hazard, [hazard.shape[0]-1, hazard.shape[1]-1])))

small_hazard = np.genfromtxt('input.txt', delimiter=1, dtype=int)

hazard = np.zeros([small_hazard.shape[0]*5, small_hazard.shape[1]*5])
for i in range(5):
    for j in range(5):
        hazard[i*small_hazard.shape[0]:(i+1)*small_hazard.shape[0], j*small_hazard.shape[1]:(j+1)*small_hazard.shape[1]] = np.mod(small_hazard + i + j - 1, 9) + 1

print('Part 2: ' + str(int(pathfind(hazard, [hazard.shape[0]-1, hazard.shape[1]-1]))))
