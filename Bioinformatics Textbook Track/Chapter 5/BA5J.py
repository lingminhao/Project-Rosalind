from Bio.SubsMat import MatrixInfo
matrix = MatrixInfo.blosum62

with open('practice.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
v = Text[0]
w = Text[1]


def Backtrack(v,w): 
    lower = []
    for i in range(len(v)+1): 
        lower.append([0]*(len(w)+1))
    
    upper = []
    for i in range(len(v)+1): 
        upper.append([0]*(len(w)+1))
    
    middle = []
    for i in range(len(v)+1): 
        middle.append([0]*(len(w)+1))

### For [0][j] and [i][0] ###    
    for j in range(1,len(middle[0])): 
        upper[0][j] = -11 + (j-1)*-1
        middle[0][j] = upper[0][j] 
    for i in range(1,len(middle)): 
        lower[i][0] = -11 + (i-1)*-1
        middle[i][0] = lower[i][0]

### For [1][1] ###
    
    lower[1][1] = middle[0][1] - 11
    upper[1][1] = middle[1][0] - 11
    
    if (v[0],w[0]) in matrix: 
        middle[1][1] = max(middle[0][0] + matrix[(v[0],w[0])], lower[1][1], upper[1][1])
    elif (w[0],v[0]) in matrix: 
        middle[1][1] = max(middle[0][0] + matrix[(w[0],v[0])], lower[1][1], upper[1][1])
    
### For [1][j] ###
        
    for j in range(2,len(middle[1])):        
        lower[1][j] = middle[0][j] - 11
        upper[1][j] = max(upper[1][j-1] - 1, middle[1][j-1] - 11)
        
        if (v[0],w[j-1]) in matrix: 
            middle[1][j] = max(middle[0][j-1] + matrix[(v[0],w[j-1])], lower[1][j], upper[1][j])
        elif (w[j-1],v[0]) in matrix: 
            middle[1][j] = max(middle[0][j-1] + matrix[(w[j-1],v[0])], lower[1][j], upper[1][j])
    
### For [i][1] ###
    
    for i in range(2,len(middle)):
        lower[i][1] = max(lower[i-1][1] - 1, middle[i-1][1] - 11)
        upper[i][1] = middle[i][0] - 11

        if (v[i-1],w[0]) in matrix: 
            middle[i][1] = max(middle[i-1][0] + matrix[(v[i-1],w[0])], lower[i][1], upper[i][1])
        elif (w[0],v[i-1]) in matrix: 
            middle[i][1] = max(middle[0][j-1] + matrix[(w[0],v[i-1])], lower[i][1], upper[i][1])
        
### For other entries ###
    for i in range(2,len(v)+1): 
        for j in range(2,len(w)+1): 
            lower[i][j] = max(lower[i-1][j] - 1, middle[i-1][j] - 11)
            upper[i][j] = max(upper[i][j-1] - 1, middle[i][j-1] - 11)
            if (v[i-1],w[j-1]) in matrix: 
                middle[i][j] = max(middle[i-1][j-1] + matrix[(v[i-1],w[j-1])], lower[i][j], upper[i][j])
            elif (w[j-1],v[i-1]) in matrix: 
                middle[i][j] = max(middle[i-1][j-1] + matrix[(w[j-1],v[i-1])], lower[i][j], upper[i][j])
    backtrack = []
    for i in range(len(v)+1): 
        backtrack.append([0]*(len(w)+1))
    
    a = len(v)
    b = len(w)
    string1 = []
    string2 = []
    while a!=0 or b!=0:
        if a == 0: 
            backtrack[a][b] = 'blue'
        elif b == 0: 
            backtrack[a][b] = 'green'
        else: 
            if middle[a][b] == lower[a][b]:
                backtrack[a][b] = 'green'
            elif middle[a][b] == upper[a][b]: 
                backtrack[a][b] = 'blue' 
            else: 
                backtrack[a][b] = 'red'

        if backtrack[a][b] == 'red': 
            string1.append(v[a-1])
            string2.append(w[b-1])
            a = a-1
            b = b-1
        elif backtrack[a][b] == 'green': 
            string1.append(v[a-1])
            string2.append('-')
            a = a-1
        elif backtrack[a][b] == 'blue': 
            string1.append('-')
            string2.append(w[b-1])
            b = b-1
    string1.reverse()
    string2.reverse()
    bestscore = middle[len(v)][len(w)]
    return [backtrack, bestscore,''.join(string1),''.join(string2)]

print(Backtrack(v,w)[1])
print(Backtrack(v,w)[2])
print(Backtrack(v,w)[3])




