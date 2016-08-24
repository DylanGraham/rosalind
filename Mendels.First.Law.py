from fractions import Fraction as Fr

data = {}


def reset_data():
    global data
    data = {'a': 2, 'b': 2, 'c': 2}


def pick(x):
    global data
    if data[x] > 0:
        data[x] -= 1
        return True
    else:
        return False


def prob(x):
    return Fr(data[x], sum(data.values()))

print('Probability of 2 x a')
reset_data()
p1 = prob('a')
pick('a')
p2 = prob('a')
print(p1 * p2)

print('Probability of 2 x b')
reset_data()
p1 = prob('b')
pick('b')
p2 = prob('b')
print(p1 * p2)

print('Probability of 2 x c')
reset_data()
p1 = prob('c')
pick('c')
p2 = prob('c')
print(p1 * p2)

print('Probability of 1 x a, 1 x b')
reset_data()
p1 = prob('a')
pick('a')
p2 = prob('b')
print(p1 * p2)

print('Probability of 1 x a, 1 x c')
reset_data()
p1 = prob('a')
pick('a')
p2 = prob('c')
print(p1 * p2)

print('Probability of 1 x b, 1 x a')
reset_data()
p1 = prob('b')
pick('b')
p2 = prob('a')
print(p1 * p2)

print('Probability of 1 x b, 1 x c')
reset_data()
p1 = prob('b')
pick('b')
p2 = prob('c')
print(p1 * p2)

print('Probability of 1 x c, 1 x a')
reset_data()
p1 = prob('c')
pick('c')
p2 = prob('a')
print(p1 * p2)

print('Probability of 1 x c, 1 x b')
reset_data()
p1 = prob('c')
pick('c')
p2 = prob('b')
print(p1 * p2)
