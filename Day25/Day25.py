import numpy as np

list_map = []

with open('input.txt') as file:
    for line in file:
        list_data = []
        for ch in line.strip():
            if ch == '.':
                list_data.append(0)
            elif ch == '>':
                list_data.append(1)
            elif ch == 'v':
                list_data.append(2)
        list_map.append(list_data)
    np_map = np.array(list_map)

    movement = True
    n_moves = 0
    while movement:
        movement = False
        new_map = np.zeros_like(np_map)
    
        for y in range(np_map.shape[0]):
            for x in range(np_map.shape[1]):
                if np_map[y,x] == 1:
                    if x == np_map.shape[1]-1:
                        new_x = 0
                    else:
                        new_x = x + 1
                    if np_map[y, new_x] == 0:
                        new_map[y, new_x] = 1
                        movement = True
                    else:
                        new_map[y,x] = 1
                elif np_map[y,x] == 2:
                    new_map[y,x] = 2

        np_map = new_map
        new_map = np.zeros_like(np_map)

        for y in range(np_map.shape[0]):
            for x in range(np_map.shape[1]):
                if np_map[y,x] == 2:
                    if y == np_map.shape[0]-1:
                        new_y = 0
                    else:
                        new_y = y + 1
                    if np_map[new_y, x] == 0:
                        new_map[new_y, x] = 2
                        movement = True
                    else:
                        new_map[y,x] = 2
                elif np_map[y,x] == 1:
                    new_map[y,x] = 1

        np_map = new_map
        n_moves += 1

    print('Part 1: ' + str(n_moves))
