import re
Paths = []

with open('practice.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
A = dict()
for i in range(len(Text)):
    key = re.findall('([0-9]+) -> [^ ]+',Text[i])[0]
    if key not in List: 
        List.append(key)
    values = re.findall('[0-9]+ -> ([^ ]+)',Text[i])[0]
    values = values.split(',')
    A[key] = values
List = list(A.keys())
print(A)
print(List)
def indegree(A,node): 
    indeg = 0
    for key in A: 
        for i in range(len(A[key])):
            if node == A[key][i]: 
                indeg = indeg + 1
    return indeg

def outdegree(A,node):
    outdeg = 0
    if node in A:
        for j in range(len(A[node])):
            outdeg = outdeg + 1
    return outdeg

for i in range(len(List)): 
    node = List[i]
    NonBranchingPathList = [node]
    if indegree(A,node) != 1 or outdegree(A,node) != 1: 
        if outdegree(A,node) > 0: 
            edgelist = A[node]
            for j in range(len(edgelist)): 
                nextnode = edgelist[j]
                NonBranchingPathList = [node]
                NonBranchingPathList.append(nextnode)
                while indegree(A,nextnode) == 1 and outdegree(A,nextnode) == 1: 
                    nextnextnode = A[nextnode][0]
                    NonBranchingPathList.append(nextnextnode[0])
                    nextnode = nextnextnode[0]
                NonBranchingPath = NonBranchingPathList[0]
                for k in range(1,len(NonBranchingPathList)): 
                    NonBranchingPath = NonBranchingPath + ' -> ' + NonBranchingPathList[k]
                Paths.append(NonBranchingPath)

print(Paths)



















                
#    while indegree(A,node) == 1 and outdegree(A,node) == 1: 
#        nextnode = A[node][0]
#        if nextnode in NonBranchingPathList:
#            NonBranchingPathList.append(nextnode[0])
#            NonBranchingPath = NonBranchingPathList[0]
#            for k in range(1,len(NonBranchingPathList)): 
#                NonBranchingPath = NonBranchingPath + ' -> ' + NonBranchingPathList[k]
#            Paths.append(NonBranchingPath)
#        else: 
#            NonBranchingPathList.append(nextnode)
#            node = nextnode
#
#print(Paths)



























#B = copy.deepcopy(A)
#C = copy.deepcopy(A)
#for i in range(len(List)):
#    node = List[i]
#    NonBranchingPathList = [node]
#    reset = NonBranchingPathList
#    if indegree(B,node)!= 1 or outdegree(B,node)!= 1: 
#
#        if outdegree(B,node) > 0 : 
#            for j in range(len(B[node])):
#                NonBranchingPathList = reset[:]
#                NonBranchingPathList.append(B[node][j])
#                node = B[node][j]
#                print(node)
#                while indegree(B, node) == 1 and outdegree(B, node) == 1: 
#                    NonBranchingPathList.append(B[node][0])
#                    node = B[node][0]
#                    
#                NonBranchingPath = NonBranchingPathList[0]
#                for i in range(1,len(NonBranchingPathList)):
#                    NonBranchingPath = NonBranchingPath + ' -> ' + NonBranchingPathList[i]
#                Paths.append(NonBranchingPath)
#    else: 
#        while indegree(C,node) == 1 and outdegree(C,node) == 1: 
#            if C[node][0] in NonBranchingPathList: 
#                NonBranchingPath = NonBranchingPathList[0]
#                for i in range(1,len(NonBranchingPathList)):
#                    NonBranchingPath = NonBranchingPath + ' -> ' + NonBranchingPathList[i]
#                    List = ['A' if x == NonBranchingPathList[i] else x for x in List]
#                NonBranchingPath = NonBranchingPath + ' -> ' + NonBranchingPathList[0]
#                Paths.append(NonBranchingPath)
#                break 
#            NonBranchingPathList.append(C[node][0])
#            node = C[node][0]
#print(Paths)






