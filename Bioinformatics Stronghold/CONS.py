from Bio import SeqIO

DNAcollection = []
for record in SeqIO.parse("input/rosalind_cons.txt", "fasta"):
    DNAcollection.append(str(record.seq))

m = len(DNAcollection[0])

### START CODE ###
nucleotide = ['A', 'C', 'G', 'T']


profilematrix = [[0]*m,[0]*m,[0]*m,[0]*m]
for i in range(len(DNAcollection)): 
    for j in range(m): 
        for k in range(len(nucleotide)): 
            if DNAcollection[i][j] == nucleotide[k]: 
                profilematrix[k][j] += 1

consensus = ''
for i in range(m): 
    best = 0
    for j in range(len(nucleotide)): 
        if profilematrix[j][i] >= best : 
            best_nucleotide = nucleotide[j]
            best = profilematrix[j][i]
    consensus += best_nucleotide
### END CODE ###

with open('output/rosalind_cons_output.txt', 'w') as f: 
    f.write(consensus)
    f.write('\n')
    for i in range(len(nucleotide)): 
        f.write(nucleotide[i] + ': ')
        for j in range(len(profilematrix[i])): 
            f.write(str(profilematrix[i][j]))
            f.write(' ')
            
        f.write('\n')
        
    
