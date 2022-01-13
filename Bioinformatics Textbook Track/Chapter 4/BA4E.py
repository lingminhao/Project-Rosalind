from C4f import CycloPeptideSequencing

with open('rosalind_ba4e.txt') as f: 
    Text = f.readlines()
Text = [x.split(' ') for x in Text]
Spectrum = [int(i) for i in Text[0]]

for item in CycloPeptideSequencing(Spectrum): 
    item = [str(i) for i in item]
    print('-'.join(item))

