with open('rosalind_ba6g.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
Text = Text[0].split(' ')
Text[0] = Text[0].split('(')
Text[0] = Text[0][-1]
Text[-1] = Text[-1].split(')')
Text[-1] = Text[-1][0]

Text = [int(x) for x in Text]
f.close()

#BA6G#
def CycletoChromosome(Nodes):
    Chromosome = []
    for i in range(int(len(Nodes)/2)): 
        if Nodes[2*i+1] > Nodes[2*i]: 
            Chromosome.append(int(Nodes[2*i+1]/2))
        else: 
            Chromosome.append(int(-Nodes[2*i]/2))
    
    for i in range(len(Chromosome)): 
        if Chromosome[i] > 0: 
            Chromosome[i] = '+' + str(Chromosome[i])
        else: Chromosome[i] = str(Chromosome[i])
    Chromosome = '(' + ' '.join(Chromosome) + ')'
    return Chromosome

with open('rosalind_ba6g_output.txt','w') as f: 
    f.write(str(CycletoChromosome(Text)))
f.close()