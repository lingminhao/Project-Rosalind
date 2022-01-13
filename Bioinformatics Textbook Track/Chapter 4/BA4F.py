from C4f import Score
from C4f import PeptidetoIM
with open('rosalind_ba4f.txt') as f: 
    Text = f.readlines()
Text = [x.strip().split(' ') for x in Text]
ExpSpec = [int(i) for i in Text[1]]
Peptide = Text[0][0]
Peptide = PeptidetoIM(Peptide)

print(Score(Peptide,ExpSpec))