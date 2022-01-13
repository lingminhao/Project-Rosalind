from Bio import SeqIO

DNAstring = SeqIO.read("input/rosalind_kmer.txt", "fasta").seq
nucleotide = ['A', 'C', 'G', 'T']
k = 4

### START CODE HERE ###
def kmercomposition(nucleotide, k): 
    if k == 0: 
        yield ''
    else: 
        for base in nucleotide: 
            for results in kmercomposition(nucleotide,k-1): 
                yield base + results


kmercomposition_table = list(kmercomposition(nucleotide,4))
kmercomposition_count = [0]*len(kmercomposition_table)

for i in range(len(kmercomposition_table)): 
    for j in range(len(DNAstring)-k+1): 
        if kmercomposition_table[i] == DNAstring[j:j+k]: 
            kmercomposition_count[i] += 1

### END CODE HERE ###

with open('output/rosalind_kmer_output.txt', 'w') as f: 
    for count in kmercomposition_count: 
        f.write(str(count))
        f.write(' ')
