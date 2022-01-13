from C4f import ProteinTranslation
with open('rosalind_ba4a.txt') as f: 
    Text = f.readlines()
Pattern = Text[0]
print(ProteinTranslation(Pattern))