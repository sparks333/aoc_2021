
input_file = open('input.txt')

x = 0
y = 0

for lines in input_file:
    sp = lines.split()
    if sp[0] == 'up':
        y -= int(sp[1])
    elif sp[0] == 'down':
        y += int(sp[1])
    elif sp[0] == 'forward':
        x += int(sp[1])
    else:
        print('Error: Unkown token ' + sp[0])

print('Part 1:')
print('X: ' + str(x) + ', Y: ' + str(y))
print('Solution: ' + str(x*y))

input_file = open('input.txt')

x = 0
y = 0
aim = 0

for lines in input_file:
    sp = lines.split()
    if sp[0] == 'up':
        aim -= int(sp[1])
    elif sp[0] == 'down':
        aim += int(sp[1])
    elif sp[0] == 'forward':
        x += int(sp[1])
        y += aim * int(sp[1])

print('Part 2:')
print('X: ' + str(x) + ', Y: ' + str(y), ', Aim: ' + str(aim))
print('Solution: ' + str(x*y))