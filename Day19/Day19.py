import numpy as np
import random

def ransac(pts1, pts2):
    best_model = (0, [0, 0, 0])
    for i in range(100):
        inliers = 0
        pt1 = pts1[random.randint(0, len(pts1)-1)]
        pt2 = pts2[random.randint(0, len(pts2)-1)]
        model = pt1 - pt2

        for j in range(len(pts2)):
            if (pts2[j]+model).tolist() in pts1.tolist():
                inliers += 1
        if inliers > best_model[0]:
            best_model = (inliers, model)
    return best_model

def rotate(pts, p, q, r, s):
    new_pts = np.zeros_like(pts)
    A = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    B = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    rot_max = np.matmul(np.matmul(np.matmul(np.linalg.matrix_power(A, p), np.linalg.matrix_power(B, q)), np.linalg.matrix_power(A, r)), np.linalg.matrix_power(B, s))
    for i in range(len(pts)):
        new_pts[i, :] = np.matmul(rot_max, pts[i, :])
    return new_pts

def translate(pts, offset):
    new_pts = np.zeros_like(pts)
    for i in range(len(pts)):
        new_pts[i, :] = pts[i, :] + offset
    return new_pts

with open('input.txt') as file:
    scanner = []
    scanner_num = -1
    first = True
    for line in file:
        if line.strip()[0:12] == '--- scanner ':
            scanner_num += 1
            first = True
        elif line.strip() != '':
            if first == True:
                line_str = line.strip().split(',')
                line_num = [int(i) for i in line_str]
                scanner.append(np.array(line_num))
                first = False
            else:
                line_str = line.strip().split(',')
                line_num = [int(i) for i in line_str]
                new_axis = np.vstack((scanner[-1], np.array(line_num)))
                scanner[-1] = new_axis

    found = np.zeros(scanner_num+1)
    found[0] = 1
    tried = np.eye(len(scanner))
    locs = []

    while sum(found) < len(scanner):
        for i in range(len(scanner)):
            if found[i] == 0:
                continue
            for j in range(len(scanner)):
                if i == j or found[j] == 1 or tried[i,j] == 1:
                    continue
                tried[i,j] = 1
                for s in range(4):
                    for r in range(4):
                        for q in range(4):
                            for p in range(4):
                                new_j = rotate(scanner[j], p, q, r, s)
                                res = ransac(scanner[i], new_j)
                                if res[0] >= 12:
                                    scanner[j] = translate(new_j, res[1])
                                    locs.append(res[1])
                                    found[j] = 1
                                    break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
    unique_probes = []

    for i in range(len(scanner)):
        for j in range(len(scanner[i])):
            if not scanner[i][j].tolist() in unique_probes:
                unique_probes.append(scanner[i][j].tolist())
    print('Part 1: ' + str(len(unique_probes)))
    
    max_dist = 0

    for i in range(len(locs)):
        for j in range(len(locs)):
            dist = np.sum(np.abs(np.array(locs[i]) - np.array(locs[j])))
            if dist > max_dist:
                max_dist = dist

    print('Part 2: ' + str(max_dist))