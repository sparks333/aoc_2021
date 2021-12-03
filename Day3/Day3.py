
import numpy as np

n_bits = 12

input = np.loadtxt('input.txt', converters={_:lambda s: int(s, 2) for _ in range(1)}, dtype='int32')

popcnt = np.zeros(n_bits)

for i in input:
    for j in range(n_bits):
        popcnt[(n_bits-1) - j] += (i & (1 << j)) != 0

popcnt_gamma = popcnt > (input.size/2)
gamma = sum(2**i for i, v in enumerate(reversed(popcnt_gamma)) if v)
popcnt_epsilon = ~popcnt_gamma;
epsilon = sum(2**i for i, v in enumerate(reversed(popcnt_epsilon)) if v)
print('Part 1:')
print(gamma*epsilon)

candidate_o2_vals = input
candidate_co2_vals = input

for j in range(n_bits):
    index = (n_bits-1)-j
    sub_popcnt = 0
    for i in candidate_o2_vals:
        sub_popcnt += (i & (1 << index)) != 0

    if(sub_popcnt >= candidate_o2_vals.size/2):
        candidate_o2_vals = candidate_o2_vals[(candidate_o2_vals & 2**index) != 0]
    else:
        candidate_o2_vals = candidate_o2_vals[(candidate_o2_vals & 2**index) == 0]
    if candidate_o2_vals.size == 1:
        break

for j in range(n_bits):
    index = (n_bits-1)-j
    sub_popcnt = 0
    for i in candidate_co2_vals:
        sub_popcnt += (i & (1 << index)) != 0

    if(sub_popcnt < candidate_co2_vals.size/2):
        candidate_co2_vals = candidate_co2_vals[(candidate_co2_vals & 2**index) != 0]
    else:
        candidate_co2_vals = candidate_co2_vals[(candidate_co2_vals & 2**index) == 0]
    if candidate_co2_vals.size == 1:
        break
print('Part 2:')
print(candidate_o2_vals[0] * candidate_co2_vals[0])