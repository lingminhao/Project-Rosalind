from Bio import SeqIO

DNAcollection = []
for record in SeqIO.parse("input/rosalind_tran.txt", "fasta"):
    DNAcollection.append(str(record.seq))

string1 = DNAcollection[0]
string2 = DNAcollection[1]    
m = len(DNAcollection[0])

### START CODE ###
def transitioncomplementcheck(base1,base2):
    if ((base1 == 'A' and base2 == 'G') or (base1 == 'G' and base2 == 'A') or
    (base1 == 'C' and base2 == 'T') or (base1 == 'T' and base2 == 'C')): 
        return True

nucleotide = ['A', 'C', 'G', 'T']
transition = 0
transversion = 0

for i in range(m): 
    if string1[i] != string2[i]:
        if transitioncomplementcheck(string1[i],string2[i]): 
            transition += 1
        else: transversion += 1

ratio = transition / transversion 
### END CODE ###
        
with open("output/rosalind_tran_output.txt", 'w') as f: 
    f.write(str(ratio))
f.close()
