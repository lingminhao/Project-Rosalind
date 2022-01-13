import numpy as  np
with open('rosalind_ba5m.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]

x = Text[0]
y = Text[1]
z = Text[2]

def Sumofweight(x,y,z):
    sumofweight = np.zeros((len(x)+1,len(y)+1,len(z)+1))
    backtrack = np.full((len(x)+1,len(y)+1,len(z)+1),'c',dtype = str)
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1): 
            for k in range(1,len(z)+1): 
                if x[i-1] == y[j-1] == z[k-1]: 
                    A = sumofweight[i-1,j-1,k-1] + 1
                else: 
                    A = sumofweight[i-1,j-1,k-1]
                sumofweight[i,j,k] = max(sumofweight[i-1,j,k],sumofweight[i,j-1,k],
                        sumofweight[i,j,k-1],sumofweight[i-1,j-1,k],sumofweight[i-1,j,k-1],
                        sumofweight[i,j-1,k-1],A)
                
                if sumofweight[i,j,k] == sumofweight[i-1,j,k]:
                    backtrack[i,j,k] = '1'
                elif sumofweight[i,j,k] == sumofweight[i,j-1,k]: 
                    backtrack[i,j,k] = '2'
                elif sumofweight[i,j,k] == sumofweight[i,j,k-1] : 
                    backtrack[i,j,k] = '3'
                elif sumofweight[i,j,k] == sumofweight[i-1,j-1,k]: 
                    backtrack[i,j,k] = '4'
                elif sumofweight[i,j,k] == sumofweight[i-1,j,k-1] : 
                    backtrack[i,j,k] = '5'
                elif sumofweight[i,j,k] == sumofweight[i,j-1,k-1]: 
                    backtrack[i,j,k] = '6'
                elif sumofweight[i,j,k] == sumofweight[i-1,j-1,k-1] + 1: 
                    backtrack[i,j,k] = '7'
                elif sumofweight[i,j,k] == sumofweight[i-1,j-1,k-1]: 
                    backtrack[i,j,k] = '8'
                    
    # Case for one zero #
    for i in range(1,len(x)+1): 
        for j in range(1,len(y)+1):
            backtrack[i,j,0] = '1'        
    for j in range(1,len(y)+1):
        for k in range(1,len(z)+1): 
            backtrack[0,j,k] = '2'
    for i in range(1,len(x)+1): 
        for k in range(1,len(z)+1): 
            backtrack[i,0,k] = '3'
    
    # Case for two zeroes #
    for i in range(1,len(x)+1): 
        backtrack[i,0,0] = '1'
    for j in range(1,len(y)+1): 
        backtrack[0,j,0] = '2'
    for k in range(1,len(z)+1): 
        backtrack[0,0,k] = '3'
    
    return (backtrack,int(sumofweight[len(x),len(y),len(z)]))

def Backtrack(x,y,z):
    backtrack = Sumofweight(x,y,z)[0]
    string1 = ''
    string2 = ''
    string3 = ''
    a = len(x)
    b = len(y)
    c = len(z)
    while a != 0 or b != 0 or c!=0:
        if backtrack[a,b,c] == '8' or backtrack[a,b,c] == '7':
            string1 += x[a-1]
            string2 += y[b-1]
            string3 += z[c-1]
            a = a-1
            b = b-1
            c = c-1
        elif backtrack[a,b,c] == '1': 
            string1 += x[a-1]
            string2 += '-'
            string3 += '-'
            a = a-1
        elif backtrack[a,b,c] == '2':
            string1 += '-'
            string2 += y[b-1]
            string3 += '-'
            b = b-1
        elif backtrack[a,b,c] == '3':
            string1 += '-'
            string2 += '-'
            string3 += z[c-1]
            c = c-1
        elif backtrack[a,b,c] == '4':
            string1 += x[a-1]
            string2 += y[b-1]
            string3 += '-'
            a = a-1
            b = b-1
        elif backtrack[a,b,c] == '5':
            string1 += x[a-1]
            string2 += '-'
            string3 += z[c-1]
            a = a-1
            c = c-1
        elif backtrack[a,b,c] == '6':
            string1 += '-'
            string2 += y[b-1]
            string3 += z[c-1]
            b = b-1
            c = c-1
    string1 = string1[::-1]
    string2 = string2[::-1]
    string3 = string3[::-1]
    return (string1,string2,string3)

print(Sumofweight(x,y,z)[1])
for item in Backtrack(x,y,z): 
    print(item)
