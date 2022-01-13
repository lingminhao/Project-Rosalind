with open('input/rosalind_rna.txt') as f: 
    file = f.readlines()

DNAstring = file[0].strip()

f.close()

### START CODE ###
RNAstring = ''
for char in DNAstring:
    if char == 'T':
        char = 'U'
        RNAstring += char
    else: RNAstring +=char
### END CODE ###    

with open('output/rosalind_rna_output.txt','w') as f: 
    f.write(RNAstring)

f.close()
