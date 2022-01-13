from Bio.SubsMat import MatrixInfo
matrix = MatrixInfo.pam250

with open('rosalind_ba5f.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
v = Text[0]
w = Text[1]

### Backtrack function for Local Alignment Problem ###
def Sumofweight(v,w): 
    sumofweight = []
    for i in range(len(v)+1): 
        sumofweight.append([0]*(len(w)+1))
    backtrack = []
    for i in range(len(v)+1): 
        backtrack.append(['grey']*(len(w)+1))
    
    for i in range(1,len(v)+1): 
        for j in range(1,len(w)+1):
            A = -9999            
            if (v[i-1],w[j-1]) in matrix: 
                A = sumofweight[i-1][j-1] + matrix[(v[i-1],w[j-1])]
            elif (w[j-1],v[i-1]) in matrix: 
                A = sumofweight[i-1][j-1] + matrix[(w[j-1],v[i-1])]
                    
            sumofweight[i][j] = max(sumofweight[i-1][j]-5, sumofweight[i][j-1]-5, A, 0)
            
            if sumofweight[i][j] == sumofweight[i-1][j] - 5: 
                backtrack[i][j] = 'green'
            elif sumofweight[i][j] == sumofweight[i][j-1] - 5: 
                backtrack[i][j] = 'blue'
            elif sumofweight[i][j] == A: 
                backtrack[i][j] = 'red'
            elif sumofweight[i][j] == 0: 
                backtrack[i][j] = 'grey'
    maximum = -1
    for i in range(len(v)+1): 
        for j in range(len(w)+1): 
            if maximum <= sumofweight[i][j]: 
                maximum = sumofweight[i][j]
    sumofweight[len(v)][len(w)] = maximum
    return [backtrack, sumofweight]

def Backtrack(v,w): 
    backtrack = Sumofweight(v,w)[0]
    sumofweight = Sumofweight(v,w)[1]
    string1 = []
    string2 = []
    a = len(v)
    b = len(w)
    maximum = -1
    for i in range(len(v)+1): 
        for j in range(len(w)+1): 
            if maximum <= sumofweight[i][j] and i!=len(v) and j!=len(w):
                maximum = sumofweight[i][j]
                a = i
                b = j
    
    while a != 0 or b != 0:
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
        elif backtrack[a][b] == 'grey': 
            a = 0 
            b = 0
            
    string1.reverse()
    string2.reverse()
    return [''.join(string1), ''.join(string2)]

############################################################################################
    
print(Sumofweight(v,w)[1][-1][-1])

for item in Backtrack(v,w): 
    print(item)