import numpy as np

cubes = np.zeros([101, 101, 101])

with open('input.txt') as file:
    for line in file:
        first = line.split()
        if first[0] == 'on':
            on = True
        else:
            on = False
        second = first[1].split(',')
        x = second[0][2:].split(',')[0].split('..')
        y = second[1][2:].split(',')[0].split('..')
        z = second[2][2:].split(',')[0].split('..')

        x_start = int(x[0]) + 50
        x_stop = int(x[1]) + 51
        y_start = int(y[0]) + 50
        y_stop = int(y[1]) + 51
        z_start = int(z[0]) + 50
        z_stop = int(z[1]) + 51

        if x_start < 0 or x_stop > 100 or y_start < 0 or y_stop > 100 or z_start < 0 or z_stop > 100:
            continue       

        cubes[x_start:x_stop, y_start:y_stop, z_start:z_stop] = on

    print('Part 1: ' + str(np.sum(cubes)))

def shatter(cuboid, on, cuboid_list):
    x1 = cuboid[0][0]
    x2 = cuboid[0][1]
    y1 = cuboid[1][0]
    y2 = cuboid[1][1]
    z1 = cuboid[2][0]
    z2 = cuboid[2][1]

    for i in cuboid_list:

        if i[0] == False:
            continue

        x1_tmp = i[1][0][0]
        x2_tmp = i[1][0][1]
        y1_tmp = i[1][1][0]
        y2_tmp = i[1][1][1]
        z1_tmp = i[1][2][0]
        z2_tmp = i[1][2][1]

        x1_intersect = max(x1, x1_tmp)
        x2_intersect = min(x2, x2_tmp)
        y1_intersect = max(y1, y1_tmp)
        y2_intersect = min(y2, y2_tmp)
        z1_intersect = max(z1, z1_tmp)
        z2_intersect = min(z2, z2_tmp)

        if x1_tmp >= x1 and x2_tmp <= x2 and y1_tmp >= y1 and y2_tmp <= y2 and z1_tmp >= z1 and z2_tmp <= z2:
            i[0] = False
            continue
        if x1_intersect > x1_tmp and x1_intersect < x2_tmp:
            i[0] = False
            cuboid_list.append([True, [[x1_tmp, x1_intersect], [y1_tmp, y2_tmp], [z1_tmp, z2_tmp]]])
            cuboid_list.append([True, [[x1_intersect, x2_tmp], [y1_tmp, y2_tmp], [z1_tmp, z2_tmp]]])
            continue
        if y1_intersect > y1_tmp and y1_intersect < y2_tmp:
            i[0] = False
            cuboid_list.append([True, [[x1_tmp, x2_tmp], [y1_tmp, y1_intersect], [z1_tmp, z2_tmp]]])
            cuboid_list.append([True, [[x1_tmp, x2_tmp], [y1_intersect, y2_tmp], [z1_tmp, z2_tmp]]])
            continue
        if z1_intersect > z1_tmp and z1_intersect < z2_tmp:
            i[0] = False
            cuboid_list.append([True, [[x1_tmp, x2_tmp], [y1_tmp, y2_tmp], [z1_tmp, z1_intersect]]])
            cuboid_list.append([True, [[x1_tmp, x2_tmp], [y1_tmp, y2_tmp], [z1_intersect, z2_tmp]]])
            continue
        if x2_intersect > x1_tmp and x2_intersect < x2_tmp:
            i[0] = False
            cuboid_list.append([True, [[x1_tmp, x2_intersect],[y1_tmp, y2_tmp], [z1_tmp, z2_tmp]]])
            cuboid_list.append([True, [[x2_intersect, x2_tmp],[y1_tmp, y2_tmp], [z1_tmp, z2_tmp]]])
            continue
        if y2_intersect > y1_tmp and y2_intersect < y2_tmp:
            i[0] = False
            cuboid_list.append([True, [[x1_tmp, x2_tmp],[y1_tmp, y2_intersect], [z1_tmp, z2_tmp]]])
            cuboid_list.append([True, [[x1_tmp, x2_tmp],[y2_intersect, y2_tmp], [z1_tmp, z2_tmp]]])
            continue
        if z2_intersect > z1_tmp and z2_intersect < z2_tmp:
            i[0] = False
            cuboid_list.append([True, [[x1_tmp, x2_tmp],[y1_tmp, y2_tmp], [z1_tmp, z2_intersect]]])
            cuboid_list.append([True, [[x1_tmp, x2_tmp],[y1_tmp, y2_tmp], [z2_intersect, z2_tmp]]])
            continue
    if on:
        cuboid_list.append([True, cuboid])






with open('test.txt') as file:

    cuboids = []
    total_cubes = 0
    for line in file:
        first = line.split()
        if first[0] == 'on':
            on = True
        else:
            on = False
        second = first[1].split(',')
        x = second[0][2:].split(',')[0].split('..')
        y = second[1][2:].split(',')[0].split('..')
        z = second[2][2:].split(',')[0].split('..')

        x_start = float(x[0])
        x_stop = float(x[1])+1
        y_start = float(y[0])
        y_stop = float(y[1])+1
        z_start = float(z[0])
        z_stop = float(z[1])+1

        new_cuboid = [[x_start, x_stop], [y_start, y_stop], [z_start, z_stop]]

        shatter(new_cuboid, on, cuboids)

        for i in cuboids:
            if i[0] == False:
                cuboids.remove(i)

        total_on = 0
        for i in cuboids:
            if i[0]:
                total_on += (i[1][0][1]-i[1][0][0])*(i[1][1][1]-i[1][1][0])*(i[1][2][1]-i[1][2][0])
        print('Total On: ' + str(total_on))


print('Part 2: ' + str(total_on))
