with open('rosalind_ba5b.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]



n = int(Text[0].split(' ')[0])
m = int(Text[0].split(' ')[1])

Down = []
for i in range(1,Text.index('-')):
    A = [int(i) for i in Text[i].split(' ')]
    Down.append(A)


Right = []
for i in range(Text.index('-')+1,len(Text)):
    A = [int(i) for i in Text[i].split(' ')]
    Right.append(A)

def ManhattanTourist(n,m,Down,Right): 
    sumofweight = []
    for i in range(n+1):
        sumofweight.append([0]*(m+1))
    
    for i in range(1,n+1): 
        sumofweight[i][0] = sumofweight[i-1][0] + Down[i-1][0]
    for j in range(1,m+1): 
        sumofweight[0][j] = sumofweight[0][j-1] + Right[0][j-1]
    for i in range(1,n+1): 
        for j in range(1,m+1):
            sumofweight[i][j] = max(sumofweight[i-1][j]+Down[i-1][j],sumofweight[i][j-1]+Right[i][j-1])
    return sumofweight[n][m]


print(ManhattanTourist(n,m,Down,Right))