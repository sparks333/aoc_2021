import numpy as np
import heapq
import copy
from itertools import count
from collections import defaultdict

from numpy.typing import _128Bit

def is_complete(game_map):
    if game_map[3, 3] == 1 and game_map[2, 3] == 1 and \
       game_map[3, 5] == 2 and game_map[2, 5] == 2 and \
       game_map[3, 7] == 3 and game_map[2, 7] == 3 and \
       game_map[3, 9] == 4 and game_map[2, 9] == 4:
        return True
    else:
        return False

def is_complete_pt2(game_map):
    if game_map[5, 3] == 1 and game_map[4, 3] == 1 and game_map[3, 3] == 1 and game_map[2, 3] == 1 and \
       game_map[5, 5] == 2 and game_map[4, 5] == 2 and game_map[3, 5] == 2 and game_map[2, 5] == 2 and \
       game_map[5, 7] == 3 and game_map[4, 7] == 3 and game_map[3, 7] == 3 and game_map[2, 7] == 3 and \
       game_map[5, 9] == 4 and game_map[4, 9] == 4 and game_map[3, 9] == 4 and game_map[2, 9] == 4:
        return True
    else:
        return False

def valid_move(y_start, x_start, x_end, y_end, game_map):
    # Not a movable game element
    if game_map[y_start, x_start] <= 0 or game_map[y_end, x_end] != 0:
        return False

    # Blocked on all sides, movement is not possible
    if game_map[y_start, x_start + 1] != 0 and game_map[y_start, x_start - 1] != 0 and game_map[y_start+1, x_start] != 0 and game_map[y_start-1, x_start] != 0:
        return False

    # Stopping in a hallway outside a door
    if y_end == 1 and (x_end == 3 or x_end == 5 or x_end == 7 or x_end == 9):
        return False

    # Going into a room that is not yours (A)
    if game_map[y_start, x_start] == 1 and (x_end == 5 or x_end == 7 or x_end == 9):
        return False

    # Going into a room that is not yours (B)
    if game_map[y_start, x_start] == 2 and (x_end == 3 or x_end == 7 or x_end == 9):
        return False

    # Going into a room that is not yours (C)
    if game_map[y_start, x_start] == 3 and (x_end == 3 or x_end == 5 or x_end == 9):
        return False

    # Going into a room that is not yours (D)
    if game_map[y_start, x_start] == 4 and (x_end == 3 or x_end == 5 or x_end == 7):
        return False

    # Move in hallway
    if y_start == 1 and y_end == 1:
        return False

    # Move vertically in room
    if x_start == x_end:
        return False
    
    # Failure to move all the way to the back of the room
    if y_end == 2 and game_map[3, x_end] == 0:
        return False

    # Placing an amphipod in a room with a wrong amphipod behind it
    if y_end == 2 and game_map[3, x_end] != game_map[y_start, x_start]:
        return False

    # Moving finalized pieces (A)
    if game_map[y_start, x_start] == 1 and x_start == 3:
        if y_start == 3:
            return False
        if y_start == 2 and game_map[3, x_start] == 1:
            return False

    # Moving finalized pieces (B)
    if game_map[y_start, x_start] == 2 and x_start == 5:
        if y_start == 3:
            return False
        if y_start == 2 and game_map[3, x_start] == 2:
            return False

    # Moving finalized pieces (C)
    if game_map[y_start, x_start] == 3 and x_start == 7:
        if y_start == 3:
            return False
        if y_start == 2 and game_map[3, x_start] == 3:
            return False

    # Moving finalized pieces (D)
    if game_map[y_start, x_start] == 4 and x_start == 9:
        if y_start == 3:
            return False
        if y_start == 2 and game_map[3, x_start] == 4:
            return False

    # Blocked hallway
    if x_start != x_end:
       if x_start < x_end:
           if not np.all(game_map[1, x_start+1:x_end+1] == 0):
               return False
       else:
            if not np.all(game_map[1, x_end:x_start] == 0):
                return False
    return True

def valid_move_pt2(y_start, x_start, y_end, x_end, game_map):
    # Not a movable game element
    if game_map[y_start, x_start] <= 0 or game_map[y_end, x_end] != 0:
        return False

    # Blocked on all sides, movement is not possible
    if game_map[y_start, x_start + 1] != 0 and game_map[y_start, x_start - 1] != 0 and game_map[y_start+1, x_start] != 0 and game_map[y_start-1, x_start] != 0:
        return False

    # Stopping in a hallway outside a door
    if y_end == 1 and (x_end == 3 or x_end == 5 or x_end == 7 or x_end == 9):
        return False

    # Going into a room that is not yours (A)
    if game_map[y_start, x_start] == 1 and (x_end == 5 or x_end == 7 or x_end == 9):
        return False

    # Going into a room that is not yours (B)
    if game_map[y_start, x_start] == 2 and (x_end == 3 or x_end == 7 or x_end == 9):
        return False

    # Going into a room that is not yours (C)
    if game_map[y_start, x_start] == 3 and (x_end == 3 or x_end == 5 or x_end == 9):
        return False

    # Going into a room that is not yours (D)
    if game_map[y_start, x_start] == 4 and (x_end == 3 or x_end == 5 or x_end == 7):
        return False

    # Move in hallway
    if y_start == 1 and y_end == 1:
        return False

    # Move vertically in room
    if x_start == x_end:
        return False
    
    # Failure to move all the way to the back of the room
    if y_end > 1 and y_end < 5 and np.all(game_map[y_end+1:6, x_end] == 0):
        return False

    # Placing an amphipod in a room with a wrong amphipod behind it
    if y_end > 1 and y_end < 5 and np.any(game_map[y_end+1:6, x_end] != game_map[y_start, x_start]):
        return False

    # Moving finalized pieces (A)
    if game_map[y_start, x_start] == 1 and x_start == 3:
        if y_start > 1 and np.all(game_map[y_start:6, x_start] == 1):
            return False

    # Moving finalized pieces (B)
    if game_map[y_start, x_start] == 2 and x_start == 5:
        if y_start > 1 and np.all(game_map[y_start:6, x_start] == 2):
            return False

    # Moving finalized pieces (C)
    if game_map[y_start, x_start] == 3 and x_start == 7:
        if y_start > 1 and np.all(game_map[y_start:6, x_start] == 3):
            return False

    # Moving finalized pieces (D)
    if game_map[y_start, x_start] == 4 and x_start == 9:
        if y_start > 1 and np.all(game_map[y_start:6, x_start] == 4):
            return False

    # Blocked room
    if y_start > 1:
        if not np.all(game_map[1:y_start, x_start] == 0):
            return False

    # Blocked hallway
    if x_start != x_end:
       if x_start < x_end:
           if not np.all(game_map[1, x_start+1:x_end+1] == 0):
               return False
       else:
            if not np.all(game_map[1, x_end:x_start] == 0):
                return False
    return True

def move(y_start, x_start, y_end, x_end, game_map):
    
    gm = copy.deepcopy(game_map)
    gm[y_start, x_start] = 0
    gm[y_end, x_end] = game_map[y_start, x_start]
    return ((10**(game_map[y_start, x_start]-1)) * (abs(x_end - x_start) + abs(y_start - 1) + abs(y_end - 1)), gm)

game_map = -1*np.ones([5, 13])

with open('input.txt') as file:
    y = 0
    for line in file:
        x=0
        for ch in line[:-1]:
            if ch == '.':
                game_map[y,x] = 0
            elif ch == 'A':
                game_map[y, x] = 1
            elif ch == 'B':
                game_map[y,x] = 2
            elif ch == 'C':
                game_map[y,x] = 3
            elif ch == 'D':
                game_map[y,x] = 4
            x+=1
        y+=1
    
counter = count()
frontier = [[0, next(counter), game_map]]
explored = {}
costs = defaultdict(lambda: float('inf'))

while True:

    node = heapq.heappop(frontier)

    explored[tuple(map(tuple, node[2]))] = node

    if is_complete(node[2]):
        print('Part 1: ' + str(node[0]))
        break
    for y_start in range(1, 4):
        for x_start in range(1,12):
            for y_end in range(1, 4):
                for x_end in range(1,12):
                    if valid_move(y_start, x_start, x_end, y_end, node[2]):
                        attempt = move(y_start, x_start, x_end, y_end, node[2])
                        new_cost = node[0] + attempt[0]
                        new_map = attempt[1]
                        new_key = tuple(map(tuple, new_map))
                        if new_key in explored:
                            continue
                        if costs[new_key] > new_cost:
                            costs[new_key] = new_cost
                            heapq.heappush(frontier, [new_cost, next(counter), new_map])

def est_cost(game_map):
    total_cost = 0
    for y in range(1, 6):
        for x in range(1,12):
            a_type = game_map[y,x]
            if game_map[y,x] > 0:
                target_x = 2*a_type+1
                if x != target_x:
                    total_cost += (10**(a_type-1)) * (abs(x-target_x) + y)
    return total_cost

game_map = -1*np.ones([7, 13])

with open('input2.txt') as file:
    y = 0
    for line in file:
        x=0
        for ch in line[:-1]:
            if ch == '.':
                game_map[y,x] = 0
            elif ch == 'A':
                game_map[y, x] = 1
            elif ch == 'B':
                game_map[y,x] = 2
            elif ch == 'C':
                game_map[y,x] = 3
            elif ch == 'D':
                game_map[y,x] = 4
            x+=1
        y+=1
    
counter = count()
frontier = [[0, next(counter), game_map]]
explored = {}
costs = defaultdict(lambda: float('inf'))

while True:

    node = heapq.heappop(frontier)

    node_cost = node[0]
    node_map = node[2]

    #for y in range(7):
    #    for x in range(13):
    #        if node_map[y,x] == -1:
    #            chout = '#'
    #        elif node_map[y,x] == 0:
    #            chout = '.'
    #        elif node_map[y,x] == 1:
    #            chout = 'A'
    #        elif node_map[y,x] == 2:
    #            chout = 'B' 
    #        elif node_map[y,x] == 3:
    #            chout = 'C'
    #        elif node_map[y,x] == 4:
    #            chout = 'D'
    #        print(chout, end='')
    #    print()
    #print('Cost: ' + str(node[0]))
    #print()

    explored[tuple(map(tuple, node_map))] = node

    if is_complete_pt2(node_map):
        print('Part 2: ' + str(node_cost))
        break
    for y_start in range(1, 6):
        for x_start in range(1,12):
            for y_end in range(1, 6):
                for x_end in range(1,12):
                    if valid_move_pt2(y_start, x_start, y_end, x_end, node_map):
                        attempt = move(y_start, x_start, y_end, x_end, node_map)
                        new_cost = node_cost + attempt[0]
                        new_map = attempt[1]
                        new_key = tuple(map(tuple, new_map))
                        if new_key in explored:
                            continue
                        if costs[new_key] > new_cost:
                            e_cost = est_cost(new_map)
                            costs[new_key] = new_cost
                            heapq.heappush(frontier, [new_cost, next(counter), new_map])


