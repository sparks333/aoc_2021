import heapq

# target area: x=25..67, y=-260..-200

x_min = 25
x_max = 67
y_min = -260
y_max = -200

in_target = []

for y_initial_vel in range(y_min, (-y_min+1)):
    for x_initial_vel in range(x_max+1):
        x = 0
        y = 0
        y_max_height = 0
        x_vel = x_initial_vel
        y_vel = y_initial_vel

        while True:
            x += x_vel
            if x_vel > 0:
                x_vel -= 1
            y += y_vel
            y_vel -= 1
            if y > y_max_height:
                y_max_height = y
            if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
                heapq.heappush(in_target, (-y_max_height, [x_initial_vel, y_initial_vel]))
                break
            if x > x_max:
                break
            if y < y_min:
                break

            
print('Part 1: ' + str(-heapq.heappop(in_target)[0]))
print('Part 2: ' + str(len(in_target)+1))