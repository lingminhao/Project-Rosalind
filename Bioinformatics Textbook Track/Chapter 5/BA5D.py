import re
with open('rosalind_ba5d.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
source = int(Text[0])
sink = int(Text[1])
edge = []
node = []
weight = []
for i in range(2,len(Text)): 
    num1 = int(re.findall('([0-9]+)->[^ ]+',Text[i])[0])
    num2 = int(re.findall('[0-9]+->([0-9]+):[0-9]+',Text[i])[0])
    num3 = int(re.findall('[0-9]+->[0-9]+:([0-9]+)',Text[i])[0])
    edge.append((num1,num2))
    weight.append(num3)
    if num1 not in node: 
        node.append(num1)
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

def Longestpath(edge,node,weight,source,sink):
    EDGE = edge[:]
    
    ### This clears all the nodes with indegree 0 except the source ###
    setofindegree0 = [0]
    while setofindegree0 != []: 
        nodeD = []
        edgeD = edge[:]
        setofindegree0 = []
        for i in range(len(edge)): 
            if edge[i][1] not in nodeD: 
                nodeD.append(edge[i][1])
        for item in node: 
            if item not in nodeD: 
                setofindegree0.append(item)
        if source in setofindegree0: 
            setofindegree0.remove(source)
        for i in range(len(setofindegree0)): 
            for j in range(len(edge)): 
                if setofindegree0[i] == edge[j][0]: 
                        edgeD.remove(edge[j])
        edge = edgeD[:]
        if source not in nodeD: 
            nodeD.append(source)
        node = nodeD[:]
    
    weightD = []
    for item in edge: 
        index = EDGE.index(item)
        weightD.append(weight[index])
    weight = weightD[:]
    
    #####################################################################
    
    
    topologysort = [int(i) for i in TopologySort(edge, node).split(',')]
    
    longestpath = [-1]*len(topologysort)
    longestpath[0] = 0
    lst = [[source]]*len(topologysort)
    for i in range(1,len(topologysort)): 
        nodes = topologysort[i]
        
        predecessor = []
        localweight = []
        for j in range(len(edge)): 
            if nodes == edge[j][1]: 
                predecessor.append(edge[j][0])
                localweight.append(weight[j])
        for j in range(len(predecessor)): 
            if longestpath[i] <= longestpath[topologysort.index(predecessor[j])] + localweight[j]:
                longestpath[i] = longestpath[topologysort.index(predecessor[j])] + localweight[j]
                lst[i] = []
                for item in lst[topologysort.index(predecessor[j])]: 
                    lst[i].append(item)
        lst[i].append(nodes)
    
    path = str(lst[topologysort.index(sink)][0])
    for i in range(1,len(lst[topologysort.index(sink)])):
        path = path + '->' + str(lst[topologysort.index(sink)][i])
    
    return {'Longest Path Total Weight': longestpath[topologysort.index(sink)], 'The path is': path}

print(Longestpath(edge,node,weight,source,sink))








