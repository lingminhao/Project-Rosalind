
with open('input/rosalind_mrna.txt') as f: 
    file = f.readlines()
    
proteinstring = [x.strip() for x in file][0]

f.close()

### START CODE ###
mappingcount = {
'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2,
'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6, 
'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 
'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2,
}

number = 1
for i in range(len(proteinstring)): 
    number *= mappingcount[proteinstring[i]]
number *= 3 # For stop codon
number %= 1000000
### END CODE ###

with open('output/rosalind_mrna_output.txt', 'w') as f: 
    f.write(str(number))
    
f.close()
