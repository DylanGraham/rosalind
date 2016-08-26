import numpy as np
from Bio import AlignIO
from Bio.Align import AlignInfo

from Bio.Seq import Seq


class MySummaryInfo(AlignInfo.SummaryInfo):
    def __init__(self, alignment):
        super()
        self.alignment = alignment
        self.ic_vector = {}

    def dumb_consensus(self, threshold=.7, ambiguous="X",
                       consensus_alpha=None, require_multiple=0):
        consensus = ''

        # find the length of the consensus we are creating
        con_len = alignment.get_alignment_length()

        # go through each seq item
        for n in range(con_len):
            # keep track of the counts of the different atoms we get
            atom_dict = {}
            num_atoms = 0

            for record in alignment:
                # make sure we haven't run past the end of any sequences
                # if they are of different lengths
                if n < len(record.seq):
                    if record.seq[n] != '-' and record.seq[n] != '.':
                        if record.seq[n] not in atom_dict:
                            atom_dict[record.seq[n]] = 1
                        else:
                            atom_dict[record.seq[n]] += 1

                        num_atoms += 1

            max_atoms = []
            max_size = 0

            for atom in atom_dict:
                if atom_dict[atom] > max_size:
                    max_atoms = [atom]
                    max_size = atom_dict[atom]
                elif atom_dict[atom] == max_size:
                    max_atoms.append(atom)

            if require_multiple and num_atoms == 1:
                consensus += ambiguous
            elif (len(max_atoms) == 1) and ((float(max_size) /
                                             float(num_atoms)) >= threshold):
                consensus += max_atoms[0]
            else:
                # consensus += ambiguous
                consensus += max_atoms[0]

        # we need to guess a consensus alphabet if one isn't specified
        if consensus_alpha is None:
            consensus_alpha = self._guess_consensus_alphabet(ambiguous)

        return Seq(consensus, consensus_alpha)


# Make an alignment from the fasta file
alignment = AlignIO.read(open('/home/dylan/Downloads/rosalind_cons.txt'), 'fasta')
print(alignment)

# Create numpy array
align_array = np.array([list(rec) for rec in alignment])
print("Array shape %i by %i" % align_array.shape)

# Make summary alignment and consensus
# summary_align = AlignInfo.SummaryInfo(alignment)
summary_align = MySummaryInfo(alignment)
consensus = summary_align.dumb_consensus(threshold=.1)
print(consensus)

my_pssm = summary_align.pos_specific_score_matrix(consensus, chars_to_ignore=['X'])
# print(my_pssm)

# Print the profile matrix how rosalind wants it
for i in 'ACGT':
    print(i + ": ", end="")
    for j in range(len(str(consensus))):
        print(int(my_pssm[j][i]), end=" ")
    print()

