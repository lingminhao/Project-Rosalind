with open('input/rosalind_dna.txt') as f: 
    file = f.readlines()

DNAstring = file[0].strip()

### START CODE ###
# Count for A,C,G,T
count = [0,0,0,0]

for i in range(len(DNAstring)): 
    if DNAstring[i] == 'A': 
        count[0] += 1
    if DNAstring[i] == 'C': 
        count[1] += 1
    if DNAstring[i] == 'G': 
        count[2] += 1
    if DNAstring[i] == 'T': 
        count[3] += 1
### END CODE ###

with open('output/rosalind_dna_output.txt','w') as f: 
    for i in range(len(count)): 
        f.write(str(count[i]))
        f.write(" ")