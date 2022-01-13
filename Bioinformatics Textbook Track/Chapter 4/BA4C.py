from C4f import Cyclospectrum
from C4f import PeptidetoIM
with open('rosalind_ba4c.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
Peptide = Text[0]

Peptide = PeptidetoIM(Peptide)
for i in Cyclospectrum(Peptide):
    print(i)