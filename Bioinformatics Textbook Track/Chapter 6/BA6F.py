with open('rosalind_ba6f.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
Text = Text[0].split(' ')
Text[0] = Text[0].split('(')
Text[0] = Text[0][-1]
Text[-1] = Text[-1].split(')')
Text[-1] = Text[-1][0]
for i in range(len(Text)): 
    if Text[i][0] == '-' : 
        Text[i] = -int(Text[i][1:])
    else: 
        Text[i] = int(Text[i][1:])
f.close()

#BA6F#
def ChromosometoCycle(Chromosome): 
    Node = []
    for j in range(len(Chromosome)):
        i = Chromosome[j]
        if i > 0:
            Node.append(2*i-1)
            Node.append(2*i)
        else: 
            Node.append(-2*i)
            Node.append(-2*i-1)
    return Node


with open('rosalind_ba6f_output.txt','w') as f: 
    f.write('(')
    for item in ChromosometoCycle(Text):
        f.write(str(item))
        if item != ChromosometoCycle(Text)[-1]:
            f.write(' ')
    f.write(')')
f.close()