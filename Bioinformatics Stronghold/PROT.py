with open('input/rosalind_prot.txt') as f: 
    file = f.readlines()
RNAstring = [x.strip() for x in file][0]
f.close()

### START CODE HERE ###
amino_code = {'UUU': 'F',     'CUU': 'L', 'AUU': 'I','GUU':'V',
'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
'UAA': '',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
'UAG': '',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
'UGA': '',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'}

lst = []
lst2 = []
for i in range(int(len(RNAstring)/3)):
    lst.append(RNAstring[3*i:3*i+3])
for code in lst:
    for key in amino_code.keys():
        if key==code:
            lst2.append(amino_code[key])
        else: continue
PROTstring = ''.join(lst2)
### END CODE HERE ###

with open('output/rosalind_prot_output.txt', 'w') as f: 
    f.write(PROTstring)
    
f.close()