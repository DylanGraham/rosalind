import re

with open('/home/dylan/Downloads/rosalind_subs.txt') as fp:
    data = fp.readline()

output = [m.start() + 1 for m in re.finditer('(?=GAAGGTTGA)', data)]
print(output)
