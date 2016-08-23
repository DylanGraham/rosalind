with open('/home/dylan/Downloads/rosalind_hamm.txt') as fp:
    data = fp.readlines()

total = 0
for x, y in zip(*data):
    if x != y:
        total += 1

print(total)
