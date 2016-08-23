from Bio import SeqIO
from collections import Counter

fasta = SeqIO.parse(open('/home/dylan/Downloads/rosalind_gc.txt'), 'fasta')

for f in fasta:
    name, seq = f.id, str(f.seq)
    c = Counter(f.seq)
    l = len(seq)
    cg = sum([(c[x]) for x in ('C', 'G')])
    print(name)
    print((cg / l) * 100)
