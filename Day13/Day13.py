import numpy as np

paper = np.zeros([10, 10])

n_folds = 0

with open('input.txt') as file:
    coords = True
    for line in file:
        if n_folds == 1:
            break
        if line == '\n':
            coords = False
            continue
        if coords == True:
            coord = line.strip().split(',')
            x = int(coord[0])
            y = int(coord[1])

            if x >= paper.shape[1] or y >= paper.shape[0]:
                new_paper = np.zeros([max(paper.shape[0], y+1), max(paper.shape[1], x+1)])
                new_paper[0:paper.shape[0], 0:paper.shape[1]] = paper
                paper = new_paper
            paper[y, x] = 1
        else:
            inst = line.strip().split()
            fold = inst[2].split('=')
            dim = int(fold[1])
            if fold[0] == 'x':
                rem = (paper.shape[1] - dim)-1
                folded_paper = paper[:, 0:dim]
                np.logical_or(folded_paper[:, -rem:], np.fliplr(paper[:, -rem:]), folded_paper[:, -rem:])
                paper = folded_paper          
                n_folds += 1
            elif fold[0] == 'y':
                rem = (paper.shape[0] - dim)-1
                folded_paper = paper[0:dim,:]
                np.logical_or(folded_paper[-rem:,:], np.flipud(paper[-rem:,:]), folded_paper[-rem:,:])
                paper = folded_paper
                n_folds += 1
            else:
                print('Something went wrong')
    print('Part 1: ' + str(np.sum(paper == 1)))


paper = np.zeros([10, 10])

with open('input.txt') as file:
    coords = True
    for line in file:
        if line == '\n':
            coords = False
            continue
        if coords == True:
            coord = line.strip().split(',')
            x = int(coord[0])
            y = int(coord[1])

            if x >= paper.shape[1] or y >= paper.shape[0]:
                new_paper = np.zeros([max(paper.shape[0], y+1), max(paper.shape[1], x+1)])
                new_paper[0:paper.shape[0], 0:paper.shape[1]] = paper
                paper = new_paper
            paper[y, x] = 1
        else:
            inst = line.strip().split()
            fold = inst[2].split('=')
            dim = int(fold[1])
            if fold[0] == 'x':
                rem = (paper.shape[1] - dim)-1
                folded_paper = paper[:, 0:dim]
                np.logical_or(folded_paper[:, -rem:], np.fliplr(paper[:, -rem:]), folded_paper[:, -rem:])
                paper = folded_paper          
                n_folds += 1
            elif fold[0] == 'y':
                rem = (paper.shape[0] - dim)-1
                folded_paper = paper[0:dim,:]
                np.logical_or(folded_paper[-rem:,:], np.flipud(paper[-rem:,:]), folded_paper[-rem:,:])
                paper = folded_paper
                n_folds += 1
            else:
                print('Something went wrong')
    print('Part 2:')

    for y in range(paper.shape[0]):
        for x in range(paper.shape[1]):
            if paper[y,x] == 0:
                st = ' '
            else:
                st = '.'
            print(st, end='')
        print()


