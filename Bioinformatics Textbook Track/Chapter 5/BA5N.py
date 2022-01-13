import re
with open('rosalind_ba5n.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text] 
#print(Text)

edge = []
node = []

for i in range(len(Text)): 
    num1 = int(re.findall('([0-9]+) -> [0-9]+',Text[i])[0])
    if num1 not in node: 
        node.append(num1)
    outcomingedge = re.findall('[0-9]+ -> ([^ ]+)',Text[i])[0].split(',')
    outcomingedge = [int(i) for i in outcomingedge]
    for num2 in outcomingedge: 
        edge.append((num1,num2))
        if num2 not in node: 
            node.append(num2)


def TopologySort(edge,node):        
    lst = []
    candidates = node[:]
    outcomingedge = []
    for i in range(len(edge)): 
        outcomingedge.append(edge[i][1])
        for num2 in outcomingedge: 
            if num2 in candidates: 
                candidates.remove(num2)
    while candidates != []: 
        nodeA = candidates[0]
        lst.append(nodeA) 
        candidates.remove(nodeA)
        node.remove(nodeA)
        edgeD = edge[:]
        for i in range(len(edge)): 
            if edge[i][0] == nodeA: 
                edgeD.remove(edge[i])
        edge = edgeD[:]
        nodeD = node[:]
        for i in range(len(edge)): 
            num2 = edge[i][1]
            if num2 in nodeD: 
                nodeD.remove(num2)
        for item in nodeD: 
            if item not in candidates: 
                candidates.append(item)
    
    if edge != []: 
        return 'the input graph is not a DAG'
    else: 
        return ', '.join([str(i) for i in lst])

print(TopologySort(edge,node))