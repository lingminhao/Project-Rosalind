with open('rosalind_ba5h.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
v = Text[0]
w = Text[1]

def Sumofweight(v,w): 
    sumofweight = []
    for i in range(len(v)+1): 
        sumofweight.append([0]*(len(w)+1))
        
    for i in range(len(sumofweight[0])): 
        sumofweight[0][i] = i*-1
    
    backtrack = []
    for i in range(len(v)+1): 
        backtrack.append([0]*(len(w)+1))
    for i in range(len(backtrack[0])):
        backtrack[0][i] = 'blue'
    backtrack[0][0] = 0 
    
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1): 
            if v[i-1] == w[j-1]: 
                A = sumofweight[i-1][j-1] + 1
            elif v[i-1] != w[j-1]: 
                A = sumofweight[i-1][j-1] - 1
            
            
            if j == len(w): 
                sumofweight[i][j] = max(sumofweight[i][j-1]-1, A)
                if sumofweight[i][j] == sumofweight[i][j-1] - 1: 
                    backtrack[i][j] = 'blue'
                elif sumofweight[i][j] == sumofweight[i-1][j-1] + 1: 
                    backtrack[i][j] = 'red'
                elif sumofweight[i][j] == sumofweight[i-1][j-1] - 1: 
                    backtrack[i][j] = 'purple'
                
            else: 
                sumofweight[i][j] = max(sumofweight[i][j-1]-1, A, sumofweight[i-1][j] - 1)
                if sumofweight[i][j] == sumofweight[i][j-1] - 1: 
                    backtrack[i][j] = 'blue'
                elif sumofweight[i][j] == sumofweight[i-1][j] - 1: 
                    backtrack[i][j] = 'green'
                elif sumofweight[i][j] == sumofweight[i-1][j-1] + 1: 
                    backtrack[i][j] = 'red'
                elif sumofweight[i][j] == sumofweight[i-1][j-1] - 1: 
                    backtrack[i][j] = 'purple'
    
    
    maximum = -999999999999999
    for i in range(len(v)+1): 
        if maximum <= sumofweight[i][len(w)]: 
            maximum = sumofweight[i][len(w)]
            startingpoint = i
    sumofweight[len(v)][len(w)] = maximum
    
    return [sumofweight, backtrack, startingpoint]

def Backtrack(v,w): 
    Backtrack = Sumofweight(v,w)[1]
    
    string1 = []
    string2 = []
    a = Sumofweight(v,w)[2]
    b = len(w)
    while b != 0:
        if Backtrack[a][b] == 'red' or Backtrack[a][b] == 'purple':
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


print(Sumofweight(v,w)[0][-1][-1])   
for item in Backtrack(v,w):
    print(item)

    










