with open('input/rosalind_revc.txt') as f: 
    file = f.readlines()

DNAstring = [x.strip() for x in file][0]

f.close()

### START CODE HERE ###
DNAstring = list(DNAstring)

ComplementDNAstring = []
for char in DNAstring:
    if char == 'A':
        char = 'T'
        ComplementDNAstring.append(char)
    elif char == 'T':
        char = 'A'
        ComplementDNAstring.append(char)
    elif char == 'G':
        char = 'C'
        ComplementDNAstring.append(char)
    elif char == 'C':
        char = 'G'
        ComplementDNAstring.append(char)
ReverseComplementDNAstring = ComplementDNAstring[:] #copy a new list
for i in range(len(ComplementDNAstring)):
    ReverseComplementDNAstring[i] = ComplementDNAstring[len(ComplementDNAstring)-1-i]
ReverseComplementDNAstring = ''.join(ReverseComplementDNAstring)
### END CODE HERE ###

with open('output/rosalind_revc_output.txt','w') as f: 
    f.write(ReverseComplementDNAstring)

f.close()

