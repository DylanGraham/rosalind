from fractions import Fraction as Fr
import random

data = {}


def reset_data():
    global data
    data = {'a': 21, 'b': 18, 'c': 21}


def pick(x):
    global data
    if data[x] > 0:
        data[x] -= 1
        return True
    else:
        return False


def prob(x):
    return Fr(data[x], sum(data.values()))


reset_data()
p1 = prob('a')
pick('a')
p2 = prob('a')
aa = p1 * p2

reset_data()
p1 = prob('b')
pick('b')
p2 = prob('b')
bb = p1 * p2

reset_data()
p1 = prob('c')
pick('c')
p2 = prob('c')
cc = p1 * p2

reset_data()
p1 = prob('a')
pick('a')
p2 = prob('b')
ab = p1 * p2

reset_data()
p1 = prob('a')
pick('a')
p2 = prob('c')
ac = p1 * p2

reset_data()
p1 = prob('b')
pick('b')
p2 = prob('a')
ba = p1 * p2

reset_data()
p1 = prob('b')
pick('b')
p2 = prob('c')
bc = p1 * p2

reset_data()
p1 = prob('c')
pick('c')
p2 = prob('a')
ca = p1 * p2

reset_data()
p1 = prob('c')
pick('c')
p2 = prob('b')
cb = p1 * p2

print('Probability of 2 x a ', aa)
print('Probability of 2 x b ', bb)
print('Probability of 2 x c ', cc)
print('Probability of 1 x a, 1 x b ', ab)
print('Probability of 1 x a, 1 x c ', ac)
print('Probability of 1 x b, 1 x a ', ba)
print('Probability of 1 x b, 1 x c ', bc)
print('Probability of 1 x c, 1 x a ', ca)
print('Probability of 1 x c, 1 x b ', cb)

print('Probability that two randomly selected mating organisms will'
      'produce an individual possessing a dominant allele\n'
      '(and thus displaying the dominant phenotype). Assume that any two organisms can mate.')

print(aa + (bb * 3/4) + ab + ac + ba + (bc * 1/2) + ca + (cb * 1/2))
print(aa + (bb * .75) + ab + ac + ba + (bc * .5) + ca + (cb * .5))
