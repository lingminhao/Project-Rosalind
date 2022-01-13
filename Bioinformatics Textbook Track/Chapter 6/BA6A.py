with open('rosalind_ba6a.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
Text = Text[0].split(' ')
Text[0] = Text[0].split('(')
Text[0] = Text[0][-1]
Text[-1] = Text[-1].split(')')
Text[-1] = Text[-1][0]
for i in range(len(Text)): 
    if Text[i][0] == '-' : 
        Text[i] = -int(Text[i][1:])
    else: 
        Text[i] = int(Text[i][1:])
f.close()

def GreedySorting(Text):
    lst = []
    for i in range(len(Text)): 
        if Text[i] != i+1:
            TextD = [abs(x) for x in Text[:]]
            index = TextD.index(abs(i+1))
            substring = Text[i:index+1]
            substring.reverse()
            substring = [-1 * x for x in substring]
            
            TextA = Text[0:i] + substring + Text[index+1:]
            lst.append(TextA)
            if TextA[i] == -(i+1):
                TextB = TextA[:]
                TextB[i] = -1 * TextA[i]
                lst.append(TextB)
                Text = TextB[:]
            else: Text = TextA[:]
            
    for i in range(len(lst)): 
        for j in range(len(lst[0])): 
            if lst[i][j] > 0 : 
                lst[i][j] = '+' + str(lst[i][j])
            else: lst[i][j] = str(lst[i][j])
    
    final = []
    for item in lst:
        final.append('(' + ' '.join(item) + ')')
    return final



with open('rosalind_ba6a_output.txt','w') as f: 
    for item in GreedySorting(Text): 
        f.write(item)
        f.write('\n')
f.close()