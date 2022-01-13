from Bio.SubsMat import MatrixInfo
matrix = MatrixInfo.blosum62
with open('practice.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]

v = list(Text[0])
w = list(Text[1])

def Sumofweight(v,w): 
    sumofweight = []
    for i in range(len(v)+1): 
        sumofweight.append([-5]*(len(w)+1))
    sumofweight[0][0] = 0
    
    sumofweight[0] = [i*-5 for i in range(len(sumofweight[0]))]
    for i in range(len(sumofweight)): 
        sumofweight[i][0] = i*-5

    
    backtrack = []
    for i in range(len(v)+1): 
        backtrack.append([0]*(len(w)+1))
    backtrack[0] = ['blue' for item in backtrack[0]]
    for item in backtrack: 
        item[0] = 'green'
    backtrack[0][0] = 0
    
    for i in range(1,len(v)+1): 
        for j in range(1,len(w)+1):
            A = -9999
            if (v[i-1],w[j-1]) in matrix: 
                A = sumofweight[i-1][j-1] + matrix[(v[i-1],w[j-1])]
            elif (w[j-1],v[i-1]) in matrix: 
                A = sumofweight[i-1][j-1] + matrix[(w[j-1],v[i-1])]      
                    
            sumofweight[i][j] = max(sumofweight[i-1][j]-5, sumofweight[i][j-1]-5, A)
            
            if sumofweight[i][j] == sumofweight[i-1][j] - 5: 
                backtrack[i][j] = 'green'
            elif sumofweight[i][j] == sumofweight[i][j-1] - 5: 
                backtrack[i][j] = 'blue'
            elif sumofweight[i][j] == A: 
                backtrack[i][j] = 'red'
    return [backtrack, sumofweight]

def Backtrack(v,w): 
    Backtrack = Sumofweight(v,w)[0]
    
    string1 = []
    string2 = []
    a = len(v)
    b = len(w)
    while a != 0 or b != 0:
        if Backtrack[a][b] == 'red':
            string1.append(v[a-1])
            string2.append(w[b-1])
            a = a-1
            b = b-1
        elif Backtrack[a][b] == 'green': 
            string1.append(v[a-1])
            string2.append('-')
            a = a-1
        elif Backtrack[a][b] == 'blue': 
            string1.append('-')
            string2.append(w[b-1])
            b = b-1
    string1.reverse()
    string2.reverse()
    
    return [''.join(string1), ''.join(string2)]


print(Sumofweight(v,w)[1][-1][-1])
for item in Backtrack(v,w):
    print(item)