from fractions import Fraction as Fr


def pick(data, x):
    if data[x] > 0:
        data[x] -= 1
        return True
    else:
        return False


def prob(x):
    return Fr(x, sum(data.values()))

print('Probability of 2 x a')
data = {'a': 2, 'b': 2, 'c': 2}
p1 = prob(data['a'])
pick(data, 'a')
p2 = prob(data['a'])
print(p1 * p2)

print('Probability of 2 x b')
data = {'a': 2, 'b': 2, 'c': 2}
p1 = prob(data['b'])
pick(data, 'b')
p2 = prob(data['b'])
print(p1 * p2)

print('Probability of 2 x c')
data = {'a': 2, 'b': 2, 'c': 2}
p1 = prob(data['c'])
pick(data, 'c')
p2 = prob(data['c'])
print(p1 * p2)

print('Probability of 1 x a, 1 x b')
data = {'a': 2, 'b': 2, 'c': 2}
p1 = prob(data['a'])
pick(data, 'a')
p2 = prob(data['b'])
print(p1 * p2)

print('Probability of 1 x a, 1 x c')
data = {'a': 2, 'b': 2, 'c': 2}
p1 = prob(data['a'])
pick(data, 'a')
p2 = prob(data['c'])
print(p1 * p2)

print('Probability of 1 x b, 1 x a')
data = {'a': 2, 'b': 2, 'c': 2}
p1 = prob(data['b'])
pick(data, 'b')
p2 = prob(data['a'])
print(p1 * p2)

print('Probability of 1 x b, 1 x c')
data = {'a': 2, 'b': 2, 'c': 2}
p1 = prob(data['b'])
pick(data, 'b')
p2 = prob(data['c'])
print(p1 * p2)

print('Probability of 1 x c, 1 x a')
data = {'a': 2, 'b': 2, 'c': 2}
p1 = prob(data['c'])
pick(data, 'c')
p2 = prob(data['a'])
print(p1 * p2)

print('Probability of 1 x c, 1 x b')
data = {'a': 2, 'b': 2, 'c': 2}
p1 = prob(data['c'])
pick(data, 'c')
p2 = prob(data['b'])
print(p1 * p2)
