from Bio import SeqIO

record = list(SeqIO.parse('input/rosalind_pdst.txt', 'fasta'))

def pdist(seq1, seq2):
    count = 0 
    for i in range(len(seq1)): 
        if seq1[i] != seq2[i]: 
            count += 1
    ratio = count / len(seq2)
    return ratio
    
with open('output/rosalind_pdst_output.txt', 'w') as f: 
    for i in range(len(record)): 
        for j in range(len(record)): 
            f.write(str(pdist(record[i].seq, record[j].seq)) + " ")
        f.write('\n')