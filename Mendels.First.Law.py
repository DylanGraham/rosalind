import random
from collections import defaultdict
from fractions import Fraction

samples = 1000
data1 = [0b11] * 2
data2 = [0b10, 0b01]
data3 = [0b00] * 2
data = data1 + data2 + data3

#result = {0: 0, 1: 0, 2: 0}
result = defaultdict(int)

for _ in range(samples):
    pick = random.sample(data, 2)
    result[pick[0] | pick[1]] += 1

print((result[3] + result[2]) / samples)
print(result)

# TODO: play with fractions
a = 2
b = 2
c = 2

