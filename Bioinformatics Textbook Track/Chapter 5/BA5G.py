## To find edit distance is equivalent to Global Alignment Problem (match + 1, mismatch indel -1). Maximising the score = minimising the number of edits required. ##

with open('rosalind_ba5g.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
v = Text[0]
w = Text[1]

def SumofWeight(v,w): 
    sumofweight = []
    for i in range(len(v)+1): 
        sumofweight.append([0]*(len(w)+1))
    
    sumofweight[0] = [i*1 for i in range(len(sumofweight[0]))]
    for i in range(len(sumofweight)): 
        sumofweight[i][0] = i*1
    backtrack = []
    for i in range(len(v)+1): 
        backtrack.append([0]*(len(w)+1))
    backtrack[0] = ['blue' for item in backtrack[0]]
    for item in backtrack: 
        item[0] = 'green'
    backtrack[0][0] = 0
    for i in range(1,len(v)+1): 
        for j in range(1,len(w)+1):
            if v[i-1] == w[j-1]:
                A = sumofweight[i-1][j-1]
            if v[i-1] != w[j-1]: 
                A = sumofweight[i-1][j-1] + 1
            sumofweight[i][j] = min(sumofweight[i-1][j] + 1, sumofweight[i][j-1] + 1, A)
            
            if sumofweight[i][j] == sumofweight[i-1][j] + 1: 
                backtrack[i][j] = 'green'
            elif sumofweight[i][j] == sumofweight[i][j-1] + 1: 
                backtrack[i][j] = 'blue'
            elif sumofweight[i][j] == sumofweight[i-1][j-1]: 
                backtrack[i][j] = 'red'
            elif sumofweight[i][j] == sumofweight[i-1][j-1] + 1: 
                backtrack[i][j] = 'purple'
    return backtrack

def Backtrack(v,w): 
    backtrack = SumofWeight(v,w)
    string1 = []
    string2 = []
    a = len(v)
    b = len(w) 
    while a != 0 or b != 0:
        if backtrack[a][b] == 'red'or backtrack[a][b] == 'purple': 
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
    
    return [''.join(string1), ''.join(string2)]

string1 = Backtrack(v,w)[0]
string2 = Backtrack(v,w)[1]
count = 0
for i in range(len(string1)):
        if string1[i] != string2[i]: 
            count = count + 1
print(count)