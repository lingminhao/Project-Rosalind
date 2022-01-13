import re
with open('rosalind_ba6d.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]

for i in range(len(Text)):
    Text[i] = re.findall('\([^);]*\)',Text[i])  # Everything except #
f.close()

def ListGenome(Genome):
    lst = []
    TextD = []
    for item in Genome: 
        item = item.split(' ')
        item[0] = item[0].split('(')
        item[0] = item[0][-1]
        item[-1] = item[-1].split(')')
        item[-1] = item[-1][0]
        for i in range(len(item)): 
            if item[i][0] == '-' : 
                item[i] = -int(item[i][1:])
            else: 
                item[i] = int(item[i][1:])
        TextD.append(item)
    lst.append(TextD)
    return lst

def BreakpointGraph(RedEdges,BlueEdges): 
    BPGraph = RedEdges + BlueEdges 
    lst = []
    while BPGraph != []: 
        while BPGraph[0][0] != BPGraph[0][-1]: 
            for i in range(1,len(BPGraph)): 
                if BPGraph[i][0] == BPGraph[0][-1]: 
                    BPGraph[0] = BPGraph[0] + [BPGraph[i][1]]
                    BPGraph.remove(BPGraph[i])
                    break
                elif BPGraph[i][1] == BPGraph[0][-1]: 
                    BPGraph[0] = BPGraph[0] + [BPGraph[i][0]]
                    BPGraph.remove(BPGraph[i])
                    
                    break  
        BPGraph[0] = BPGraph[0][0:-1]
        lst.append(BPGraph[0])
        BPGraph.remove(BPGraph[0])
    return lst

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

#BA6H
def ColoredEdges(P): 
    Edges = []
    for Chromosome in P: 
        Nodes = ChromosometoCycle(Chromosome)
        Nodes.append(Nodes[0])
        for j in range(len(Chromosome)): 
            Edges.append([Nodes[2*j+1],Nodes[2*j+2]])
    return Edges

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
    GenomeGraph = [] 
    
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
            GenomeGraph.append(Combined[0][0:-1])
            Combined.remove(Combined[0])
    return GenomeGraph

def twobreakOnGenomeGraph(GenomeGraphs,indices):
    ColoredEdge = []
    for item in GenomeGraphs: 
        itemD = item[:]
        itemD.remove(item[0])
        itemD.remove(item[-1])
        for i in range(int(len(itemD)/2)): 
            ColoredEdge.append([itemD[2*i],itemD[2*i+1]])
        ColoredEdge.append([item[-1],item[0]])
    if [indices[0],indices[1]] in ColoredEdge: 
        ColoredEdge.remove([indices[0],indices[1]])
    else: 
        ColoredEdge.remove([indices[1],indices[0]])
        
    if [indices[2],indices[3]] in ColoredEdge: 
        ColoredEdge.remove([indices[2],indices[3]])
    else: 
        ColoredEdge.remove([indices[3],indices[2]])     
    ColoredEdge.append([indices[0],indices[2]])
    ColoredEdge.append([indices[1],indices[3]])
    GenomeGraphs = GenomeGraph(ColoredEdge)
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

def twoBreakOnGenome(Genome,indices): 
    ColoredEdge = ColoredEdges(Genome)
    GenomeGraphs = GenomeGraph(ColoredEdge)
    GenomeGraphs = twobreakOnGenomeGraph(GenomeGraphs,indices)
    Genome = GraphtoGenome(GenomeGraphs)
    return Genome

Genome1 = ListGenome(Text[0])[0]
Genome2 = ListGenome(Text[1])[0]

def ShortestRearrangementScenario(Genome1,Genome2): 
    lst = [Text[0][0]]
    RedEdges = ColoredEdges(Genome1)
    BlueEdges = ColoredEdges(Genome2)
    BreakpointGraphs = BreakpointGraph(RedEdges,BlueEdges)
    
    while all(len(item) == 2 for item in BreakpointGraphs) == False:
        for item in BreakpointGraphs: 
            if len(item)!=2: 
                Nontrivialredblue = item
                break
            
        rededge1 = Nontrivialredblue[0:2]
        rededge2 = Nontrivialredblue[2:4]
    
        if rededge1 in RedEdges: 
            RedEdges.remove(rededge1)
        else: 
            rededge1.reverse()
            RedEdges.remove(rededge1)
            rededge1.reverse()
        
        if rededge2 in RedEdges: 
            RedEdges.remove(rededge2)
        else: 
            rededge2.reverse()
            RedEdges.remove(rededge2)
            rededge2.reverse()
    
        newrededge1 = [rededge1[0]] + [rededge2[1]]
        newrededge2 = [rededge1[1]] + [rededge2[0]]
        
        RedEdges.append(newrededge1)
        RedEdges.append(newrededge2)
        BreakpointGraphs = BreakpointGraph(RedEdges,BlueEdges)
        
        indices = []
        indices.append(rededge1[0])
        indices.append(rededge1[1])
        indices.append(rededge2[1])
        indices.append(rededge2[0])
        Genome1 = twoBreakOnGenome(Genome1,indices)
        lst.append(Genome1)
        
        Genome1 = re.findall('\([^);]*\)',Genome1)
        Genome1 = ListGenome(Genome1)[0]
    return lst

with open('rosalind_ba6d_output.txt','w') as f: 
    for item in ShortestRearrangementScenario(Genome1,Genome2): 
        f.write(item)
        f.write('\n')
f.close()