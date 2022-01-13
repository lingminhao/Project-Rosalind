import re
with open('rosalind_ba6c.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]

for i in range(len(Text)):
    Text[i] = re.findall('\([^);]*\)',Text[i])  # Everything except #
f.close()

lst = []
for i in range(len(Text)):
    TextD = []
    for item in Text[i]: 
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
    
Genome1 = lst[0]
Genome2 = lst[1]

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

def ColoredEdges(P): 
    Edges = []
    for Chromosome in P: 
        Nodes = ChromosometoCycle(Chromosome)
        Nodes.append(Nodes[0])
        for j in range(len(Chromosome)): 
            Edges.append([Nodes[2*j+1],Nodes[2*j+2]])
    return Edges

#BA6C#
def Cycles(Genome1,Genome2): 
    GraphGenome1 = ColoredEdges(Genome1)
    GraphGenome2 = ColoredEdges(Genome2)
    BPGraph = GraphGenome1 + GraphGenome2 
    count = 0
    while BPGraph != []: 
        while BPGraph[0][0] != BPGraph[0][-1]: 
            for i in range(1,len(BPGraph)): 
                if BPGraph[i][0] == BPGraph[0][-1]: 
                    BPGraph[0].append(BPGraph[i][1])
                    BPGraph.remove(BPGraph[i])
                    break
                elif BPGraph[i][1] == BPGraph[0][-1]: 
                    BPGraph[0].append(BPGraph[i][0])
                    BPGraph.remove(BPGraph[i])
                    break      
        BPGraph.remove(BPGraph[0])
        count = count + 1
    return count

def Blocks(Genome1,Genome2):
    GraphGenome1 = ColoredEdges(Genome1)
    return len(GraphGenome1)

twobreakdistance = Blocks(Genome1,Genome2) - Cycles(Genome1,Genome2)

with open('rosalind_ba6c_output.txt','w') as f: 
    f.write(str(twobreakdistance))
f.close()





