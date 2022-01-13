from C4f import DNAtoRNA
from C4f import RNAtoDNA
from C4f import ProteinTranslation
from C4f import ReverseComplement


with open('rosalind_ba4b.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]

DNAstring = Text[0]
Amino = Text[1]

k = 3*len(Amino)
lst = []

for i in range(len(DNAstring)-k+1):
    substring = DNAstring[i:i+k]
    RCsubstring = ReverseComplement(substring)
    
    RNAsubstring = DNAtoRNA(substring)
    RNARCsubstring = DNAtoRNA(RCsubstring)
    if ProteinTranslation(RNAsubstring) == Amino: 
        lst.append(RNAtoDNA(RNAsubstring))
    elif ProteinTranslation(RNARCsubstring) == Amino: 
        lst.append(RNAtoDNA(RNAsubstring))

for i in lst: print(i)