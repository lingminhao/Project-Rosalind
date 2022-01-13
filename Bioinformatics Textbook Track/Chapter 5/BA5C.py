with open('rosalind_ba5c.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]

v = Text[0]
w = Text[1]



def LCSBacktrack(v,w): 
    sumofweight = []
    for i in range(len(v)+1): 
        sumofweight.append([0]*(len(w)+1))
    backtrack = []
    for i in range(len(v)+1): 
        backtrack.append([0]*(len(w)+1))
    
    for i in range(1,len(v)+1): 
        for j in range(1,len(w)+1):
            A = -1
            if v[i-1] == w[j-1]:
                A = sumofweight[i-1][j-1] + 1
            sumofweight[i][j] = max(sumofweight[i-1][j], sumofweight[i][j-1], A)
            
            if sumofweight[i][j] == sumofweight[i-1][j]: 
                backtrack[i][j] = 'green'
            elif sumofweight[i][j] == sumofweight[i][j-1]: 
                backtrack[i][j] = 'blue'
            elif sumofweight[i][j] == sumofweight[i-1][j-1] + 1: 
                backtrack[i][j] = 'red'
    return backtrack

lst = []
def OutputLCS(Backtrack,v,i,j): 
    if i == 0 or j == 0: 
        return 
    if Backtrack[i][j] == 'green': 
        OutputLCS(Backtrack,v,i-1,j)
    elif Backtrack[i][j] == 'blue': 
        OutputLCS(Backtrack,v,i,j-1)
    elif Backtrack[i][j] == 'red': 
        OutputLCS(Backtrack,v,i-1,j-1)
        lst.append(v[i-1])
    return lst


Backtrack = LCSBacktrack(v,w)
Answer = OutputLCS(Backtrack,v,len(v),len(w))
Answer = ''.join(Answer)
print(Answer)
