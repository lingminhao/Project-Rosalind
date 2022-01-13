import re
with open('rosalind_ba6h.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
Text = re.findall('\([^);]*\)',Text[0])  # Everything except #
f.close()

TextD = []
for item in Text: 
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
Text = TextD[:]

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

    


ColoredEdge = ColoredEdges(Text)
ColoredEdge = [str(tuple(ColoredEdge[i])) for i in range(len(ColoredEdge))]
ColoredEdge = ', '.join(ColoredEdge)
with open('rosalind_ba6h_output.txt','w') as f: 
    f.write(ColoredEdge)
f.close()