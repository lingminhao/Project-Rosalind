import re
with open('rosalind_ba6j.txt') as f: 
    Text = f.readlines()
f.close()
Text = [x.strip() for x in Text]
indices = [int(x) for x in Text[1].split(', ')]
ColoredEdge = re.findall('\([^);]*\)',Text[0])

for i in range(len(ColoredEdge)): 
    ColoredEdge[i] = ColoredEdge[i].split(', ')
    ColoredEdge[i][0] = ColoredEdge[i][0][1:]
    ColoredEdge[i][-1] = ColoredEdge[i][-1][0:-1]
    ColoredEdge[i] = [int(x) for x in ColoredEdge[i]]

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

#BA6J    
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

NewGenomeGraph = twobreakOnGenomeGraph(GenomeGraph(ColoredEdge),indices) # A process to delete 2 edges and add 2 new edges. 
NewColoredEdge = []
for item in NewGenomeGraph: 
    itemD = item[:]
    itemD.remove(item[0])
    itemD.remove(item[-1])
    for i in range(int(len(itemD)/2)): 
        NewColoredEdge.append([itemD[2*i],itemD[2*i+1]])
    NewColoredEdge.append([item[-1],item[0]])

for i in range(len(NewColoredEdge)): 
    NewColoredEdge[i] = str(tuple(NewColoredEdge[i]))

with open('rosalind_ba6j_output.txt','w') as f: 
    f.write(', '.join(NewColoredEdge))
f.close()