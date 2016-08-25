import numpy as np
from Bio import AlignIO
from Bio.Align import AlignInfo

# Make an alignment from the fasta file
alignment = AlignIO.read(open('/home/dylan/Downloads/rosalind_cons.txt'), 'fasta')
print(alignment)

# Create numpy array
align_array = np.array([list(rec) for rec in alignment])
print("Array shape %i by %i" % align_array.shape)

# Make summary alignment and consensus
summary_align = AlignInfo.SummaryInfo(alignment)
consensus = summary_align.dumb_consensus(threshold=.4)
print(consensus)

my_pssm = summary_align.pos_specific_score_matrix(consensus, chars_to_ignore=['X'])
# print(my_pssm)

# Print the profile matrix how rosalind wants it
for i in 'ACGT':
    print(i + ": ", end="")
    for j in range(len(str(consensus))):
        print(int(my_pssm[j][i]), end=" ")
    print()

