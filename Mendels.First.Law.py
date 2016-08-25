from fractions import Fraction as Fr


def reset_data():
    global data
    data = {'a': 21, 'b': 18, 'c': 21}


def pick(x):
    global data
    if data[x] > 0:
        data[x] -= 1
    else:
        raise IndexError


def prob(x):
    return Fr(data[x], sum(data.values()))

data = {}
output = {}
for event in 'aa bb cc ab ac ba bc ca cb'.split():
    output[event] = {}
    reset_data()
    for gene, probability in zip(event, 'p1 p2'.split()):
        output[event][probability] = prob(gene)
        pick(gene)
    output[event]['p'] = output[event]['p1'] * output[event]['p2']

for event in 'aa bb cc ab ac ba bc ca cb'.split():
    print('Probability of {}: {}'.format(event, output[event]['p']))

print('Probability that two randomly selected mating organisms will'
      'produce an individual possessing a dominant allele\n'
      '(and thus displaying the dominant phenotype). Assume that any two organisms can mate.')

result = 0
for event in 'aa bb cc ab ac ba bc ca cb'.split():
    multiplier = 1
    if event == 'cc':
        continue
    elif event == 'bb':
        multiplier = .75
    elif event == 'bc' or event == 'cb':
        multiplier = .5
    result += output[event]['p'] * multiplier

print(result)
