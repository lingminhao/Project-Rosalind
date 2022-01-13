import re
with open('rosalind_ba6i.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
Text = re.findall('\([^);]*\)',Text[0])

for i in range(len(Text)): 
    Text[i] = Text[i].split(', ')
    Text[i][0] = int(Text[i][0][1:])
    Text[i][-1] = int(Text[i][-1][0:-1])

ColoredEdge = Text[:]


## This is a code to form BlackEdge and Genome Graph##
def GenomeGraph(ColoredEdge):
    lst1 = []
    lst2 = []
    for item in ColoredEdge: 
        lst1.append(min(item))
        lst2.append(max(item))
    minimum = min(lst1)
    maximum = max(lst2)
    
    BlackEdge = []
    for i in range(int((maximum-minimum+1)/2)):
        BlackEdge.append([2*i+1,2*i+2])
    
    Combined = BlackEdge[:] + ColoredEdge[:]
    GenomeGraphs = [] 
    
    while Combined != []:     
        for i in range(1,len(Combined)):
            if Combined[i][0] == Combined[0][-1]: 
                Combined[0] = Combined[0] + [Combined[i][-1]]
                Combined.remove(Combined[i])
                break
            elif Combined[i][1] == Combined[0][-1]: 
                Combined[i].reverse()
                Combined[0] = Combined[0] + [Combined[i][-1]]
                Combined.remove(Combined[i])
                break
        if Combined[0][0] == Combined[0][-1]: 
            GenomeGraphs.append(Combined[0][0:-1])
            Combined.remove(Combined[0])
    return GenomeGraphs

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

def GraphtoGenome(GenomeGraphs):
    P = []
    for item in GenomeGraphs: 
        Chromosome = CycletoChromosome(item)
        P.append(Chromosome)
    P = ''.join(P)
    return P

GenomeGraphs = GenomeGraph(ColoredEdge)
with open('rosalind_ba6i_output.txt','w') as f: 
    f.write(GraphtoGenome(GenomeGraphs))