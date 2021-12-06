import numpy as np

n_days = 80

fish = np.loadtxt('input.txt',delimiter=',' )
for i in range(n_days):
    fish -= 1
    new_fish = sum(fish == -1)
    fish[fish == -1] = 6
    fish = np.append(fish, 8*np.ones(new_fish))
print('Part 1: ' + str(len(fish)))

n_days = 256
population = np.zeros(9)
fish = np.loadtxt('input.txt', delimiter=',')
for i in fish:
    population[int(i)]+=1

for i in range(n_days):
    new_fish = population[0]
    population[0:8] = population[1:9]
    population[8] = new_fish
    population[6] += new_fish

print('Part 2: ' + str(int(np.sum(population))))
